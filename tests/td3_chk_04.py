import unittest
from mrz.checker.td3 import TD3CodeChecker


class TestCase20(unittest.TestCase):
    # optional_data_hash TD3
    # if optional data is empty "0" and "<" will return True
    # See #21

    def test_td3_checker(self):
        # optional data hash == '0'
        mrz1 = ("P<CANMARTIN<<SARAH<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
                "ZE000509<9CAN8501019F2301147<<<<<<<<<<<<<<08")
        test1 = bool(TD3CodeChecker(mrz1))

        # optional data hash == '<'
        mrz2 = ("P<CANMARTIN<<SARAH<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
                "ZE000509<9CAN8501019F2301147<<<<<<<<<<<<<<08")
        test2 = bool(TD3CodeChecker(mrz2))

        self.assertEqual(test1, test2)


if __name__ == '__main__':
    unittest.main()
