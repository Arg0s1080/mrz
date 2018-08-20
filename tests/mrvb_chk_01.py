import unittest
from mrz.checker.mrvb import MRVBCodeChecker


class TestCase13(unittest.TestCase):

    def test_mrvb_checker(self):
        mrz_code = ("V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<\n"
                    "L8988901C4XXX4009078F9612109<<<<<<<<")
        mrvb_check = MRVBCodeChecker(mrz_code)

        self.assertTrue(bool(mrvb_check))


if __name__ == '__main__':
    unittest.main()
