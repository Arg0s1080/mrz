#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from generator.td1 import TD1CodeGenerator
import examples.functions.functions as oi

print(TD1CodeGenerator("I",              # Document type   Normally 'I' or 'ID' for id cards
                       "LTU",            # Country         3 letters code or country name
                       "11810187",       # Document number
                       "641123",         # Birth date      YYMMDD
                       "F",              # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "190101",         # Expiry date     YYMMDD
                       "LTU",            # Nationality
                       "BASANAVIČIENĖ",  # Surname         Special characters will be transliterated
                       "BIRUTĖ",         # Given name(s)   Special characters will be transliterated
                       "46411231034"))   # Optional data 1

oi.open_image("id_cards", "Lithuania.png")
