#!/usr/bin/python3
# -*- coding: utf-8 -*-
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

from string import ascii_uppercase, digits


def hash_string(string: str) -> str:
    """
    >>> hash_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    '7'
    >>> hash_string("0123456789")
    '7'
    >>> hash_string("0123456789ABCDEF")
    '0'
    >>> hash_string("0")
    '0'
    """
    printable = digits + ascii_uppercase
    string = string.upper().replace("<", "0")
    weight = [7, 3, 1]
    summation = 0
    for i in range(len(string)):
        c = string[i]
        if c not in printable:
            raise ValueError("%s contains invalid characters" % string, c)
        summation += printable.index(c) * weight[i % 3]
    return str(summation % 10)


def hash_is_ok(string: str, hash_: str) -> bool:
    """
    >>> hash_is_ok("0123456789abcdef", "0")
    True
    >>> hash_is_ok("0", "1")
    False
    """
    return True if hash_string(string) == hash_ else False


def full_capitalize(string: str) -> str:
    """
        >>> full_capitalize("It'S A teSt")
        "It's A Test"
    """
    if " " in string:
        t = string.split()
        for i in range(len(t)):
            t[i] = t[i].capitalize()
        return " ".join(t)
    else:
        return string.capitalize()


def transliterate(string: str, dictionary: dict, sep="<") -> str:
    """
    >>> from mrz.generator.dictionaries.cyrillic_serbian import transliteration as serbian
    >>> from mrz.generator.dictionaries.latin_based import transliteration as latin_based
    >>> from mrz.generator.dictionaries.arabic import transliteration as arabic
    >>> from mrz.generator.dictionaries.greek import transliteration as greek
    >>> transliterate("ТЕСТ МИЛИЦА", serbian)
    'TEST<MILICA'
    >>> transliterate("Þĩŝ ïŜ Á ţęšť", latin_based, " ")
    'THIS IS A TEST'
    >>> transliterate("محمود عبدالرحيم", arabic, "-")
    'MXHMWD-EBDALRXHYM'
    >>> transliterate("παράδειγμα δοκιμής", greek)
    'PAPADEIGMA<DOKIMIS'
    """
    word = string.replace(u"\u002D", u"\u0020").split(u"\u0020")
    for i in range(len(word)):
        final_word = ""
        for char in word[i]:
            final_word += dictionary[char] if char in dictionary else char
        word[i] = final_word.upper()
    return sep.join(word)


def get_doc(cls):
    name = cls.__class__.__name__
    return name[:name.find("Code")]


def namedtuple_maker(*args):
    # USE:
    # namedtuple_maker(common_fields, common_hashes)
    # namedtuple_maker(common_fields, common_hashes, extra_fields, extra_names)
    from collections import namedtuple

    cf, cfn = args[0]
    ch, chn = args[1]
    names = cfn + chn
    fields = cf + ch
    if len(args) > 2:
        names += args[3]
        fields += args[2]
    data = namedtuple("fields", names)
    return data(*fields)


def anset(string: str, zfill: bool) -> str:
    # AlphaNum string setter
    return string.strip("<") if not zfill else string.replace("<", "0")


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

