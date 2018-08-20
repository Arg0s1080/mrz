from mrz.generator.mrvb import MRVBCodeGenerator
from examples.functions.functions import open_image

print(MRVBCodeGenerator(
    "VD",          # Document type   For visas, the first letter must be 'V'
    "GBR",         # Country         3 letters code or country name
    "MUNIR",       # Surname(s)      Special characters will be transliterated
    "FAISAL",      # Given name(s)   Special characters will be transliterated
    "AD0725981",   # Document number
    "PAK",         # Nationality     3 letter code or country name
    "760815",      # Birth date      YYMMDD
    "M",           # Genre           Male: 'M', Female: 'F' or Undefined 'X'
    "061116"))     # Expiry date     YYMMDD


open_image("visas", "United_Kingdom.png")
