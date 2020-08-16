# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

import mrz.base.string_checkers as check


class _FieldsGenerator:
    def __init__(self, document_type: str, country_code: str, document_number: str,
                 nationality: str, sex: str, force: bool):
        self.force = force
        self.document_type = document_type
        self.country_code = country_code
        self.document_number = document_number
        self.nationality = nationality
        self.sex = sex

    @property
    def document_type(self) -> str:
        """Return document type code

        """
        return self._document_type

    @document_type.setter
    def document_type(self, value: str):
        """Set document type code

        For TD1 and TD2, the first letter must be 'I', 'A' or 'C'. Optionally, can be used a
        second character. The second character shall be at discretion of issuing state.
        Note: 'V' shall not be used as 2nd char and 'C' shall not be used after 'A'. (TD1 and TD2)

        First letter of passports and other TD3 must be 'P'. Optionally, can be used a second
        character. The second character shall be at discretion of issuing state

        For visas (MRV-A and MRV-B), the first letter must be 'V'. Optionally, can be used a
        second character. The second character shall be at discretion of issuing state

        Case insensitive.

        """
        self._document_type = check.document_type(value, self) if not self.force \
            else check.field(value, 2, "document type")

    @property
    def country_code(self) -> str:
        """Return 3-letter-code of issuing State

        Representation of issuing State or organization and nationality of holder specified in ISO 3166-1

        """
        return self._country_code

    @country_code.setter
    def country_code(self, value: str):
        """Set issuing state

        Can be used the 3-letter code (ISO 3166-1) or the country name called in English (For example,
        'NLD' or 'Netherlands')

        Case insensitive.

        """
        self._country_code = check.country(value) if not self.force else check.field(value, 3, "country code")

    @property
    def nationality(self) -> str:
        """Return 3-letter-code of nationality

        Representation of 3-letter code (ISO 3166-1) of holder's nationality

        """
        return self._nationality

    @nationality.setter
    def nationality(self, value: str):
        """Set holder's nationality

        Can be used the 3-letter code (ISO 3166-1) or the country name called in English (For example,
        'NLD' or 'Netherlands')

        Case insensitive

        """
        self._nationality = check.country(value) if not self.force else check.field(value, 3, "document type")

    @property
    def sex(self) -> str:
        """Return holder's genre

        """
        return self._sex

    @sex.setter
    def sex(self, value: str):
        """Set holder's genre

        Can be used 'F' (female), 'M' (male) or undefined. Case insensitive.

        """
        value = value if value not in "Xx" else "<"
        self._sex = check.sex(value)

