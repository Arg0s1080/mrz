#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td1 import *
import examples.functions.functions as oi

print(TD1CodeGenerator(
            "ID",                                 # Document type   Normally 'I' or 'ID' for id cards
            "Serbia",                             # Country         3 letters code or country name
            "955555546",                          # Document number Special characters will be transliterated
            "680229",                             # Birth date      YYMMDD
            "F",                                  # Genre           Male: 'M', Female: 'F' or Undefined 'X'
            "130724",                             # Expiry date     YYMMDD
            "Serbia",                             # Nationality
            "ТЕСТ",                               # Surname         Special characters will be transliterated
            "МИЛИЦА",                             # Given name(s)   Special characters will be transliterated
            "2902968000000",                      # Optional data 1 empty string by default
            "",                                   # Optional data 2 empty string by default
            dictionary.cyrillic_serbian()))       # Transliteration Dictionary (latin by default)

oi.open_image("id_cards", "Serbia.png")
