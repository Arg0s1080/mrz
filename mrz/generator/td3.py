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
import mrz.base.string_checkers as check
import mrz.generator.transliterations as dictionary

__all__ = ["PassportCodeGenerator", "dictionary", "code_list", "countries_list", "countries_code_list",
           "code_country_list", "is_country", "is_code", "get_code", "get_country", "find_country"]


class _PassportHashGenerator(HashGenerator):

    @property
    def id_number(self) -> str:
        """Return ID Number of the passport holder

        Optional data at the discretion of the issuing State or organization. Non mandatory field

        """
        return self._id_number

    @id_number.setter
    def id_number(self, value: str):
        """Return ID Number of the passport holder

        Optional data at the discretion of the issuing State or organization. Non mandatory field

        Case insensitive property

        """
        self._id_number = check.field(functions.transliterate(value, self.transliteration), 14, "id number", "<")

    @property
    def id_number_hash(self) -> str:
        """Return hash digit of the id_number field

        """
        return functions.hash_string(self.id_number)

    @property
    def final_hash(self) -> str:
        """Return final hash digit of the passport or other TD3

        """
        final_string = (self.document_number +
                        self.document_number_hash +
                        self.birth_date +
                        self.birth_date_hash +
                        self.expiry_date +
                        self.expiry_date_hash +
                        self.id_number +
                        self.id_number_hash)

        return functions.hash_string(final_string)


class _PassportHolderName(HolderName):
    def __init__(self, surname: str, given_names: str, transliteration=dictionary.latin_based()):
        HolderName.__init__(self, surname, given_names, transliteration)

    @property
    def identifier(self) -> str:
        """Return identifier (the primary and secondary identifiers)

        """
        return check.field(self.surname + "<<" + self.given_names, 39, "full name", "<")


class PassportCodeGenerator(Fields, _PassportHashGenerator, _PassportHolderName):
    """Calculate the string code of the machine readable zone for official travel documents of size 3 (passports)

    Params:
        document_type    (str):  Normally 'P' for passport
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Primary identifier(s)
        given_names      (str):  Secondary identifier(s)
        passport_number  (str):  Passport number
        nationality      (str):  3 letters code (ISO 3166-1) or country name
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined 'X'
        expiry_date      (str):  YYMMDD
        id_number        (str):  Personal number. In some countries non-mandatory field. Empty string by default
        transliteration (dict):  Transliteration dictionary for non-ascii chars. Latin based by default
        force           (bool):  Disables checks for country, nationality and document_type fields.
                                 Allows to use 3-letter-codes not included in the countries dictionary
                                 and to use document_type codes without restrictions.

    """
    def __init__(self,
                 document_type: str,
                 country_code: str,
                 surname: str,
                 given_names: str,
                 passport_number: str,
                 nationality: str,
                 birth_date: str,
                 sex: str,
                 expiry_date: str,
                 id_number="",
                 transliteration=dictionary.latin_based(),
                 force=False):
        _PassportHolderName.__init__(self, surname, given_names, transliteration)
        self.force = force
        self.document_type = document_type
        self.country_code = country_code
        self.document_number = passport_number
        self.nationality = nationality
        self.birth_date = birth_date
        self.sex = sex
        self.expiry_date = expiry_date
        self.id_number = id_number

    @property
    def document_type(self) -> str:
        """Return document type code of the passport

        """
        return self._document_type

    @document_type.setter
    def document_type(self, value: str):
        """Set document type code of the passport

        Can be used 'P' for passports and other TD3. Optionally, can be used a second character.
        The second character shall be at discretion of issuing state.

        Case insensitive.

        """
        self._document_type = check.document_type(value, True)

    def _line1(self):
        return (self.document_type +
                self.country_code +
                self.identifier)

    def _line2(self):
        return (self.document_number +
                self.document_number_hash +
                self.nationality +
                self.birth_date +
                self.birth_date_hash +
                self.sex +
                self.expiry_date +
                self.expiry_date_hash +
                self.id_number +
                self.id_number_hash +
                self.final_hash)

    def __str__(self):
        return (self._line1() + "\n" +
                self._line2())
