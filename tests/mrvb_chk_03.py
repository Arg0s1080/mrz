import unittest
from mrz.checker.mrvb import MRVBCodeChecker, get_country


class TestCase19(unittest.TestCase):

    def test_mrvb_checker(self):
        # unittest for mrvb fields()
        mrz_code = ("VBD<<DEDIC<<SIDNAN<<<<<<<<<<<<<<<<<<\n"
                    "D091740530BIH8201135M9708011<2020711")
        mrvb_check = MRVBCodeChecker(mrz_code)

        fields = mrvb_check.fields()
        self.assertEqual("DEDIC", fields.surname)
        self.assertEqual("SIDNAN", fields.name)
        self.assertEqual("Germany", get_country(fields.country))
        self.assertEqual("BIH", fields.nationality)
        self.assertEqual("820113", fields.birth_date)
        self.assertEqual("970801", fields.expiry_date)
        self.assertEqual("M", fields.sex)
        self.assertEqual("VB", fields.document_type)
        self.assertEqual("D09174053", fields.document_number)
        self.assertEqual("2020711", fields.optional_data)
        self.assertEqual("5", fields.birth_date_hash)
        self.assertEqual("1", fields.expiry_date_hash)
        self.assertEqual("0", fields.document_number_hash)


if __name__ == '__main__':
    unittest.main()
