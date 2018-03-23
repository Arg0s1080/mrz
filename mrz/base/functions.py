#!/usr/bin/python3
#
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
    from string import ascii_uppercase
    string = string.upper().replace("<", "0")
    weight = [7, 3, 1]
    hsh = 0
    for i in range(len(string)):
        c = list(string)[i]
        w = weight[i % 3]
        if c.isdigit():
            hsh += int(c) * w
        elif c in ascii_uppercase:
            hsh += list(ascii_uppercase).index(c) * w
        else:
            raise ValueError("%s contains invalid characters" % string, c)

    return str(hsh % 10)


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
    >>> import mrz.generator.transliterations as dictionary_
    >>> transliterate("ТЕСТ МИЛИЦА", dictionary_.cyrillic_serbian())
    'TEST<MILICA'
    >>> transliterate("Þĩŝ ïŜ Á ţęšť", dictionary_.latin_based(), " ")
    'THIS IS A TEST'
    >>> transliterate("محمود عبدالرحيم", dictionary_.arabic(), "-")
    'MXHMWD-EBDALRXHYM'
    >>> transliterate("παράδειγμα δοκιμής", dictionary_.greek())
    'PAPADEIGMA<DOKIMIS'
    """
    word = string.replace(u"\u002D", u"\u0020").split(u"\u0020")
    for i in range(len(word)):
        final_word = ""
        for char in word[i]:
            final_word += dictionary[char] if char in dictionary else char
        word[i] = final_word.upper()
    return sep.join(word)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

