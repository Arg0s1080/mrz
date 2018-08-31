#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Adding mrz path to PYTHONPATH to execute the example as script
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
##################################################################

from mrz.generator.td1 import TD1CodeGenerator
from mrz.checker.td1 import TD1CodeChecker
import examples.functions.functions as functions

mrz = str(TD1CodeGenerator("I", "LTU", "11810187", "201123", "F", "300101", "LTU", "BASANAVIČIENĖ", "BIRUTĖ",
                           "46411231034"))

td1_check = TD1CodeChecker(mrz)
print(td1_check)

td1_check = TD1CodeChecker(mrz, check_expiry=True)
if not bool(td1_check):
    print("FALSE:")
    print(td1_check.report_falses)

functions.open_image("id_cards", "Lithuania.png")
