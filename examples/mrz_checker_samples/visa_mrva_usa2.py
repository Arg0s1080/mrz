from mrz.checker.mrva import MRVACodeChecker
from examples.functions.functions import open_image


mrz_code = ("VIUSATRAVELER<<HAPPYPERSON<<<<<<<<<<<<<<<<<<\n"
            "555123ABC6GBR6502056F0412236IFLND00AMS803085")

print(MRVACodeChecker(mrz_code))

open_image("visas", "USA2.png")
