#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import PassportCodeGenerator
import examples.functions.functions as oi

print(PassportCodeGenerator("P",            # Document type   Normally 'P' for passport
                            "TAIWAN",       # Country         3 letters code or country name
                            "LIN",          # Surname(s)
                            "MEI-HUA",      # Given name(s)
                            "000000000",    # Passport number
                            "TAIWAN",       # Nationality     3 letter code or country name
                            "760101",       # Birth date      YYMMDD
                            "F",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                            "140401",       # Expiry date     YYMMDD
                            "A234567893"))  # Id number       Non-mandatory field in some countries

oi.open_image("passports", "China.png")
