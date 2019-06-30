# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from enum import Enum, IntEnum

class Kind(IntEnum):  # kind = 0: fields, 1: warning, 2: error
    FIELDS = 0
    WARNING = 1
    ERROR = 2


class Foo(Enum):
    AAA = 0
    BBB = 1
    CCC = 2


print(type(Kind.FIELDS))
print(type(Foo.AAA))