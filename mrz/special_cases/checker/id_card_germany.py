# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from mrz.base.functions import hash_is_ok
from mrz.checker.td1 import *

import mrz.base.string_checkers as check


class TD1DutchCodeChecker(TD1CodeChecker):

    @property
    def optional_data_hash(self):
        self._optional_data_hash = self.mrz_code.splitlines()[0][29]
        self._optional_data = self.mrz_code.splitlines()[0][15: 29]
        return self.report.add("id number hash", hash_is_ok(self._optional_data, self._optional_data_hash))

    @property
    def optional_data(self) -> bool:
        """Return True if the format of the optional data field is validated, False otherwise."""
        s = self._optional_data
        return True if check.is_empty(s) else self.report.add("id number format", check.is_printable(s))

    def _all_hashes(self) -> bool:
        return (self.final_hash &
                self.document_number_hash &
                self.birth_date_hash &
                self.expiry_date_hash &
                self.optional_data_hash)

