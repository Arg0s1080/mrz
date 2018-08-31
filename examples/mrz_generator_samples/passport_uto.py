#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Adding mrz to PYTHONPATH to execute this example as script
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
#############################################################

from mrz.generator.td3 import TD3CodeGenerator
from examples.functions.functions import open_image

print(TD3CodeGenerator("P",           # Document type   Normally 'P' for passport
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
