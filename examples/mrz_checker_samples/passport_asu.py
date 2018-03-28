#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.base.countries_ops import is_code
from mrz.checker.td3 import TD3CodeChecker

mrz_td3 = ("P<ASUMXHMWD<<EBDALRXHYM<<<<<<<<<<<<<<<<<<<<<\n"
           "A2222222<0ASU7108215F04120411000146819<<<<44")

td3_check = TD3CodeChecker(mrz_td3, check_expiry=True)

print(td3_check.mrz_code)

if not td3_check:
    print("Falses:", td3_check.report_falses)
    print("Warnings:", td3_check.report_warnings)

print("'%s' is code: %s" % (td3_check._country, str(is_code("ASU"))))
