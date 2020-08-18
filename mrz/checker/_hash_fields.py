# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from ..base.functions import hash_is_ok
from ._report import _Report


class _HashChecker:
    def __init__(self, document_number: str, document_number_hash: str, birth_date: str, birth_date_hash: str,
                 expiry_date: str, expiry_date_hash: str):
        self._document_number = document_number
        self._document_number_hash = document_number_hash
        self._birth_date = birth_date
        self._birth_date_hash = birth_date_hash
        self._expiry_date = expiry_date
        self._expiry_date_hash = expiry_date_hash
        self.report = _Report()

    @property
    def document_number_hash(self) -> bool:
        """Return True if the hash of the document number is validated, False otherwise."""

        return self.report.add("document number hash",
                               hash_is_ok(self._document_number, self._document_number_hash))

    @property
    def birth_date_hash(self) -> bool:
        """Return True if the hash of the birth date is validated, False otherwise."""

        return self.report.add("birth date hash", hash_is_ok(self._birth_date, self._birth_date_hash))

    @property
    def expiry_date_hash(self) -> bool:
        """Return True if the hash of the expiry date is validated, False otherwise."""

        return self.report.add("expiry date hash", hash_is_ok(self._expiry_date, self._expiry_date_hash))

    def _all_hashes(self):
        return (self.document_number_hash &
                self.birth_date_hash &
                self.expiry_date_hash)

    def _str_common_hashes(self):
        return ((self._birth_date_hash, self._expiry_date_hash, self._document_number_hash),
                "birth_date_hash expiry_date_hash document_number_hash ")

    def __repr__(self):
        return self._all_hashes()
