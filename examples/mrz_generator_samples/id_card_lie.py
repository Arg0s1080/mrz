#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td1 import TD1CodeGenerator
import examples.functions.functions as oi

print(TD1CodeGenerator("ID",           # Document type   Normally 'I' or 'ID' for id cards
                       "LIE",          # Country         3 letters code or country name
                       "ID9875401",    # Document number
                       "820512",       # Birth date      YYMMDD
                       "F",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "190622",       # Expiry date     YYMMDD
                       "LIE",          # Nationality
                       "OSPELT-BECK",  # Surname         Special characters will be transliterated
                       "Marisa"))      # Given name(s)   Special characters will be transliterated

oi.open_image("id_cards", "Liechtenstein.png")
