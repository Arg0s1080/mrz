#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td1 import TD1CodeGenerator

print(TD1CodeGenerator("ID",                 # Document type   Normally 'I' or 'ID' for id cards
                       "ESP",                # Country         3 letters code or country name
                       "BAA000589",          # Document number
                       "800101",             # Birth date      YYMMDD
                       "F",                  # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "250101",             # Expiry date     YYMMDD
                       "ESP",                # Nationality
                       "ESPAÑOLA ESPAÑOLA",  # Surname         Special characters will be transliterated
                       "CARMEN",             # Given name(s)   Special characters will be transliterated
                       "99999999R"))         # Optional data 1
