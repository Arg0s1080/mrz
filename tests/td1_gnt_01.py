import unittest
from mrz.generator.td1 import TD1CodeGenerator


class TestCase01(unittest.TestCase):

    def test_td1_generator(self):
        td1_generator = TD1CodeGenerator("ID", "ESP", "BAA000589", "800101", "F", "250101", "ESP",
                                              "ESPAÑOLA ESPAÑOLA", "CARMEN", "99999999R")

        result = ("IDESPBAA000589599999999R<<<<<<\n"
                  "8001014F2501017ESP<<<<<<<<<<<7\n"
                  "ESPANOLA<ESPANOLA<<CARMEN<<<<<")

        self.assertEqual(str(td1_generator), result)


if __name__ == '__main__':
    unittest.main()
