import unittest
from mrz.checker.td3 import TD3CodeChecker

# unittest for td3 fields()


class TestCase17(unittest.TestCase):

    def test_td3_checker(self):
        mrz_code = ("P<ASUMXHMWD<<EBDALRXHYM<<<<<<<<<<<<<<<<<<<<<\n"
                    "A2222222<0ASU7108215M04120411000146819<<<<44")
        td3_check = TD3CodeChecker(mrz_code)

        fields = td3_check.fields()
        self.assertEqual("MXHMWD", fields.surname)
        self.assertEqual("EBDALRXHYM", fields.name)
        self.assertEqual("ASU", fields.country)
        self.assertEqual("ASU", fields.nationality)
        self.assertEqual("710821", fields.birth_date)
        self.assertEqual("041204", fields.expiry_date)
        self.assertEqual("M", fields.sex)
        self.assertEqual("P", fields.document_type)
        self.assertEqual("A2222222", fields.document_number)
        self.assertEqual("1000146819", fields.optional_data)
        self.assertEqual("5", fields.birth_date_hash)
        self.assertEqual("1", fields.expiry_date_hash)
        self.assertEqual("0", fields.document_number_hash)
        self.assertEqual("4", fields.final_hash)


if __name__ == '__main__':
    unittest.main()
