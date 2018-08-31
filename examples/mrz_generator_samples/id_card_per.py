#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Adding mrz to PYTHONPATH to execute this example as script
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
#############################################################

from mrz.generator.td1 import TD1CodeGenerator
from examples.functions.functions import open_image

print(TD1CodeGenerator("I",               # Document type   Normally 'I' or 'ID' for id cards
                       "PER",             # Country         3 letters code or country name
                       "70275722",        # Document number
                       "890612",          # Birth date      YYMMDD
                       "M",               # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "210716",          # Expiry date     YYMMDD
                       "PER",             # Nationality
                       "Cárdenas",        # Surname         Special characters will be transliterated
                       "Jorge Anthony"))  # Given name(s)   Special characters will be transliterated

open_image("id_cards", "Peru.png")
