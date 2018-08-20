from mrz.checker.mrvb import MRVBCodeChecker

mrvb = ("V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<\n"
        "L8988901C4XXX4009078F9612109<<<<<<<<")

print(MRVBCodeChecker(mrvb))