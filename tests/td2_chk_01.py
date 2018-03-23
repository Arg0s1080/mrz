import unittest
from mrz.checker.td2 import TD2CodeChecker


class TestCase08(unittest.TestCase):

    def test_td2_generator(self):
        mrz_td2 = ("I<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<\n"
                   "D231458907UTO7408122F1204159<<<<<<<6")
        self.assertTrue(bool(TD2CodeChecker(mrz_td2)))


if __name__ == '__main__':
    unittest.main()
