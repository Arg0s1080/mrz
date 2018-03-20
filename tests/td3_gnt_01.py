import unittest
from generator.td3 import PassportCodeGenerator, dictionary


class TestCase04(unittest.TestCase):

    def test_td3_generator(self):
        td3_generator = PassportCodeGenerator("P", "ASU", "محمود", "عبدالرحيم", "A2222222",
                                              "ASU", "710821", "F", "041204", "1000146819",
                                              dictionary.arabic(), force=True)

        result = ("P<ASUMXHMWD<<EBDALRXHYM<<<<<<<<<<<<<<<<<<<<<\n"
                  "A2222222<0ASU7108215F04120411000146819<<<<44")

        self.assertEqual(str(td3_generator), result)


if __name__ == '__main__':
    unittest.main()
