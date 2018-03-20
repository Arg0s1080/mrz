from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name="mzr",
   version="0.1",
   description="Machine readable zone generator and checker for passports and other travel documents",
   license="GPL-3",
   long_description=long_description,
   author='Iván Rincón',
   author_email='ivan.rincon76@gmail.com',
   url="https://github.com/Arg0s1080/mrz",
   packages=["mzr.generator", "mrz.checker"],
)