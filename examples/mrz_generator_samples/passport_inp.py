#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Adding mrz to PYTHONPATH to execute this example as script
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
#############################################################

#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import TD3CodeGenerator
from examples.functions.functions import open_image

print(TD3CodeGenerator("P",            # Document type   Normally 'P' for passport
                       "Interpol",     # Country         3 letters code or country name
                       "SPECIMEN",     # Surname(s)      Special characters will be transliterated
                       "SAMPLE",       # Given name(s)   Special characters will be transliterated
                       "XX000000",     # Passport number
                       "FRANCE",       # Nationality     3 letter code or country name
                       "750101",       # Birth date      YYMMDD
                       "F",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       "190730",       # Expiry date     YYMMDD
                       "1234567890"))  # Id number       Non-mandatory field in some countries


open_image("passports", "Interpol.png")
