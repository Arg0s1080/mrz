# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from mrz.checker.td1 import *
from mrz.base.functions import hash_is_ok


class TD1BELCodeChecker(TD1CodeChecker):

    @property
    def document_number_hash(self) -> bool:
        """Return True if the hash of the document number is validated, False otherwise."""
        if self._document_number_hash == "<":
            doc_number_fin = self._optional_data.rstrip("<")
            self._document_number = self._document_number + "<" + doc_number_fin[:-1]
            self._document_number_hash = doc_number_fin[-1]
        return self.report.add("document number hash", hash_is_ok(self._document_number, self._document_number_hash))
