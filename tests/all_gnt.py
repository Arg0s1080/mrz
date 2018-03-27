import unittest

from tests.td1_gnt_01 import TestCase01
from tests.td1_gnt_02 import TestCase02
from tests.td2_gnt_01 import TestCase03
from tests.td3_gnt_01 import TestCase04
from tests.td3_gnt_02 import TestCase05


class TestCaseGntAll(unittest.TestCase):
    def test_generator(self):
        TestCase01().test_td1_generator()
        TestCase02().test_td1_generator()
        TestCase03().test_td2_generator()
        TestCase04().test_td3_generator()
        TestCase05().test_td3_generator()


if __name__ == '__main__':
    unittest.main()
