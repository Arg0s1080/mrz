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
from ..base.functions import namedtuple_maker
from .td2 import TD2CodeChecker

import mrz.base.string_checkers as check


__all__ = ["MRVBCodeChecker", "code_list", "countries_list", "countries_code_list", "code_country_list",
           "is_country", "is_code", "get_code", "get_country", "find_country"]


class MRVBCodeChecker(TD2CodeChecker):
    """
    Check the string code of the machine readable visas type B (MRVB)

    __bool__() returns True if all fields are validated, False otherwise

    Params:
        mrz_string        (str):  MRZ string of MRVB. Must be 88 characters long (uppercase)
        check_expiry     (bool):  If it's set to True, it is verified and reported as warning that the
                                  document is not expired and that expiry_date is not greater than 10 years
        compute_warnings (bool):  If it's set True, warnings compute as False

    """
    def __init__(self, mrz_code: str, check_expiry=False, compute_warnings=False):
        TD2CodeChecker.__init__(self, mrz_code, check_expiry, compute_warnings)

    @property
    def optional_data(self) -> bool:
        """Return True if the format of the optional data field is validated, False otherwise."""

        s = self._optional_data = self.mrz_code.splitlines()[1][28: 36]
        return True if check.is_empty(s) else self.report.add("optional data format", check.is_printable(s))

    def fields(self, zero_fill=False):
        """Returns a namedtuple with all fields strings

        Available strings for Visas B:
        surname, name, country, nationality, birth_date, expiry_date, sex, document_type,
        document_number, optional_data, birth_date_hash, expiry_date_hash and document_number_hash

        Params:
            zero_fill  (bool): Replace '<' char by '0' in alphanum fields (document_number and
                               optional_data)

        """
        return namedtuple_maker(self._str_common_fields(zero_fill), self._str_common_hashes())

    def _all_hashes(self) -> bool:
        return (self.document_number_hash &
                self.birth_date_hash &
                self.expiry_date_hash)

