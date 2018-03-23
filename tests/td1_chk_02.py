import unittest
from mrz.checker.td1 import TD1CodeChecker


class TestCase07(unittest.TestCase):

    def test_td1_generator(self):
        mrz_td1 = ("IDSRB95555554612902968000000<<\n"
                   "6802295F1307245SRB<<<<<<<<<<<6\n"
                   "TEST<<MILICA<<<<<<<<<<<<<<<<<<")
        td1_check = TD1CodeChecker(mrz_td1)

        self.assertTrue(bool(td1_check))


if __name__ == '__main__':
    unittest.main()
