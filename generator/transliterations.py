#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned
# on making available complete source code of licensed works
# and modifications, which include larger works using a licensed
# work, under the same license. Copyright and license notices
# must be preserved. Contributors provide an express grant of
# patent rights.
#
# For more information on this, and how to apply and follow the
# GNU GPL, see http://www.gnu.org/licenses
#
# (ɔ) Iván Rincón 2018


def arabic():
    from .dictionaries.arabic import transliteration
    return transliteration


def cyrillic():
    from .dictionaries.cyrillic import transliteration
    return transliteration


def cyrillic_belarussian():
    from .dictionaries.cyrillic_belarussian import transliteration
    return transliteration


def cyrillic_bulgarian():
    from .dictionaries.cyrillic_bulgarian import transliteration
    return transliteration


def cyrillic_macedonian():
    from .dictionaries.cyrillic_macedonian import transliteration
    return transliteration


def cyrillic_serbian():
    from .dictionaries.cyrillic_serbian import transliteration
    return transliteration


def cyrillic_ukrainian():
    from .dictionaries.cyrillic_ukrainian import transliteration
    return transliteration


def greek():
    from .dictionaries.greek import transliteration
    return transliteration


def latin_based():
    from .dictionaries.latin_based import transliteration
    return transliteration


