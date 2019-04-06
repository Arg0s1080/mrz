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


def print_txt(title, value):
    print(title.ljust(20), value)


fields = td3_check.fields()

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
print_txt("Optional data hash:", fields.optional_data_hash)
print_txt("Final Hash:", fields.final_hash)
