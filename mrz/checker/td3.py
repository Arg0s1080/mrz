#!/usr/bin/python3
# -*- coding: UTF-8 -*-

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

from ..base.countries_ops import *
from ..base.functions import hash_is_ok, namedtuple_maker
from ..base.string_checkers import is_empty
from ._hash_fields import _HashChecker
from ._fields import _FieldsChecker

import mrz.base.string_checkers as check

__all__ = ["TD3CodeChecker", "code_list", "countries_list", "countries_code_list", "code_country_list",
           "is_country", "is_code", "get_code", "get_country", "find_country"]


class _TD3HashChecker(_HashChecker):
    def __init__(self, document_number, document_number_hash, birth_date, birth_date_hash, expiry_date,
                 expiry_date_hash, optional_data, optional_data_hash, final_hash):
        self._optional_data = optional_data
        self._optional_data_hash = optional_data_hash
        self._final_hash = final_hash
        _HashChecker.__init__(self, document_number, document_number_hash, birth_date, birth_date_hash,
                              expiry_date, expiry_date_hash)

    @property
    def optional_data_hash(self) -> bool:
        """Return True if hash of optional data is True, False otherwise."""

        ok = True if is_empty(self._optional_data) and self._optional_data_hash == "<" \
            else hash_is_ok(self._optional_data, self._optional_data_hash)
        return self.report.add("optional data hash", ok)

    @property
    def final_hash(self) -> bool:
        """Return True if final hash is True, False otherwise"""

        ok = hash_is_ok(self._document_number +
                        self._document_number_hash +
                        self._birth_date +
                        self._birth_date_hash +
                        self._expiry_date +
                        self._expiry_date_hash +
                        self._optional_data +
                        self._optional_data_hash, self._final_hash)
        return self.report.add("final hash", ok)

    def _all_hashes(self) -> bool:
        return (self.final_hash &
                self.document_number_hash &
                self.birth_date_hash &
                self.expiry_date_hash &
                self.optional_data_hash)

    def __repr__(self) -> str:
        return str(self._all_hashes())


class TD3CodeChecker(_TD3HashChecker, _FieldsChecker):
    """
    Check the string code of the machine readable zone for passports and other official travel documents of size 3

    __bool__() returns True if all fields are validated, False otherwise

    Params:
        mrz_string        (str):  MRZ string of TD3. Must be 88 characters long (uppercase)
        check_expiry     (bool):  If it's set to True, it is verified and reported as warning that the
                                  document is not expired and that expiry_date is not greater than 10 years.
        compute_warnings (bool):  If it's set True, warnings compute as False.

    """

    def __init__(self, mrz_code: str, check_expiry=False, compute_warnings=False):
        check.precheck("TD3", mrz_code, 89)
        lines = mrz_code.splitlines()
        self._document_type = lines[0][0: 2]
        self._country = lines[0][2: 5]
        self._identifier = lines[0][5: 44]
        self._document_number = lines[1][0: 9]
        self._document_number_hash = lines[1][9]
        self._nationality = lines[1][10: 13]
        self._birth_date = lines[1][13: 19]
        self._birth_date_hash = lines[1][19]
        self._sex = lines[1][20]
        self._expiry_date = lines[1][21: 27]
        self._expiry_date_hash = lines[1][27]
        self._optional_data = lines[1][28: 42]
        self._optional_data_hash = lines[1][42]
        self._final_hash = lines[1][43]
        _TD3HashChecker.__init__(self,
                                 self._document_number,
                                 self._document_number_hash,
                                 self._birth_date,
                                 self._birth_date_hash,
                                 self._expiry_date,
                                 self._expiry_date_hash,
                                 self._optional_data,
                                 self._optional_data_hash,
                                 self._final_hash)
        _FieldsChecker.__init__(self,
                                self._document_type,
                                self._country,
                                self._identifier,
                                self._document_number,
                                self._nationality,
                                self._birth_date,
                                self._sex,
                                self._expiry_date,
                                self._optional_data,
                                "",
                                check_expiry,
                                compute_warnings,
                                mrz_code)
        self.result = self._all_hashes() & self._all_fields()

    def fields(self, zero_fill=False):
        """Returns a namedtuple with all fields strings

        Available strings for Passports and other TD3's:
        surname, name, country, nationality, birth_date, expiry_date, sex, document_type,
        document_number, optional_data, birth_date_hash, expiry_date_hash, document_number_hash,
        optional_data_hash and final_hash

        Params:
            zero_fill  (bool): Replace '<' char by '0' in alphanum fields (document_number and
                               optional_data)

        """
        extra_fields = self._optional_data_hash, self._final_hash
        extra_names = "optional_data_hash final_hash"
        return namedtuple_maker(self._str_common_fields(zero_fill), self._str_common_hashes(),
                                extra_fields, extra_names)

    def __repr__(self):
        return str(self.result)

    def __bool__(self):
        return self.result
