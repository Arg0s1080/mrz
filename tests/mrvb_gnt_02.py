import unittest
from mrz.generator.mrvb import MRVBCodeGenerator


class TestCase09(unittest.TestCase):

    def test_mrvb_generator(self):
        generator = MRVBCodeGenerator("V", "UTO", "ERIKSSON", "ANNA MARIA","L8988901C",
                                      "Unknown", "400907", "F", "961210")

        result = ("V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<\n"
                  "L8988901C4XXX4009078F9612109<<<<<<<<")

        self.assertEqual(str(generator), result)


if __name__ == '__main__':
    unittest.main()
