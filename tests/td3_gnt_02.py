import unittest
from generator.td3 import PassportCodeGenerator, dictionary


class TestCase05(unittest.TestCase):

    def test_td3_generator(self):
        td3_generator = PassportCodeGenerator("P", "UKRAINE", "ТКАЧЕНКО", "МАР'ЯНА", "XX000000", "UKRAINE",
                                              "910824", "F", "230925", "1234567890", dictionary.cyrillic_ukrainian())

        result = ("P<UKRTKACHENKO<<MARIANA<<<<<<<<<<<<<<<<<<<<<\n"
                  "XX000000<0UKR9108242F23092571234567890<<<<70")

        self.assertEqual(str(td3_generator), result)


if __name__ == '__main__':
    unittest.main()
