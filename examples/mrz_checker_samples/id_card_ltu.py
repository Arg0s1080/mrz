#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td1 import TD1CodeGenerator
from mrz.checker.td1 import TD1CodeChecker
import examples.functions.functions as functions

mrz = str(TD1CodeGenerator("I", "LTU", "11810187", "641123", "F", "190101", "LTU", "BASANAVIČIENĖ", "BIRUTĖ",
                           "46411231034"))

td1_check = TD1CodeChecker(mrz)
print(td1_check)

td1_check = TD1CodeChecker(mrz, check_expiry=True, compute_warnings=True)

if not bool(td1_check):
    print("FALSE:")
    print(td1_check.report.falses)

functions.open_image("id_cards", "Lithuania.png")
