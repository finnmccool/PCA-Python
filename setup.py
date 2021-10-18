from __future__ import print_function, unicode_literals
from setuptools import setup, find_packages

$Import

__author__ = "$USER"

with open("requirements.txt", 'r') as file:
    requirements = file.readlines()
    
with open("readme.md", 'r') as file:
    readme = file.read()

with open("LICENSE", 'r') as file:
    license = file.read()

setup(
    name='$Package_name',
    version='$Version',
    packages=find_packages(),
    #url='https://github.com/danishabdullah/$Package_name',
    install_requires=requirements,
    license=license,
    zip_safe=False,
    keywords='$Package_name ',
    author='Graeme McMillan',
    author_email='graemedonmcmillan@gmail.com',
    description='$Package_name',
    package_data={
        '': ['requirements.txt', 'readme.md', 'LICENSE']
    },
    entry_points={
        'console_scripts': ['$Package_name=$Package_name.scripts.cli:cli']
    },
    long_description=readme,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
