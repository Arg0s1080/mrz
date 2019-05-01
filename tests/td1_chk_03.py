import unittest
from mrz.checker.td1 import TD1CodeChecker,get_country

# unittest for td1 fields()


class TestCase15(unittest.TestCase):

    def test_td1_checker(self):
        mrz_code = ("IDESPBAA000589599999999R<<<<<<\n"
                    "8001014F2501017ESP<<<<<<<<<<<7\n"
                    "ESPANOLA<ESPANOLA<<CARMEN<<<<<")
        td1_check = TD1CodeChecker(mrz_code)

        fields = td1_check.fields()
        self.assertEqual("ESPANOLA ESPANOLA", fields.surname)
        self.assertEqual("CARMEN", fields.name)
        self.assertEqual("ESP", fields.country)
        self.assertEqual("Spain", get_country(fields.country))
        self.assertEqual("ESP", fields.nationality)
        self.assertEqual("Spain", get_country(fields.nationality))
        self.assertEqual("800101", fields.birth_date)
        self.assertEqual("250101", fields.expiry_date)
        self.assertEqual("F", fields.sex)
        self.assertEqual("ID", fields.document_type)
        self.assertEqual("BAA000589", fields.document_number)
        self.assertEqual("99999999R", fields.optional_data)
        self.assertEqual("4", fields.birth_date_hash)
        self.assertEqual("7", fields.expiry_date_hash)
        self.assertEqual("5", fields.document_number_hash)
        self.assertEqual("7", fields.final_hash)
        self.assertEqual("", fields.optional_data_2)


if __name__ == '__main__':
    unittest.main()
