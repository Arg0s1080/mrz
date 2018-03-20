#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from checker.td1 import TD1CodeChecker

mrz_td1 = ("I<LVAPA99929216121282<88882<<<\n"
           "8212122M1703054LVA<<<<<<<<<<<0\n"
           "PARAUDZINS<<ANDRIS<<<<<<<<<<<<")

td1_check = TD1CodeChecker(mrz_td1, check_expiry=True)

print(td1_check._all_fields)
