# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

import mrz.base.countries as countries
from mrz.base.functions import full_capitalize

dictionary = countries.english


def code_list() -> list:
    """Return a sorted list with country codes

    Returns:
        The list, alphabetically sorted, of 3-letter countries codes conform to ICAO
        specifications (also included in ISO 3166-1 alpha 3)

        """
    return [dictionary[country] for country in sorted(dictionary, key=dictionary.__getitem__)]


def countries_list():
    """Return a sorted list with country names

    Returns:
        The list of all countries and organizations recognized by ICAO, denominated
        in English, alphabetically ordered.

        """
    return [country for country in sorted(dictionary)]


def countries_code_list() -> list:
    """Return a sorted list of tuples with all country names and country codes

    Returns:
        A list, alphabetically sorted, of tuples with all countries and organizations,
        denominated in English, recognized by ICAO and their 3-letters code. The first
        element of the tuple is the country name and the second is its 3-letter code.

        """
    # return [(country, code) for country, code in sorted(dictionary.items())]
    return [country for country in sorted(dictionary.items())]


def code_country_list() -> list:
    """Return a list of tuples with all 3-letter codes and their corresponding countries names

    Returns:
        A list, alphabetically sorted, of tuples with all countries and organizations,
        denominated in English, recognized by ICAO and their 3-letters code. The first
        element of the tuple is the 3-letter code and the second is the country name.

        """
    return [(dictionary[country], country) for country in sorted(dictionary, key=dictionary.__getitem__)]


def is_country(country: str) -> bool:
    """Return True if the parameter is valid country string, False otherwise

    Returns:
        True if the parameter is a valid country name, denominated in English and
        otherwise False. Note: case insensitive method

        """
    return True if full_capitalize(country) in dictionary.keys() else False


def is_code(code: str) -> bool:
    """Return True if the parameter is a valid country code string, False otherwise

    Returns:
        True if the parameter is a valid 3-letter country code conform to ICAO
        specifications and False otherwise. Note: case insensitive method.

        """
    return True if code.upper() in dictionary.values() else False


def get_code(country: str) -> object:
    """Get the 3-letter code of a valid country name, None otherwise

    Parameter:
        Country string, denominated in English. Note: case insensitive.
    Returns:
        3-letter country code, conform to ICAO specifications, of the country string
        given as parameter and None otherwise. Note: case insensitive method.

        """
    try:
        return dictionary[full_capitalize(country)]
    except KeyError:
        return None


def get_country(code: str) -> object:
    """Get the country string of a valid 3-letter code, None otherwise

    Parameter:
        3-letter code string, conform to ICAO specifications. Note: case insensitive.
    Returns:
        Country name string, denominated in English, of the 3-letter code given as
        parameter, None otherwise.

        """
    for country, value in dictionary.items():
        if value == code.upper():
            return country
    return None


def find_country(pattern: str) -> list:
    """Search all countries that matches the given pattern

    Parameter:
        String pattern to search.
    Returns:
        A list of countries, denominated in English, matching the given pattern

        """
    return [country for country in sorted(dictionary) if pattern.lower() in country.lower()]

