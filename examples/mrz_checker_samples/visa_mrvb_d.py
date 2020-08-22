from mrz.checker.mrvb import *
from examples.functions.functions import open_image

mrz_code = ("VBD<<DEDIC<<SIDNAN<<<<<<<<<<<<<<<<<<\n"
            "D091740530BOS8201135M9708011<2020711")

checker = MRVBCodeChecker(mrz_code, check_expiry=True)
ok = bool(checker)

print("The visa is: %s" % ok)

if not ok:
    print("FALSE")
    for false in checker.report.falses:
        print("- %s" % false[0])

    print("WARNINGS")
    for warning in checker.report.warnings:
        print("- %s" % warning)


print()
nationality_code = "BOS"  # nationality = BOS (deprecated or invalid country name)
print("%s is a valid country code: %s" % (nationality_code, is_code(nationality_code)))
print("%s is the code of: %s" % (nationality_code, get_country(nationality_code)))


print("==========================================")


mrz_code = ("VBD<<DEDIC<<SIDNAN<<<<<<<<<<<<<<<<<<\n"
            "D091740530BIH8201135M9708011<2020711")  # nationality = BIH


checker = MRVBCodeChecker(mrz_code)
ok = bool(checker)

print("The visa is: %s" % ok)
print()

nationality_code = "BIH"
print("%s is the code of: %s" % (nationality_code, get_country(nationality_code)))
