#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td1 import TD1CodeGenerator
import examples.functions.functions as oi

print(TD1CodeGenerator("I",          # Document type   Normally 'I' or 'ID' for id cards
                       "Monaco",     # Country         3 letters code or country name
                       "029067",     # Document number
                       "990101",     # Birth date      YYMMDD
                       "F",          # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "090324",     # Expiry date     YYMMDD
                       "Monaco",     # Nationality
                       "SPECIMEN",   # Surname         Special characters will be transliterated
                       "SPECIMEN"))  # Given name(s)   Special characters will be transliterated

oi.open_image("id_cards", "Monaco.png")
