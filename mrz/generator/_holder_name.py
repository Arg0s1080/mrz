# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from ..base.functions import transliterate


class _HolderName:
    def __init__(self, surname: str, given_names: str, transliteration: dict):
        self.transliteration = transliteration
        self.surname = surname
        self.given_names = given_names

    @property
    def transliteration(self) -> dict:
        """Return the transliteration dictionary used for non-ascii characters

        """
        return self._transliteration

    @transliteration.setter
    def transliteration(self, value: dict):
        """Set the transliteration dictionary used for non-ascii characters

        National characters may be used in the visual inspection zone for identifiers. If the national
        characters are not ASCII, a transliteration into Latin ASCII chars is provided by the
        transliteration methods included in transliteration.py or another transliteration dict.


        """
        self._transliteration = value

    @property
    def surname(self) -> str:
        """Return the primary identifier, usually the holder's surname.

        The issuing State or organization shall establish which part of the name is the primary identifier.
        This may be the family name, the maiden name or the married name, the main name, the surname, and
        in some cases, the entire name where the holder’s name cannot be divided into two parts.


        """
        return self._surnames

    @surname.setter
    def surname(self, value: str):
        """Set the primary identifier, usually the holder's surname

        The issuing State or organization shall establish which part of the name is the primary identifier.
        This may be the family name, the maiden name or the married name, the main name, the surname, and
        in some cases, the entire name where the holder’s name cannot be divided into two parts.

        Case insensitive.

        """
        self._surnames = transliterate(value, self.transliteration)

    @property
    def given_names(self) -> str:
        """Return the secondary identifier, usually holder's given names.

        The remaining parts of the name are the secondary identifier. These may be the forenames, familiar
        names, given names, initials, or any other secondary names.

        """
        return self._given_names

    @given_names.setter
    def given_names(self, value: str):
        """Set the secondary identifier, usually holder's given names.

        The remaining parts of the name are the secondary identifier. These may be the forenames, familiar
        names, given names, initials, or any other secondary names.

        Case insensitive.

        """
        self._given_names = transliterate(value, self.transliteration)

    def __str__(self):
        return self.surname + "<<" + self.given_names
