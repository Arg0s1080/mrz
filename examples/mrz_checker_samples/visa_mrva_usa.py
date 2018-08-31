#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Adding mrz to PYTHONPATH to execute this example as script
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
#############################################################

from mrz.checker.mrva import MRVACodeChecker

mrz_code = ("VNUSATRAVELER<<HAPPY<<<<<<<<<<<<<<<<<<<<<<<<\n"
            "1234567897CAN6612120M1407282B3XLC000FD142955")

checker = MRVACodeChecker(mrz_code)

print(checker.result)
