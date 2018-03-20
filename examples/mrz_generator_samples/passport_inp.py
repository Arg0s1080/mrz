#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from generator.td3 import PassportCodeGenerator
import examples.functions.functions as oi

print(PassportCodeGenerator("P",            # Document type   Normally 'P' for passport
                            "Interpol",     # Country         3 letters code or country name
                            "SPECIMEN",     # Surname(s)      Special characters will be transliterated
                            "SAMPLE",       # Given name(s)   Special characters will be transliterated
                            "XX000000",     # Passport number
                            "FRANCE",       # Nationality     3 letter code or country name
                            "750101",       # Birth date      YYMMDD
                            "F",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                            "190730",       # Expiry date     YYMMDD
                            "1234567890"))  # Id number       Non-mandatory field in some countries


oi.open_image("passports", "Interpol.png")
