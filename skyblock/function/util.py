from itertools import cycle
from math import isinf
from os import name as os_name
from re import fullmatch, sub
from subprocess import call
from textwrap import wrap
from types import FunctionType
from typing import Optional

from ..constant.colors import CRIT_COLORS
from ..constant.enchanting import ENCHS
from ..constant.mobs import BESTIARY_ALTER
from ..constant.util import (
    NUMBER_SCALES, ROMAN_NUM, SPECIAL_ZONES, SPECIAL_NAMES,
    SPECIAL_ALTER, IGNORED_WORDS, UPGRADE_ATTRS, Number,
)

from .io import red, yellow


__all__ = [
    'camel_to_under', 'checkpoint', 'clear', 'format_name', 'format_number',
    'format_roman', 'format_short', 'format_zone', 'get', 'get_family', 'generate_help',
    'includes', 'includes_id', 'index', 'is_valid_usage',
]


def camel_to_under(string: str) -> str:
    return sub(r'([A-Z])', r'_\1', string)[1:].lower()


def checkpoint(func: FunctionType, /) -> FunctionType:
    def result(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            yellow('\nKeyboardInterruption')

    result.__name__ = func.__name__
    result.__doc__ = func.__doc__
    return result


if os_name == 'nt':
    def clear():
        call(['cls'], shell=True)
else:
    def clear():
        call(['clear'])


def _format_word(word: str, /) -> str:
    return word.lower() if word in IGNORED_WORDS else word.capitalize()


def format_crit(string: str, /) -> str:
    result = ''
    color_iter = iter(cycle(CRIT_COLORS))
    last_color = next(color_iter)
    next_color = last_color

    for i, char in enumerate(string):
        if fullmatch(r'\d', char):
            last_color = next_color
        result += last_color
        if i == 0:
            result += '✧'
        result += char
        if fullmatch(r'\d', char):
            next_color = next(color_iter)
    result += '✧'
    return result


def format_name(name: str, /) -> str:
    result = name
    for original, alternative in SPECIAL_NAMES.items():
        if result.endswith(original):
            result = result.replace(original, alternative)
            break
    else:
        result = result.replace('_', ' ')
        result = ' '.join(_format_word(word) for word in result.split(' '))
    for original, alternative in SPECIAL_ALTER.items():
        if result.startswith(original):
            result = result.replace(original, alternative)
            break
    return result


def format_number(number: Number, /, *, sign: bool = False) -> str:
    if isinf(number):
        if sign:
            return '+∞' if number > 0 else '-∞'
        else:
            return '∞' if number > 0 else '-∞'

    if sign:
        sign_str = '+' if number >= 0 else '-'
    else:
        sign_str = '' if number >= 0 else '-'
    number = abs(number)

    if number % 1 == 0:
        string = f'{number:.0f}'
        string = ','.join(part[::-1] for part in wrap(string[::-1], 3)[::-1])
    else:
        string = f'{number:.1f}'
        integer, floating = string.split('.')
        integer = ','.join(part[::-1] for part in wrap(integer[::-1], 3)[::-1])
        string = f'{integer}.{floating}'
    return f'{sign_str}{string}'


def format_rarity(rarity: str, /) -> str:
    return rarity.upper().replace('_', ' ')


def format_roman(number: int, /) -> str:
    result = ''
    for letter, amount in reversed(ROMAN_NUM):
        while number >= amount:
            number -= amount
            result += letter
    return result


def format_short(number: Number, /) -> str:
    for letter, amount in reversed(NUMBER_SCALES):
        if number >= amount:
            break
    else:
        amount = 1
        letter = ''
    string = f'{number / amount:.1f}'
    if string.endswith('.0'):
        string = string[:-2]
    return f'{string}{letter}'


def format_zone(name: str, /) -> str:
    if name in SPECIAL_ZONES:
        return SPECIAL_ZONES[name]
    else:
        result = name.replace('_', ' ')
        return ' '.join(_format_word(word) for word in result.split(' '))


def generate_help(doc: str, /) -> dict[str, str]:
    description = {}

    for para in doc.split('\n\n'):
        desc = para.split('\n')[-1]
        for _cmd in para.split('\n')[:-1]:
            description[
                ' '.join(part for part in _cmd[2:].split()
                         if not part.startswith(('[', '<')))
            ] = (_cmd, desc)

    return description


def get(ls: list[any], /, name: str | None = None,
        default: Optional[any] = None, **kwargs) -> any:
    attrs = {}
    args = {}
    for key, value in kwargs.items():
        if key in {'count'} | UPGRADE_ATTRS:
            attrs[key] = value
        elif key not in {'type'}:
            args[key] = value

    for item in ls:
        if name is not None and item.name != name:
            continue
        for key, value in args.items():
            if getattr(item, key, None) != value:
                break
        else:
            result = item.copy() if hasattr(item, 'copy') else item
            for attr, value in attrs.items():
                setattr(result, attr, value)
            return result

    return default.copy() if hasattr(default, 'copy') else default


def get_ench(name: str, /) -> tuple[str, tuple[int]]:
    for row in ENCHS:
        if row[0] == name:
            if isinstance(row[2], tuple):
                return row[2]
            exp_levels = tuple(lvl * row[2] + row[3]
                               for lvl in range(1, row[1] + 1))
            return exp_levels
    else:
        raise ValueError(f'Enchantment not found: {name!r}')


def get_family(name: str, /) -> str:
    for family, others in BESTIARY_ALTER.items():
        if name in others:
            return family
    return name


def includes(ls: list[any], name: str, /) -> bool:
    for obj in ls:
        if obj.name == name:
            return True
    return False


def includes_id(ls: list[any], id_: str, /) -> bool:
    for obj in ls:
        if obj.id == id_:
            return True
    return False


def index(ls: list[any], name: str, /, *, err=True) -> int:
    for i, obj in enumerate(ls):
        if obj.name == name:
            return i
    if err:
        raise ValueError(f'{name!r} not found from the list.')


def is_valid_usage(usage: str, words: list[str], /) -> bool:
    all_words = usage.split()[1:]
    pos_words = [word for word in all_words if word[0] != '[']
    return len(pos_words) <= len(words) <= len(all_words)


def parse_int(string: str, /, *, warn=True) -> int | None:
    if fullmatch(r'\d+', string):
        return int(string)
    elif warn:
        red('Please input a valid number!')
