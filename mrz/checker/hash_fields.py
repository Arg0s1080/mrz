# GNU General Public License v3.0

import mrz.base.functions as functions
from mrz.checker.report import Report


class HashChecker(Report):
    def __init__(self, document_number: str, document_number_hash: str, birth_date: str, birth_date_hash: str,
                 expiry_date: str, expiry_date_hash: str):
        self._document_number = document_number
        self._document_number_hash = document_number_hash
        self._birth_date = birth_date
        self._birth_date_hash = birth_date_hash
        self._expiry_date = expiry_date
        self._expiry_date_hash = expiry_date_hash

    @property
    def document_number_hash(self) -> bool:
        """Return True if the hash of the document number is validated, False otherwise."""

        return self._report("document number hash",
                            functions.hash_is_ok(self._document_number, self._document_number_hash))

    @property
    def birth_date_hash(self) -> bool:
        """Return True if the hash of the birth date is validated, False otherwise."""

        return self._report("birth date hash", functions.hash_is_ok(self._birth_date, self._birth_date_hash))

    @property
    def expiry_date_hash(self) -> bool:
        """Return True if the hash of the expiry date is validated, False otherwise."""

        return self._report("expiry date hash", functions.hash_is_ok(self._expiry_date, self._expiry_date_hash))
