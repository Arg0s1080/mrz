#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import PassportCodeGenerator, dictionary
from examples.functions.functions import open_image


print(PassportCodeGenerator(
        "P",                  # Document type   Normally 'P' for passport
        "ASU",                # Country         3 letters code or country name
        "محمود",              # Surname(s)      Special characters will be transliterated
        "عبدالرحيم",          # Given name(s)   Special characters will be transliterated
        "A2222222",           # Passport number
        "ASU",                # Nationality     3 letter code or country name
        "710821",             # Birth date      YYMMDD
        "F",                  # Genre           Male: 'M', Female: 'F' or Undefined 'X'
        "041204",             # Expiry date     YYMMDD
        "1000146819",         # Id number       Not mandatory field
        dictionary.arabic(),  # Dictionary      Transliteration dictionary
        force=True))          # Force           Disables checks for country, nationality and document_type fields.

open_image("passports", "ICAO_Example2.png")
