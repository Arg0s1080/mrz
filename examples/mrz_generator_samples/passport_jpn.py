#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from mrz.generator.td3 import *
from examples.functions.functions import open_image


print(TD3CodeGenerator("P",          # Document type   Normally 'P' for passport
                       "JPN",        # Country         3 letters code or country name
                       "GAIMU",      # Surname(s)      Special characters will be transliterated
                       "SAKURA",     # Given name(s)   Special characters will be transliterated
                       "XS1234567",  # Passport number
                       "Japan",      # Nationality     3 letter code or country name
                       "790220",     # Birth date      YYMMDD
                       "F",          # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "160320"))    # Expiry date     YYMMDD

open_image("passports", "Japan.png")
