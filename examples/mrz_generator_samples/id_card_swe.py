#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td1 import TD1CodeGenerator
from examples.functions.functions import open_image

print(TD1CodeGenerator("I",              # Document type   Normally 'I' or 'ID' for id cards
                       "Sweden",         # Country         3 letters code or country name
                       "59000002",       # Document number Special characters will be transliterated
                       "870314",         # Birth date      YYMMDD
                       "M",              # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "170102",         # Expiry date     YYMMDD
                       "SWEDEN",         # Nationality
                       "SPECIMEN",       # Surname         Special characters will be transliterated
                       "SVEN",           # Given name(s)   Special characters will be transliterated
                       "198703142391"))

open_image("id_cards", "Sweden.png")
