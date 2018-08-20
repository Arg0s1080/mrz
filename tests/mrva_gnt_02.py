import unittest
from mrz.generator.mrva import MRVBCodeGenerator


class TestCase07(unittest.TestCase):

    def test_mrva_generator(self):
        generator = MRVBCodeGenerator("VI", "USA", "TRAVELER", "HAPPYPERSON", "555123ABC", "GBR",
                                      "650205", "F", "041223", "IFLND00AMS803085")

        result = ("VIUSATRAVELER<<HAPPYPERSON<<<<<<<<<<<<<<<<<<\n"
                  "555123ABC6GBR6502056F0412236IFLND00AMS803085")

        self.assertEqual(str(generator), result)


if __name__ == '__main__':
    unittest.main()
