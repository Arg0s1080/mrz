import unittest

from tests.td1_chk_01 import TestCase06
from tests.td1_chk_02 import TestCase07
from tests.td1_chk_03 import TestCase15
from tests.td2_chk_01 import TestCase08
from tests.td2_chk_02 import TestCase16
from tests.td3_chk_01 import TestCase09
from tests.td3_chk_02 import TestCase10
from tests.td3_chk_03 import TestCase17
from tests.td3_chk_04 import TestCase20
from tests.mrva_chk_01 import TestCase11
from tests.mrva_chk_02 import TestCase12
from tests.mrva_chk_03 import TestCase18
from tests.mrvb_chk_01 import TestCase13
from tests.mrvb_chk_02 import TestCase14
from tests.mrvb_chk_03 import TestCase19


class TestCaseChkAll(unittest.TestCase):
    def test_checker(self):
        TestCase06().test_td1_checker()
        TestCase07().test_td1_checker()
        TestCase15().test_td1_checker()
        TestCase08().test_td2_checker()
        TestCase16().test_td2_checker()
        TestCase09().test_a_td3_checker()
        TestCase09().test_b_td3_checker()
        TestCase09().test_c_td3_checker()
        TestCase10().test_td3_checker()
        TestCase17().test_td3_checker()
        TestCase20().test_a_td3_checker()
        TestCase20().test_b_td3_checker()
        TestCase11().test_mrva_checker()
        TestCase12().test_mrva_checker()
        TestCase18().test_mrva_checker()
        TestCase13().test_mrvb_checker()
        TestCase14().test_mrvb_checker()
        TestCase19().test_mrvb_checker()


if __name__ == '__main__':
    unittest.main()
