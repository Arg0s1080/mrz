import unittest
from mrz.generator.td1 import TD1CodeGenerator, dictionary


class TestCase02(unittest.TestCase):

    def test_td1_generator(self):
        td1_generator = TD1CodeGenerator("id", "srb", "955555546", "680229", "f", "130724", "seRbIA",
                                         "Тест", "Милица", "2902968000000", "", dictionary.cyrillic_serbian())

        result = ("IDSRB95555554612902968000000<<\n"
                  "6802295F1307245SRB<<<<<<<<<<<6\n"
                  "TEST<<MILICA<<<<<<<<<<<<<<<<<<")

        self.assertEqual(str(td1_generator), result)


if __name__ == '__main__':
    unittest.main()

