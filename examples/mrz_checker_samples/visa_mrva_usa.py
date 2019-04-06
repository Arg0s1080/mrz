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

mrz_code = ("VNUSATRAVELER<<HAPPY<<<<<<<<<<<<<<<<<<<<<<<<\n"
            "1234567897CAN6612120M1407282B3XLC000FD142955")

checker = MRVACodeChecker(mrz_code)

print(checker.result)



def print_txt(title, value):
    print(title.ljust(20), value)


fields = checker.fields()

print_txt("Document Type:", fields.document_type)
print_txt("Country:", fields.country)
print_txt("Surname:", fields.surname)
print_txt("Name:", fields.name)
print_txt("Doc. Number", fields.document_number)
print_txt("Doc. Number Hash:", fields.document_number_hash)
print_txt("Nationality:", fields.nationality)
print_txt("Birth Date:", fields.birth_date)
print_txt("Birth Date Hash:", fields.birth_date_hash)
print_txt("Sex:", fields.sex)
print_txt("Expiry Date:", fields.expiry_date)
print_txt("Expiry Date Hash:", fields.expiry_date_hash)
print_txt("Optional data:", fields.optional_data)
print_txt("Final Hash:", fields.final_hash)
