from mrz.checker.mrvb import MRVBCodeChecker

mrz_code = ("VDGBRMUNIR<<FAISAL<<<<<<<<<<<<<<<<<<\n"
            "AD07259817PAK7608151M0611165<<<<<<<<")

mrvb_check = MRVBCodeChecker(mrz_code)


def print_txt(title, value):
    print(title.ljust(20), value)


fields = mrvb_check.fields()

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
