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
# For more information on this, and how to apply and follow the GNU GPL, see:
# http://www.gnu.org/licenses
#
# Iván Rincón 2019

from ..base.countries_ops import *
from ..base.functions import hash_string, transliterate
from ._fields import _FieldsGenerator
from ._hash_fields import _HashGenerator
from ._holder_name import _HolderName

import mrz.base.string_checkers as check
import mrz.generator._transliterations as dictionary

__all__ = ["TD3CodeGenerator", "dictionary", "code_list", "countries_list", "countries_code_list",
           "code_country_list", "is_country", "is_code", "get_code", "get_country", "find_country"]


class _TD3HashGenerator(_HashGenerator):

    @property
    def optional_data(self) -> str:
        """Return optional data field (ID Number of the passport holder)

        Optional data at the discretion of the issuing State or organization. Non mandatory field.
        29 to 42 char position of the second line.

        """
        return self._optional_data

    @optional_data.setter
    def optional_data(self, value: str):
        """Set optional data field (ID Number of the passport holder)

        Optional data at the discretion of the issuing State or organization. Non mandatory field.
        29 to 42 char position of the second line.

        Case insensitive property

        """
        self._optional_data = check.field(transliterate(value, self.transliteration), 14, "optional data", "<")

    @property
    def optional_data_hash(self) -> str:
        """Return hash digit of the id_number field

        """
        return hash_string(self.optional_data)

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
                        self.optional_data +
                        self.optional_data_hash)

        return hash_string(final_string)


class _TD3HolderName(_HolderName):
    def __init__(self, surname: str, given_names: str, transliteration=dictionary.latin_based()):
        _HolderName.__init__(self, surname, given_names, transliteration)

    @property
    def identifier(self) -> str:
        """Return identifier (the primary and secondary identifiers)

        """
        return check.field(self.surname + "<<" + self.given_names, 39, "full name", "<")


class TD3CodeGenerator(_FieldsGenerator, _TD3HashGenerator, _TD3HolderName):
    """Calculate the string code of the machine readable zone for official travel documents of size 3 (passports)

    Params:
        document_type    (str):  Normally 'P' for passport
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Primary identifier(s)
        given_names      (str):  Secondary identifier(s)
        document_number  (str):  Document number
        nationality      (str):  3 letters code (ISO 3166-1) or country name
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined: 'X', "<" or ""
        expiry_date      (str):  YYMMDD
        optional data    (str):  Personal number. In some countries non-mandatory field. Empty string by default
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
                 document_number: str,
                 nationality: str,
                 birth_date: str,
                 sex: str,
                 expiry_date: str,
                 optional_data="",
                 transliteration=dictionary.latin_based(),
                 force=False):
        _TD3HolderName.__init__(self, surname, given_names, transliteration)
        self.force = force
        self.document_type = document_type
        self.country_code = country_code
        self.document_number = document_number
        self.nationality = nationality
        self.birth_date = birth_date
        self.sex = sex
        self.expiry_date = expiry_date
        self.optional_data = optional_data

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
                self.optional_data +
                self.optional_data_hash +
                self.final_hash)

    def __str__(self):
        return (self._line1() + "\n" +
                self._line2())
