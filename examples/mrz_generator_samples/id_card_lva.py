#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from generator.td1 import TD1CodeGenerator
import examples.functions.functions as oi

print(TD1CodeGenerator("I",              # Document type   Normally 'I' or 'ID' for id cards
                       "LVA",            # Country         3 letters code or country name
                       "PA9992921",      # Document number
                       "821212",         # Birth date      YYMMDD
                       "M",              # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "170305",         # Expiry date     YYMMDD
                       "LVA",            # Nationality
                       "PARAUDZINŠ",     # Surname         Special characters will be transliterated
                       "ANDRIS",         # Given name(s)   Special characters will be transliterated
                       "121282-88882"))  # Optional data 1 empty string by default


oi.open_image("id_cards", "Latvia.png")









