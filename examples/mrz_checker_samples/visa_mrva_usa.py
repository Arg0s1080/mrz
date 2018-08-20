from mrz.checker.mrva import MRVACodeChecker

mrz_code = ("VNUSATRAVELER<<HAPPY<<<<<<<<<<<<<<<<<<<<<<<<\n"
            "1234567897CAN6612120M1407282B3XLC000FD142955")

checker = MRVACodeChecker(mrz_code)

print(checker.result)
