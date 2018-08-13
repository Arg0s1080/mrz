#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import *
from examples.functions.functions import open_image


print(PassportCodeGenerator(
        "P",                               # Document type   Normally 'P' for passport
        "UKRAINE",                         # Country         3 letters code or country name
        "ТКАЧЕНКО",                        # Surname(s)      Special characters will be transliterated
        "МАР'ЯНА",                         # Given name(s)   Special characters will be transliterated
        "XX000000",                        # Passport number
        "UKRAINE",                         # Nationality     3 letter code or country name
        "910824",                          # Birth date      YYMMDD
        "F",                               # Genre           Male: 'M', Female: 'F' or Undefined 'X'
        "230925",                          # Expiry date     YYMMDD
        "1234567890",                      # Id number       Not mandatory field
        dictionary.cyrillic_ukrainian()))  # Dictionary      Transliteration dictionary

open_image("passports", "Ukraine.png")
