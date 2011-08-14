
from setuptools import setup, find_packages

install_requires=[
    'setuptools',
    'collective.transmogrifier',
]

try:
    eval("1 if True else 2")  # http://stackoverflow.com/questions/446052
    install_requires.append('configparser')
except SyntaxError:
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
