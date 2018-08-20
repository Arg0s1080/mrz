import unittest
from mrz.checker.mrva import MRVACodeChecker


class TestCase12(unittest.TestCase):

    def test_mrva_checker(self):
        mrva_code = ("V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\n"
                     "L8988901C4XXX4009078F96121096ZE184226B<<<<<<")
        mrva_check = MRVACodeChecker(mrva_code, check_expiry=True, compute_warnings=True)

        self.assertFalse(bool(mrva_check))


if __name__ == '__main__':
    unittest.main()
