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
# (ɔ) Iván Rincón 2019

from ..base.functions import transliterate
from .td3 import TD3CodeGenerator

import mrz.base.string_checkers as check
import mrz.generator._transliterations as dictionary


class MRVACodeGenerator(TD3CodeGenerator):
    """Calculate the string code for machine readable zone visas of type A (MRVA)

    Params:
        document_type    (str):  The First letter must be 'V'
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Primary identifier(s)
        given_names      (str):  Secondary identifier(s)
        document_number  (str):  Document number
        nationality      (str):  3 letters code (ISO 3166-1) or country name
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined: 'X', "<" or ""
        expiry_date      (str):  YYMMDD
        optional_data    (str):  Optional personal data at the discretion of the issuing State.
                                 Non-mandatory field. Empty string by default.
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
        TD3CodeGenerator.__init__(self, document_type, country_code, surname, given_names, document_number,
                                  nationality, birth_date, sex, expiry_date, optional_data, transliteration,
                                  force)
        self.optional_data = optional_data

    @property
    def optional_data(self) -> str:
        """Return optional data field for Visas of type A (MRVA)

        Optional data at the discretion of the issuing State or organization. Non mandatory field.
        29 to 44 char position of the second line.

        """
        return self._optional_data

    @optional_data.setter
    def optional_data(self, value: str):
        """Set optional data field for Visas of type A (MRVA)

        Optional data at the discretion of the issuing State or organization. Non mandatory field
        29 to 44 char position of the second line.

        Case insensitive property

        """
        self._optional_data = check.field(transliterate(value, self.transliteration), 16, "optional data", "<")

    @property
    def final_hash(self) -> None:
        # override property (TD3)
        return None

    @property
    def optional_data_hash(self) -> None:
        # override property (TD3)
        return None

    def _line2(self):
        return (self.document_number +
                self.document_number_hash +
                self.nationality +
                self.birth_date +
                self.birth_date_hash +
                self.sex +
                self.expiry_date +
                self.expiry_date_hash +
                self.optional_data)
