# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned on making available
# complete source code of licensed works and modifications, which include larger works
# using a licensed work, under the same license. Copyright and license notices must be
# preserved. Contributors provide an express grant of patent rights.
#
# For more information on this, and how to apply and follow theGNU GPL, see:
# http://www.gnu.org/licenses
#
# Iván Rincón 2018

from string import ascii_letters
from mrz.base.errors import *

import mrz.base.countries as countries
import mrz.base.functions as functions


def date(string):
    """
    >>> date("001122")
    '001122'
    >>> date("200229")
    '200229'
    """
    if _is_string(string):
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
    if _is_string(string) and len(string) != 1 or string not in "MmFfXx":
        raise SexError(cause=string)
    return string.upper()


def field(string: str, str_length: int, field_description: str, exception="") -> str:
    """
    >>> field("string", 8, "description")
    'STRING<<'
    """
    if _is_string(string) and len(string) > str_length:
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
    if _is_string(string) and string.upper() in dictionary.values():
        return string.upper().ljust(3, "<")
    elif functions.full_capitalize(string) in dictionary.keys():
        return dictionary[functions.full_capitalize(string)].ljust(3, "<")
    else:
        raise CountryError(cause=string)


def document_type(string, td3=False):
    """
    >>> document_type("ID")
    'ID'
    >>> document_type("px", td3=True)
    'PX'
    """
    s = string.upper()
    if _is_string(s) and s and len(s) <= 2:
        if not td3 and s[0] in "IiAaCc" and s.find("V") != 1 and s != "AC":
            return s.ljust(2, "<")
        elif td3 and s[0] in "Pp":
            return s.ljust(2, "<")
    raise DocumentTypeError(cause=string)


def precheck(document_description: str, string: str, length: int):
    s = string.replace("\n", "")
    if _is_string(_check_upper(string)) and len(s) != length:
        raise LengthError(cause=len(string), document=document_description, length=length)
    if not is_printable(s):
        raise FieldError("%s contains invalid characters" % document_description, s)


def is_printable(string: str) -> bool:
    for c in string:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<":
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


def _is_string(o):
    if isinstance(o, str):
        return True
    else:
        raise TypeError("Invalid argument. It should be a string, not a %s" % str(type(o).__name__))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

