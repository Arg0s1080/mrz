#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import *
from examples.functions.functions import open_image


print(PassportCodeGenerator("PA",           # Document type   Normally 'P' for passport
                            "Iceland",      # Country         3 letters code or country name
                            "ÆVARSDÓTTIR",  # Surname(s)      Special characters will be transliterated
                            "ÞURÍÐUR ÖSP",  # Given name(s)   Special characters will be transliterated
                            "A2040611",     # Passport number
                            "ICELAND",       # Nationality     3 letter code or country name
                            "121212",       # Birth date      YYMMDD
                            "F",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                            "110629",       # Expiry date     YYMMDD
                            "121212-1239"))  # Id number       Non-mandatory field in some countries

open_image("passports", "Iceland.png")
