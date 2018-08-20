#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.checker.td1 import TD1CodeChecker


def print_report(checker: TD1CodeChecker):
    print("REPORT")
    for r in checker.report:
        print(r[0] + ":" + str(r[1]).rjust(30 - len(r[0])))
    print("\nResult:" + str(td1_check).rjust(24).upper())


mrz_td1 = ("I<LVAPA99929216121282<88882<<<\n"
           "8212122M1703054LVA<<<<<<<<<<<0\n"
           "PARAUDZINS<<ANDRIS<<<<<<<<<<<<")


td1_check = TD1CodeChecker(mrz_td1, check_expiry=True)  # Check expiry date as warning
# Expiry Date = 170305
print_report(td1_check)  # TRUE    td1_check.report_warnings = ['document expired']


td1_check = TD1CodeChecker(mrz_td1, check_expiry=True, compute_warnings=True)  # Compute warnings as False
# Expiry Date = 170305
print_report(td1_check)  # FALSE

