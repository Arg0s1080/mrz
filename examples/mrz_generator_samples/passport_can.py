#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from generator.td3 import *

td3_generator = PassportCodeGenerator("P",            # Document type   Normally 'P' for passport
                                      "GB",           # Country         3 letters code or country name
                                      "MARTIN",       # Surname(s)      Special characters will be transliterated
                                      "SARAH",        # Given name(s)   Special characters will be transliterated
                                      "980XG47",      # Passport number
                                      "GBR",          # Nationality     3 letter code or country name
                                      "850101",       # Birth date      YYMMDD
                                      "F",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                                      "261228",       # Expiry date     YYMMDD
                                      "ID88933477")   # Id number       Not mandatory field

print(td3_generator)

td3_generator.country_code = "CAN"
td3_generator.document_number = "ZE000509"
td3_generator.nationality = "CAN"
td3_generator.expiry_date = "230114"
td3_generator.id_number = ""

print(td3_generator)
