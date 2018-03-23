# -*- coding: UTF8 -*-

from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="mzr",
    version="0.1",
    description="Machine readable zone generator and checker for passports and other travel documents",
    license="GPLv3",
    long_description=long_description,
    author='Ivan Rincon',
    author_email='ivan.rincon76@gmail.com',
    url="https://github.com/Arg0s1080/mrz",
    keywords="mrz passports id cards td1 td2 td3 icao",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: Security"
    ]
)