import unittest
from mrz.checker.td3 import TD3CodeChecker


class TestCase09(unittest.TestCase):

    mrz_td3 = ("P<UTOMXHMWD<<EBDALRXHYM<<<<<<<<<<<<<<<<<<<<<\n"
               "A2222222<0UTO7108215F04120411000146819<<<<44")

    def test_a_td3_checker(self):
        self.assertTrue(bool(TD3CodeChecker(self.mrz_td3)))

    def test_b_td3_checker(self):
        self.assertListEqual(TD3CodeChecker(self.mrz_td3, check_expiry=True).report_warnings, ['document expired'])

    def test_c_td3_checker(self):
        self.assertFalse(bool(TD3CodeChecker(self.mrz_td3, check_expiry=True, compute_warnings=True)))


if __name__ == '__main__':
    unittest.main()
