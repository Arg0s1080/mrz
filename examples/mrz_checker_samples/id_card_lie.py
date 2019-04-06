#!/usr/bin/python3
# -*- coding UTF-8 -*-

from mrz.checker.td1 import TD1CodeChecker

mrz_td1 = ("IDLIEID98754015<<<<<<<<<<<<<<<\n" 
           "8205122M1906224LIE<<<<<<<<<<<6\n" 
           "OSPELT<BECK<<MARISA<<<<<<<<<<<")

td1_check = TD1CodeChecker(mrz_td1)

if bool(td1_check) == False:
    print(td1_check.report_falses)

fields = td1_check.fields()


def print_txt(title, value):
    print(title.ljust(20), value)


print_txt("Document Type:", fields.document_type)
print_txt("Country:", fields.country)
print_txt("Doc. Number", fields.document_number)
print_txt("Doc. Number Hash:", fields.document_number_hash)
print_txt("Optional data:", fields.optional_data)
print_txt("Birth Date:", fields.birth_date)
print_txt("Birth Date Hash:", fields.birth_date_hash)
print_txt("Sex:", fields.sex)
print_txt("Expiry Date:", fields.expiry_date)
print_txt("Expiry Date Hash:", fields.expiry_date_hash)
print_txt("Nationality:", fields.nationality)
print_txt("Optional data 2:", fields.optional_data_2)
print_txt("Final Hash:", fields.final_hash)
print_txt("Surname:", fields.surname)
print_txt("Name:", fields.name)
