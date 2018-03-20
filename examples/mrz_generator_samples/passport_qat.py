#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from generator.td3 import PassportCodeGenerator
import examples.functions.functions as oi

print(PassportCodeGenerator("P",                  # Document type   Normally 'P' for passport
                            "QATAR",              # Country         3 letters code or country name
                            "AL-KAABI",           # Surname(s)
                            "ALI HAMAD ABDULLAH", # Given Names
                            "00000000",           # Passport number
                            "QAT",                # Nationality     3 letter code or country name
                            "710307",             # Birth date      YYMMDD
                            "M",                  # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                            "110725",             # Expiry date     YYMMDD
                            "12345458902"))       # Id number       Non-mandatory field in some countries

oi.open_image("passports", "Qatar.png")
