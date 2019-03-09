#!/usr/bin/python3
# -*- coding: UTF8 -*-

from setuptools import setup
from os import path
from mrz import __version__ as version

parent = path.abspath(path.dirname(__file__))

with open(path.join(parent, "README.rst"), 'r') as readme:
    long_description = readme.read()

setup(
    name="mrz",
    version=version,
    description="Machine readable zone generator and checker for passports, visas, id cards and other travel documents",
    license="GPLv3",
    long_description=long_description,
    author='Ivan Rincon',
    author_email='ivan.rincon76@gmail.com',
    url="https://github.com/Arg0s1080/mrz",
    keywords="mrz passports visas id cards td1 td2 td3 mrva mrvb icao",
    packages=["mrz", "mrz.base", "mrz.checker", "mrz.generator", "mrz.generator.dictionaries"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: Security"
    ]
)
