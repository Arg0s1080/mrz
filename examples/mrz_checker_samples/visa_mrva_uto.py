from mrz.checker.mrva import MRVACodeChecker
from examples.functions.functions import open_image


mrva_code = ("V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\n"
             "L8988901C4XXX4009078F96121096ZE184226B<<<<<<")

checker = MRVACodeChecker(mrva_code, check_expiry=True)  # Check expiry date as warning

print("Expiry date : %s" % checker.expiry_date)                # True              (It's a real date)
print("Warning ....: %s" % "".join(checker.report_warnings))   # document expired
print("VISA .......: %s" % str(checker).upper())               # TRUE

checker = MRVACodeChecker(mrva_code, check_expiry=True, compute_warnings=True)  # Compute Warnings as False
print()
print("Expiry date : %s" % checker.expiry_date)                # False
print("Warning ....: %s" % "".join(checker.report_warnings))   # document expired
print("VISA .......: %s" % str(checker).upper())               # FALSE

print()
open_image("visas", "MRVA_ICAO_Example.png")
