import unittest
from mrz.generator.mrvb import MRVBCodeGenerator


class TestCase08(unittest.TestCase):

    def test_mrvb_generator(self):
        generator = MRVBCodeGenerator("VB", "D", "DEDIC", "SIDNAN", "D09174053", "BOS",
                                      "820113", "M", "970801", " 2020711", force=True)

        result = ("VBD<<DEDIC<<SIDNAN<<<<<<<<<<<<<<<<<<\n"
                  "D091740530BOS8201135M9708011<2020711")

        self.assertEqual(str(generator), result)


if __name__ == '__main__':
    unittest.main()
