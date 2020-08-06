import unittest
from mrz.checker.td3 import TD3CodeChecker


class TestCase20(unittest.TestCase):
    # optional_data_hash TD3
    # if optional data is empty "0" and "<" will return True
    # See #21

    def test_a_td3_checker(self):
        mrz_td3 = ("P<CANMARTIN<<SARAH<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
                   "ZE000509<9CAN8501019F2301147<<<<<<<<<<<<<<08")
        self.assertTrue(bool(TD3CodeChecker(mrz_td3)))

    def test_b_td3_checker(self):
        mrz_td3 = ("P<CANMARTIN<<SARAH<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
                   "ZE000509<9CAN8501019F2301147<<<<<<<<<<<<<<<8")
        self.assertTrue(bool(TD3CodeChecker(mrz_td3)))


if __name__ == '__main__':
    unittest.main()
