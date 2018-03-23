#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import *
import examples.functions.functions as oi

# search for a country by pattern listing the possible results
print("\n".join(find_country("REPUBLIC")))

# get the code of a country
code = get_code("Czech republic")

print(PassportCodeGenerator("P",            # Document type   Normally 'P' for passport
                            code,           # Country         3 letters code or country name
                            "SPECIMEN",     # Surname(s)      Special characters will be transliterated
                            "Vzor",         # Given name(s)   Special characters will be transliterated
                            "99003853",     # Passport number
                            code,           # Nationality     3 letter code or country name
                            "110101",       # Birth date      YYMMDD
                            "M",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                            "120704",       # Expiry date     YYMMDD
                            "110101111"))   # Id number       Non-mandatory field in some countries

oi.open_image("passports", "Czech_Republic.png")
