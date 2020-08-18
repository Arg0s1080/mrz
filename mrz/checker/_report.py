# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from enum import IntEnum


class Kind(IntEnum):
    # Base class is IntEnum instead Enum for compatibility with previous versions of mrz
    # e.g. with Enum Kind.ERROR != 2, with IntEnum Kind.ERROR == 2
    FIELDS = 0
    WARNING = 1
    ERROR = 2


class _Report:

    def __init__(self):
        self._rep = [[], [], []]  # [[fields], [warnings], [errors]]

    def add(self, description, result=None, level=Kind.FIELDS):
        # kind = 0: fields, 1: warning, 2: error
        if result is not None:
            self._rep[Kind.FIELDS].append((description, result))
            if result is False:
                self._rep[Kind.ERROR].append("false %s" % description)
        else:
            self._rep[level].append(description)
        return result

    def reset(self):
        self._rep = [[], [], []]

    @property
    def fields(self) -> list:
        """Returns a list with all fields checked.

        Returns:
            A list of tuples. In the tuples, the first item is a string with the field description,
            the second one is a bool with the result.

            """
        return self._rep[0]

    @property
    def falses(self) -> list:
        """Returns a list of tuples with all wrong fields checked."""

        return [item for item in self._rep[0] if not item[1]]

    @property
    def warnings(self) -> list:
        """Returns a list of detected warnings"""

        return self._rep[1]

    @property
    def errors(self) -> list:
        """Returns a list of detected errors"""

        return self._rep[2]
