from mrz.generator.mrvb import MRVBCodeGenerator
from examples.functions.functions import open_image

print(MRVBCodeGenerator(
    "V",           # Document type   For visas, the first letter must be 'V'
    "UTO",         # Country         3 letters code or country name
    "ERIKSSON",    # Surname(s)      Special characters will be transliterated
    "ANNA MARIA",  # Given name(s)   Special characters will be transliterated
    "L8988901C",   # Document number
    "Unknown",     # Nationality     3 letter code or country name
    "400907",      # Birth date      YYMMDD
    "F",           # Genre           Male: 'M', Female: 'F' or Undefined 'X'
    "961210"))     # Expiry date     YYMMDD

open_image("visas", "MRVB_ICAO_Example.png")