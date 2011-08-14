
from setuptools import setup, find_packages

setup(
    name='bbb.sucks',
    packages=find_packages(),
    namespace_packages=[
        'bbb',
    ],
    install_requires=[
        'setuptools',
        'collective.transmogrifier',
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
        'console_scripts': 'bbb = bbb.sucks:main',
    }
)
