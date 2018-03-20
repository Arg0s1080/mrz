#!/usr/bin/python3
# -*- coding UTF-8 -*-
import sys
sys.path.append(sys.path[0].replace("examples/mrz_checker_samples", ""))
from checker.td1 import *

mrz_td1 = ("IDLIEID98754015<<<<<<<<<<<<<<<\n" 
           "8205122M1906224LIE<<<<<<<<<<<6\n" 
           "OSPELT<BECK<<MARISA<<<<<<<<<<<")

td1_check = TD1CodeChecker(mrz_td1)

if bool(td1_check) == False:
    print(td1_check.report_falses)
