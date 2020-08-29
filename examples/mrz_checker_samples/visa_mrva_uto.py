#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Note for end users: #######################################################################
#
# Adding mrz (local) to PYTHONPATH to execute this example as a script without installing mrz
# (if it was installed using pip or setup.py the three lines below are not necessary)
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
##############################################################################################

from mrz.checker.mrva import MRVACodeChecker
from examples.functions.functions import open_image


mrva_code = ("V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\n"
             "L8988901C4XXX4009078F96121096ZE184226B<<<<<<")

checker = MRVACodeChecker(mrva_code, check_expiry=True)  # Check expiry date as warning

print("Expiry date : %s" % checker.expiry_date)                # True              (It's a real date)
print("Warning ....: %s" % "".join(checker.report.warnings))   # document expired
print("VISA .......: %s" % str(checker).upper())               # TRUE

checker = MRVACodeChecker(mrva_code, check_expiry=True, compute_warnings=True)  # Compute Warnings as False
print()
print("Expiry date : %s" % checker.expiry_date)                # False
print("Warning ....: %s" % ", ".join(checker.report.warnings))   # document expired
print("VISA .......: %s" % str(checker).upper())               # FALSE

print()
open_image("visas", "MRVA_ICAO_Example.png")
