#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import TD3CodeGenerator
from examples.functions.functions import open_image

print(TD3CodeGenerator("P",                   # Document type   Normally 'P' for passport
                       "QATAR",               # Country         3 letters code or country name
                       "AL-KAABI",            # Surname(s)
                       "ALI HAMAD ABDULLAH",  # Given Names     Special characters will be transliterated
                       "00000000",            # Passport number Special characters will be transliterated
                       "QAT",                 # Nationality     3 letter code or country name
                       "710307",              # Birth date      YYMMDD
                       "M",                   # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "110725",              # Expiry date     YYMMDD
                       "12345458902"))        # Id number       Non-mandatory field in some countries

open_image("passports", "Qatar.png")
