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


from mrz.generator.mrvb import MRVBCodeGenerator
from examples.functions.functions import open_image

print(MRVBCodeGenerator(
    "VB",          # Document type   For visas, the first letter must be 'V'
    "D",           # Country         3 letters code or country name. Note: Germany it's an
    #                                exception. Only uses one letter
    "DEDIC",       # Surname(s)      Special characters will be transliterated
    "SIDNAN",      # Given name(s)   Special characters will be transliterated
    "D09174053",   # Document number
    "BOS",         # Nationality     3 letter code or country name.  Note: 'BOS' is deprecated
    "820113",      # Birth date      YYMMDD
    "M",           # Genre           Male: 'M', Female: 'F' or Undefined 'X'
    "970801",      # Expiry date     YYMMDD
    " 2020711",    # Optional data   Not mandatory field
    force=True))   # Force           Disables checks for country, nationality and document_type
                   #                 fields. Note: 'BOS' is deprecated or non-normative

open_image("visas", "Germany.png")
