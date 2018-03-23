#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from mrz.generator.td3 import *
import examples.functions.functions as oi


print(PassportCodeGenerator("P",            # Document type   Normally 'P' for passport
                            "JPN",          # Country         3 letters code or country name
                            "GAIMU",        # Surname(s)
                            "SAKURA",       # Given name(s)
                            "XS1234567",    # Passport number
                            "Japan",        # Nationality     3 letter code or country name
                            "790220",       # Birth date      YYMMDD
                            "F",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                            "160320"))       # Expiry date     YYMMDD

oi.open_image("passports", "Japan.png")
