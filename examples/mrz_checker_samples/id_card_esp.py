#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Note for end users: #######################################################################
#
# Adding mrz (local) to PYTHONPATH to execute this example as a script without installing mrz
# (if it was installed using pip or setup.py the three lines below are not necessary)
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
##############################################################################################

from mrz.checker.td1 import TD1CodeChecker

print(TD1CodeChecker("IDESPBAA000589599999999R<<<<<<\n"
                     "8001014F2501017ESP<<<<<<<<<<<7\n"
                     "ESPANOLA<ESPANOLA<<CARMEN<<<<<"))

