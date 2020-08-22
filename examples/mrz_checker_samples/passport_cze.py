#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.checker.td3 import TD3CodeChecker


td3_check = TD3CodeChecker("P<CZESPECIMEN<<VZOR<<<<<<<<<<<<<<<<<<<<<<<<<\n"
                           "99003853<1CZE1101018M1207046110101111<<<<<94",
                           check_expiry=True)

print(bool(td3_check))
print(td3_check.report.warnings)
