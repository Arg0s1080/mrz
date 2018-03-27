#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import PassportCodeGenerator
from examples.functions.functions import open_image

print(PassportCodeGenerator("P",           # Document type   Normally 'P' for passport
                            "Utopia",      # Country         3 letters code or country name (fictional ICAO sample)
                            "Eriksson",    # Surname(s)
                            "Anna María",  # Given name(s)
                            "L898902C3",   # Passport number
                            "UTO",         # Nationality     3 letter code or country name (fictional ICAO sample)
                            "740812",      # Birth date      YYMMDD
                            "F",           # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                            "120415",      # Expiry date     YYMMDD
                            "ZE184226B"))  # Id number       Non-mandatory field in some countries

open_image("passports", "ICAO_Example.png")
