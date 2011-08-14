
from setuptools import setup, find_packages

install_requires=[
    'setuptools',
    'collective.transmogrifier',
],

try:
    # If we are using Python 2.5 or greater we can require configparser
    eval("1 if True else 2")  # http://stackoverflow.com/questions/446052
    install_requires.append('configparser')
except SyntaxError:
    # If we are using Python 2.4 or lower we cannot require configparser
    pass

setup(
    name='bbb.sucks',
    packages=find_packages(),
    namespace_packages=[
        'bbb',
    ],
    install_requires=install_requires,
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
        'console_scripts': 'bbb = bbb.sucks:main',
    }
)
