from setuptools import setup


setup(
    name='skyblock-peterhunt',
    version='0.1.0',
    author='Peter Hunt',
    author_email='huangtnhao@gmail.com',
    description=('Hypixel Skyblock Remake in Python.'
                 ' A command-line-based RPG game.'),
    packages=['skyblock'],
    url='https://github.com/treesontop/skyblock',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.10',
)
