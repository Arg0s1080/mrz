import unittest
from mrz.checker.td3 import TD3CodeChecker


class TestCase10(unittest.TestCase):

    def test_td3_generator(self):
        mrz_td3 = ("P<UKRTKACHENKO<<MARIANA<<<<<<<<<<<<<<<<<<<<<\n"
                   "XX000000<0UKR9108242F23092571234567890<<<<70")
        self.assertTrue(bool(TD3CodeChecker(mrz_td3)))


if __name__ == '__main__':
    unittest.main()
