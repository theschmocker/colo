from setuptools import setup

NAME = 'colo'
DESCRIPTION = 'A simple tool to convert hex colors to other formats for CSS'
URL = 'https://github.com/theschmocker/colo.git'
AUTHOR = 'Jacob Schmocker'

VERSION = None

REQUIRED = [
    'Click',
]

setup(
    name=NAME,
    author=AUTHOR,
    url=URL,
    install_requires=REQUIRED,
    packages=['colo'],
    entry_points = {
        'console_scripts': [
            'colo = colo.__main__:cli'
        ]
    }
)
