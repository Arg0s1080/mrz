import unittest
from mrz.generator.mrva import MRVBCodeGenerator


class TestCase06(unittest.TestCase):

    def test_mrva_generator(self):
        generator = MRVBCodeGenerator("V", "Utopia", "ÊrÌkS'ŝóN", "ÂNNa mARíA", "L8988901c", "Unknown",
                                      "400907", "f", "961210",  "Ze184226b")

        result = ("V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\n"
                  "L8988901C4XXX4009078F9612109ZE184226B<<<<<<<")

        self.assertEqual(str(generator), result)


if __name__ == '__main__':
    unittest.main()
