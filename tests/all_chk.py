import unittest

from tests.td1_chk_01 import TestCase06
from tests.td1_chk_02 import TestCase07
from tests.td2_chk_01 import TestCase08
from tests.td3_chk_01 import TestCase09
from tests.td3_chk_02 import TestCase10


class TestCaseChkAll(unittest.TestCase):
    def test_checker(self):
        TestCase06().test_td1_checker()
        TestCase07().test_td1_checker()
        TestCase08().test_td2_checker()
        TestCase09().test_a_td3_checker()
        TestCase09().test_b_td3_checker()
        TestCase09().test_c_td3_checker()
        TestCase10().test_td3_checker()


if __name__ == '__main__':
    unittest.main()

