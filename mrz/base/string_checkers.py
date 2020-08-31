# -*- coding: UTF-8 -*-
#
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

from string import ascii_letters
from .errors import *
from .functions import full_capitalize, get_doc

import mrz.base.countries as countries


def date(string):
    """
    >>> date("001122")
    '001122'
    >>> date("200229")
    '200229'
    """
    if check_string(string):
        try:
            from datetime import datetime
            datetime.strptime(string, "%y%m%d").strftime("%y%m%d")
        except ValueError:
            raise DateError(cause=string)
        else:
            return string


def sex(string):
    """
    >>> sex("m")
    'M'
    """
    if check_string(string) and len(string) != 1 or string not in "MmFf<":
        raise SexError(cause=string)
    return string.upper()


def field(string: str, str_length: int, field_description: str, exception="") -> str:
    """
    >>> field("string", 8, "description")
    'STRING<<'
    """
    if check_string(string) and len(string) > str_length:
        raise LengthError(document=field_description, cause=len(string), length=str_length, amx=True)
    for c in string:
        if c not in ascii_letters + "0123456789" + exception:
            raise FieldError(cause=c)
    return string.upper().ljust(str_length, "<")


def country(string, dictionary=countries.english):
    """
    >>> country("alb")
    'ALB'
    >>> country("yemen")
    'YEM'
    """
    if check_string(string) and string.upper() in dictionary.values():
        return string.upper().ljust(3, "<")
    elif full_capitalize(string) in dictionary.keys():
        return dictionary[full_capitalize(string)].ljust(3, "<")
    else:
        raise CountryError(cause=string)


def document_type(string, cls):
    # To know document type the name of the class is read. (class name must be TD1Type1CodeChecker,
    # MRVAUKCodeGenerator, TD2BRACodeGenerator, TD3CodeCheckerBlahBlah or similar)
    ok = False
    doc = get_doc(cls)
    s = string.upper()
    if check_string(s) and s and len(s) <= 2:
        if doc.startswith("TD1") or doc.startswith("TD2"):
            if s[0] in "IiAaCc" and s.find("V") != 1 and s != "AC":
                ok = True
        elif doc.startswith("TD3") or doc.startswith("Passport"):
            if s[0] in "Pp" or s[0:2].upper()=='DP':
                ok = True
        elif doc.startswith("MRVA") or doc.startswith("MRVB"):
            if s[0] in "Vv":
                ok = True
    if not ok:
        raise DocumentTypeError(cause=string)
    return s.ljust(2, "<")


def precheck(document_description: str, string: str, length: int):
    s = string.replace("\n", "")
    if check_string(_check_upper(string)) and len(string) != length:
        raise LengthError(cause=len(s), document=document_description, length=length)
    if not is_printable(string, "\n"):
        raise FieldError("%s contains invalid characters" % document_description, s)


def is_printable(string: str, additions="") -> bool:
    for c in string:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<" + additions:
            return False
    return True


def uses_nums(string: str) -> bool:
    for c in string:
        if c in "0123456789":
            return True
    return False


def begin_by(string: str, char: str) -> bool:
    if string[0] != char:
        return False
    return True


def _check_upper(string):
    if string.isupper() or string.replace("<", "0").isdigit():
        return string
    else:
        raise FieldError("String contains invalid characters. Must be upper.", string)


def is_empty(string, padding="<"):
    return string == padding * len(string)


def check_string(o):
    if isinstance(o, str):
        return True
    else:
        raise TypeError("Invalid argument. It should be a string, not a %s" % str(type(o).__name__))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

