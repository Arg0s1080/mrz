import unittest
from mrz.checker.td1 import TD1CodeChecker


class TestCase06(unittest.TestCase):

    def test_td1_generator(self):
        mrz_td1 = ("IDLIEID98754015<<<<<<<<<<<<<<<\n"
                   "8205122M1906224LIE<<<<<<<<<<<6\n"
                   "OSPELT<BECK<<MARISA<<<<<<<<<<<")
        td1_check = TD1CodeChecker(mrz_td1)

        self.assertTrue(bool(td1_check))


if __name__ == '__main__':
    unittest.main()
