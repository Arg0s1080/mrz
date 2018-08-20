import unittest
from mrz.checker.mrvb import MRVBCodeChecker


class TestCase14(unittest.TestCase):

    def test_mrvb_checker(self):
        mrz_code = ("VBD<<DEDIC<<SIDNAN<<<<<<<<<<<<<<<<<<\n"
                    "D091740530BOS8201135M9708011<2020711")
        mrvb_check = MRVBCodeChecker(mrz_code)

        self.assertFalse(bool(mrvb_check))


if __name__ == '__main__':
    unittest.main()
