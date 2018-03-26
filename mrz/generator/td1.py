#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned on making available
# complete source code of licensed works and modifications, which include larger works
# using a licensed work, under the same license. Copyright and license notices must be
# preserved. Contributors provide an express grant of patent rights.
#
# For more information on this, and how to apply and follow theGNU GPL, see:
# http://www.gnu.org/licenses
#
# Iván Rincón 2018

from mrz.generator.fields import Fields
from mrz.generator.hash_fields import HashGenerator
from mrz.generator.holder_name import HolderName

from mrz.base.countries_ops import *

import mrz.base.functions as functions
import mrz.generator.transliterations as dictionary
import mrz.base.string_checkers as check

__all__ = ["TD1CodeGenerator", "dictionary", "code_list", "countries_list", "countries_code_list",
           "code_country_list", "is_country", "is_code", "get_code", "get_country", "find_country"]


class _TD1HashGenerator(HashGenerator):
    @property
    def optional_data1(self) -> str:
        """Return optional data field of the first line (16 to 30 char position) for TD1

        Optional data at the discretion of the issuing State or organization. Non mandatory field

        """
        return self._optional_data1

    @optional_data1.setter
    def optional_data1(self, value: str):
        """Set optional data field of the first line (16 to 30 char position) for TD1

        Optional data at the discretion of the issuing State or organization. Non mandatory field

        Case insensitive

        """
        self._optional_data1 = check.field(functions.transliterate(value, self.transliteration),
                                           15, "optional data 1", "<")

    @property
    def optional_data2(self) -> str:
        """Return optional data field of the second line (19 to 29 char position) for TD1

        Optional data at the discretion of the issuing State or organization. Non mandatory field

        """
        return self._optional_data2

    @optional_data2.setter
    def optional_data2(self, value: str):
        """Set optional data field of the second line (19 to 29 char position) for TD1

        Optional data at the discretion of the issuing State or organization. Non mandatory field

        Case insensitive.

        """
        self._optional_data2 = check.field(functions.transliterate(value, self.transliteration),
                                           11, "optional data 2", "<")

    @property
    def final_hash(self) -> str:
        """Return final hash digit for TD1

        """
        return functions.hash_string(self.document_number +
                                     self.document_number_hash +
                                     self.optional_data1 +
                                     self.birth_date +
                                     self.birth_date_hash +
                                     self.expiry_date +
                                     self.expiry_date_hash +
                                     self.optional_data2)


class _TD1HolderName(HolderName):
    def __init__(self, surname: str, given_names: str, transliteration: dict):
        HolderName.__init__(self, surname, given_names, transliteration)

    @property
    def identifier(self) -> str:
        """Return identifier (sum of the primary and secondary identifier)

        """
        return check.field(self.surname + "<<" + self.given_names, 30, "full name", "<")


class TD1CodeGenerator(_TD1HolderName, _TD1HashGenerator, Fields):
    """Calculate the string code of the machine readable zone for official travel documents of size 1

    Params:
        document_type    (str):  The first letter shall be 'I', 'A' or 'C'
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        document_number  (str):  Document number
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined 'X'
        expiry_date      (str):  YYMMDD
        nationality      (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Holder primary identifier(s)
        given_names      (str):  Holder secondary identifier(s)
        optional_data1   (str):  Optional personal data at the discretion of the issuing State.
                                 Non-mandatory field. Empty string by default
        optional_data2   (str):  Optional personal data at the discretion of the issuing State.
                                 Non-mandatory field. Empty string by default
        transliteration (dict):  Transliteration dictionary for non-ascii chars. Latin based by default
        force           (bool):  Disables checks for country, nationality and document_type fields.
                                 Allows to use 3-letter-codes not included in the countries dictionary
                                 and to use document_type codes without restrictions.

    """
    def __init__(self,
                 document_type: str,
                 country_code: str,
                 document_number: str,
                 birth_date: str,
                 sex: str,
                 expiry_date: str,
                 nationality: str,
                 surname: str,
                 given_names: str,
                 optional_data1="",
                 optional_data2="",
                 transliteration=dictionary.latin_based(),
                 force=False):
        _TD1HolderName.__init__(self, surname, given_names, transliteration)
        self.force = force
        self.document_type = document_type
        self.country_code = country_code
        self.document_number = document_number
        self.optional_data1 = optional_data1
        self.birth_date = birth_date
        self.sex = sex
        self.expiry_date = expiry_date
        self.nationality = nationality
        self.optional_data2 = optional_data2
        self.transliteration = transliteration

    def _line1(self):
        return(self.document_type +
               self.country_code +
               self.document_number +
               self.document_number_hash +
               self.optional_data1)

    def _line2(self):
        return(self.birth_date +
               self.birth_date_hash +
               self.sex +
               self.expiry_date +
               self.expiry_date_hash +
               self.nationality +
               self.optional_data2 +
               self.final_hash)

    def __str__(self):
        return(self._line1() + "\n" +
               self._line2() + "\n" +
               self.identifier)
