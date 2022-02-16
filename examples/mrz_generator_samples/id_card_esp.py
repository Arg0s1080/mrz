#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Note for end users: #######################################################################
#
# Adding mrz (local) to PYTHONPATH to execute this example as a script without installing mrz
# (if it was installed using pip or setup.py the two lines below are not necessary)
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
##############################################################################################

from mrz.generator.td1 import TD1CodeGenerator

print(TD1CodeGenerator("ID",                 # Document type   Normally 'I' or 'ID' for id cards
                       "ARG",                # Country         3 letters code or country name
                       "33186544",          # Document number
                       "800101",             # Birth date      YYMMDD
                       "M",                  # Genre           Male: 'M', Female: 'F' or Undefined
                       "8707123610077",             # Expiry date     YYMMDD
                       "ARG",                # Nationality
                       "GONZALEZ",  # Surname         Special characters will be transliterated
                       "GASTON LEONEL",             # Given name(s)   Special characters will be transliterated
                       "99999999R"))         # Optional data 1
