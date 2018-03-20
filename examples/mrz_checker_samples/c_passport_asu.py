#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from checker.td3 import *
from base.countries_ops import is_code
mrz_td3 = ("P<ASUMXHMWD<<EBDALRXHYM<<<<<<<<<<<<<<<<<<<<<\n"
           "A2222222<0ASU7108215F04120411000146819<<<<44")

td1_check = TD3CodeChecker(mrz_td3, check_expiry=True)

if not td1_check:
    print("Falses:", td1_check.report_falses)
    print("Warnings:", td1_check.report_warnings)

print(is_code("ASU"))
