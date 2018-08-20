from mrz.checker.mrvb import MRVBCodeChecker

mrz_code = ("VDGBRMUNIR<<FAISAL<<<<<<<<<<<<<<<<<<\n"
            "AD07259817PAK7608151M0611165<<<<<<<<")

print(MRVBCodeChecker(mrz_code))
