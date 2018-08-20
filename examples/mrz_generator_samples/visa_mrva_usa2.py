from mrz.generator.mrva import MRVBCodeGenerator
from examples.functions.functions import open_image

print(MRVBCodeGenerator(
    "VI",                  # Document type   For visas, the first letter must be 'V'
    "USA",                 # Country         3 letters code or country name
    "TRAVELER",            # Surname(s)      Special characters will be transliterated
    "HAPPYPERSON",         # Given name(s)   Special characters will be transliterated
    "555123ABC",           # Document number
    "GBR",                 # Nationality     3 letter code or country name
    "650205",              # Birth date      YYMMDD
    "F",                   # Genre           Male: 'M', Female: 'F' or Undefined 'X'
    "041223",              # Expiry date     YYMMDD
    "IFLND00AMS803085"))   # Optional data   Not mandatory field

open_image("visas", "USA2.png")
