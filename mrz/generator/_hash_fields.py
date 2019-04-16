# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from ..base.functions import hash_string
from ..base.string_checkers import field, date


class _HashGenerator:
    def __init__(self, document_number: str, birth_date: str, expiry_date: str, transliteration: dict):
        self.document_number = document_number
        self.birth_date = birth_date
        self.expiry_date = expiry_date
        self.transliteration = transliteration  # included to transliterate optional fields

    @property
    def document_number(self) -> str:
        """Return document number string

        Document number given by the issuing State or organization, to uniquely identify the document
        from all other MRTDs

        """
        return self._document_number

    @document_number.setter
    def document_number(self, value: str):
        """Set document number

        Document number given by the issuing State or organization, to uniquely identify the document
        from all other MRTDs

        Case insensitive.

        """
        self._document_number = field(value, 9, "document number")

    @property
    def document_number_hash(self) -> str:
        """Return hash digit of document number

        """
        return hash_string(self.document_number)

    @property
    def birth_date(self) -> str:
        """Return birth date of holder

        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: str):
        """Set holder's date of birth with 'YYMMDD' format

        """
        self._birth_date = date(value)

    @property
    def birth_date_hash(self) -> str:
        """Return hash digit of birth date

        """
        return hash_string(self.birth_date)

    @property
    def expiry_date(self) -> str:
        """Return date of expiry of the document

        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value: str):
        """Set date of expiry of the MRTD with 'YYMMDD' format

        """
        self._expiry_date = date(value)

    @property
    def expiry_date_hash(self) -> str:
        """Return hash digit of expiry date

        """
        return hash_string(self.expiry_date)
