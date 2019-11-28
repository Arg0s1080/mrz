#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Note for end users: #######################################################################
#
# Adding mrz (local) to PYTHONPATH to execute this example as a script without installing mrz
# (if it was installed using pip or setup.py the three lines below are not necessary)
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
##############################################################################################

from mrz.generator.mrva import MRVACodeGenerator
from examples.functions.functions import open_image

print(MRVACodeGenerator(
    "VN",                  # Document type   For visas, the first letter must be 'V'
    "USA",                 # Country         3 letters code or country name
    "TRAVELER",            # Surname(s)      Special characters will be transliterated
    "HAPPY",               # Given name(s)   Special characters will be transliterated
    "123456789",           # Document number
    "CAN",                 # Nationality     3 letter code or country name
    "661212",              # Birth date      YYMMDD
    "M",                   # Genre           Male: 'M', Female: 'F' or Undefined 'X'
    "140728",              # Expiry date     YYMMDD
    "B3XLC000FD142955"))   # Optional data   Not mandatory field

open_image("visas", "USA.png")
