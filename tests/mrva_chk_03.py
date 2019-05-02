import unittest
from mrz.checker.mrva import MRVACodeChecker


# unittest for mrva fields()


class TestCase18(unittest.TestCase):

    def test_mrva_checker(self):
        mrz_code = ("VIUSATRAVELER<<HAPPY<PERSON<<<<<<<<<<<<<<<<<\n"
                    "555123ABC6GBR6502056F0412236IFLND00AMS803085")
        mrva_check = MRVACodeChecker(mrz_code)

        fields = mrva_check.fields()

        self.assertEqual("TRAVELER", fields.surname)
        self.assertEqual("HAPPY PERSON", fields.name)
        self.assertEqual("USA", fields.country)
        self.assertEqual("GBR", fields.nationality)
        self.assertEqual("650205", fields.birth_date)
        self.assertEqual("041223", fields.expiry_date)
        self.assertEqual("F", fields.sex)
        self.assertEqual("VI", fields.document_type)
        self.assertEqual("555123ABC", fields.document_number)
        self.assertEqual("IFLND00AMS803085", fields.optional_data)
        self.assertEqual("6", fields.birth_date_hash)
        self.assertEqual("6", fields.expiry_date_hash)
        self.assertEqual("6", fields.document_number_hash)


if __name__ == '__main__':
    unittest.main()
