#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td2 import TD2CodeGenerator
from examples.functions.functions import open_image

print(TD2CodeGenerator("I",             # Document type   Normally 'I' or 'ID' for id cards
                       "Utopia",        # Country         3 letters code or country name
                       "ERIKSSON",      # Surname         Special characters will be transliterated
                       "ANNA MARIA",    # Given name(s)   Special characters will be transliterated
                       "D23145890",     # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "UTO",           # Nationality     3 letters code or country name
                       "740812",        # Birth Date      YYMMDD
                       "F",             # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "120415"))       # Expiry date     YYMMDD

open_image("other", "TD2_ICAO_Example.png")
