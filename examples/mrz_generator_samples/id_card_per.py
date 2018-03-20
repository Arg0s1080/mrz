#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from generator.td1 import TD1CodeGenerator
import examples.functions.functions as oi

print(TD1CodeGenerator("I",               # Document type   Normally 'I' or 'ID' for id cards
                       "PER",             # Country         3 letters code or country name
                       "70275722",        # Document number
                       "890612",          # Birth date      YYMMDD
                       "M",               # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "210716",          # Expiry date     YYMMDD
                       "PER",             # Nationality
                       "Cárdenas",        # Surname         Special characters will be transliterated
                       "Jorge Anthony"))  # Given name(s)   Special characters will be transliterated

oi.open_image("id_cards", "Peru.png")
