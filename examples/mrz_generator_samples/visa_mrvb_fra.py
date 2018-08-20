from mrz.generator.mrvb import MRVBCodeGenerator
from examples.functions.functions import open_image

print(MRVBCodeGenerator(
    "VC",          # Document type   For visas, the first letter must be 'V'
    "FRA",         # Country         3 letters code or country name
    "SPECIMEN",    # Surname(s)      Special characters will be transliterated
    "SPECIMEN",    # Given name(s)   Special characters will be transliterated
    "F00000000",   # Document number
    "UTO",         # Nationality     3 letter code or country name
    "031106",      # Birth date      YYMMDD
    "M",           # Genre           Male: 'M', Female: 'F' or Undefined 'X'
    "140114",      # Expiry date     YYMMDD
    " M300703"))   # Optional data   Not mandatory field

open_image("visas", "France.png")
