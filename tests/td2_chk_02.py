import unittest
from mrz.checker.td2 import TD2CodeChecker

# Unittest for td2 fields()


class TestCase16(unittest.TestCase):

    def test_td2_checker(self):
        mrz_td2 = ("I<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<\n"
                   "D231458907UTO7408122F1204159<<<<<<<6")
        td2_check = TD2CodeChecker(mrz_td2)

        fields = td2_check.fields()
        self.assertEqual("ERIKSSON", fields.surname)
        self.assertEqual("ANNA MARIA", fields.name)
        self.assertEqual("UTO", fields.country)
        self.assertEqual("UTO", fields.nationality)
        self.assertEqual("740812", fields.birth_date)
        self.assertEqual("120415", fields.expiry_date)
        self.assertEqual("F", fields.sex)
        self.assertEqual("I", fields.document_type)
        self.assertEqual("D23145890", fields.document_number)
        self.assertEqual("", fields.optional_data)
        self.assertEqual("2", fields.birth_date_hash)
        self.assertEqual("9", fields.expiry_date_hash)
        self.assertEqual("7", fields.document_number_hash)
        self.assertEqual("6", fields.final_hash)


if __name__ == '__main__':
    unittest.main()
