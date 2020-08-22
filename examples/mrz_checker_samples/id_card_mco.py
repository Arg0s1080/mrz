#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.checker.td1 import TD1CodeChecker

mrz_td1 = ("I<MCO029067<<<0<<<<<<<<<<<<<<<\n"
           "9901018F0903248MCO<<<<<<<<<<<0\n"
           "SPECIMEN<<SPECIMEN<<<<<<<<<<<<")

td1_check = TD1CodeChecker(mrz_td1)

print("".ljust(35, "="))
print(td1_check.mrz_code)
print("\n")
print("Result:", bool(td1_check))
print("Falses:", td1_check.report.falses)
print("Warnings:", td1_check.report.warnings)
print("".ljust(35, "="))
print(td1_check.mrz_code)
print("\n")

td1_check = TD1CodeChecker(mrz_td1, check_expiry=True, compute_warnings=True)
print("Result:", bool(td1_check))
print("Falses:", td1_check.report.falses)
print("Warnings:", td1_check.report.warnings)
