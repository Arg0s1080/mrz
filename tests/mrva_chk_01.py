import unittest
from mrz.checker.mrva import MRVACodeChecker


class TestCase11(unittest.TestCase):

    def test_mrva_checker(self):
        mrz_code = ("VNUSATRAVELER<<HAPPY<<<<<<<<<<<<<<<<<<<<<<<<\n"
                    "1234567897CAN6612120M1407282B3XLC000FD142955")
        mrva_check = MRVACodeChecker(mrz_code)

        self.assertTrue(bool(mrva_check))


if __name__ == '__main__':
    unittest.main()
