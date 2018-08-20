from mrz.checker.mrvb import MRVBCodeChecker

mrz_code = ("VCFRASPECIMEN<<SPECIMEN<<<<<<<<<<<<<\n"
            "F000000005UTO0311063M1401143<M300703")

ok = bool(MRVBCodeChecker(mrz_code))

print("Valid visa code: %s" % ok)
