import unittest
from mrz.generator.td2 import TD2CodeGenerator


class TestCase03(unittest.TestCase):

    def test_td2_generator(self):
        td2_generator = TD2CodeGenerator("I", "Utopia", "ERIKSSON", "ANNA MARIA", "D23145890",
                                         "UTO", "740812", "F", "120415")

        result = ("I<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<\n"
                  "D231458907UTO7408122F1204159<<<<<<<6")

        self.assertEqual(str(td2_generator), result)


if __name__ == '__main__':
    unittest.main()
