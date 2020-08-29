import unittest
from mrz.checker.td1 import TD1CodeChecker

# unittest for Report


class TestCase21(unittest.TestCase):
    def test_a_td1_checker(self):
        # WARNINGS 1:

        mrz_code = ("IDSRB95555554612902968000000<<\n"
                    "6802295F5007245SRB<<<<<<<<<<<6\n"
                    "DR<TEST<TEST<<MILICA<MILICAAAA")

        test = TD1CodeChecker(mrz_code, check_expiry=True)

        warnings = ['expiry date greater than 10 years', 'possible truncating',
                    'Possible not recommended prefix or suffix in identifier']

        self.assertListEqual(warnings, test.report.warnings)

    def test_b_td1_checker(self):
        # WARNINGS 2:

        mrz_code = ("IDSRB95555554612902968000000<<\n"
                    "6802295F1907245SRB<<<<<<<<<<<6\n"
                    "TEST<<<<<<<<<<<<<<<<<<<<<<<<<<")

        test = TD1CodeChecker(mrz_code, check_expiry=True)

        warnings = ['document expired', 'only one identifier']

        self.assertListEqual(warnings, test.report.warnings)


if __name__ == '__main__':
    unittest.main()
