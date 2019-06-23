# -*- coding: UTF-8 -*-

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
# (ɔ) Iván Rincón 2018


# Latin based

transliteration = {
    u"\u0027": "",                      # '
    u"\u00C1": "A",   u"\u00E1": "a",   # Á, á
    u"\u00C0": "A",   u"\u00E0": "a",   # À, à
    u"\u00C2": "A",   u"\u00E2": "a",   # Â, â
    u"\u00C4": "AE",  u"\u00E4": "ae",  # Ä, ä
    u"\u00C3": "A",   u"\u00E3": "a",   # Ã, ã
    u"\u0102": "A",   u"\u0103": "a",   # Ă, ă
    u"\u00C5": "AA",  u"\u00E5": "aa",  # Å, å
    u"\u0100": "A",   u"\u0101": "a",   # Ā, ā
    u"\u0104": "A",   u"\u0105": "a",   # Ą, ą
    u"\u0106": "C",   u"\u0107": "c",   # Ć, ć
    u"\u0108": "C",   u"\u0109": "c",   # Ĉ, ĉ
    u"\u010C": "C",   u"\u010D": "c",   # Č, č
    u"\u010A": "C",   u"\u010B": "c",   # Ċ, ċ
    u"\u00C7": "C",   u"\u00E7": "c",   # Ç, ç
    u"\u0110": "D",   u"\u0111": "d",   # Đ, đ
    u"\u010E": "D",   u"\u010F": "d",   # Ď, ď
    u"\u00D0": "D",   u"\u00F0": "d",   # Ð, ð
    u"\u00C9": "E",   u"\u00E9": "e",   # É, é
    u"\u00C8": "E",   u"\u00E8": "e",   # È, è
    u"\u00CA": "E",   u"\u00EA": "e",   # Ê, ê
    u"\u00CB": "E",   u"\u00EB": "e",   # Ë, ë
    u"\u011A": "E",   u"\u011B": "e",   # Ě, ě
    u"\u0116": "E",   u"\u0117": "e",   # Ė, ė
    u"\u0112": "E",   u"\u0113": "e",   # Ē, ē
    u"\u0118": "E",   u"\u0119": "e",   # Ę, ę
    u"\u0114": "E",   u"\u0115": "e",   # Ĕ, ĕ
    u"\u011C": "G",   u"\u011D": "g",   # Ĝ, ĝ
    u"\u011E": "G",   u"\u011F": "g",   # Ğ, ğ
    u"\u0120": "G",   u"\u0121": "g",   # Ġ, ġ
    u"\u0122": "G",   u"\u0123": "g",   # Ģ, ģ
    u"\u0126": "H",   u"\u0127": "h",   # Ħ, ħ
    u"\u0124": "H",   u"\u0125": "h",   # Ĥ, ĥ
    u"\u00CD": "I",   u"\u00ED": "i",   # Í, í
    u"\u00CC": "I",   u"\u00EC": "i",   # Ì, ì
    u"\u00CE": "I",   u"\u00EE": "i",   # Î, î
    u"\u00CF": "I",   u"\u00EF": "i",   # Ï, ï
    u"\u0128": "I",   u"\u0129": "i",   # Ĩ, ĩ
    u"\u0130": "I",   u"\u0131": "i",   # İ, ı
    u"\u012A": "I",   u"\u012B": "i",   # Ī, ī
    u"\u012E": "I",   u"\u012F": "i",   # Į, į
    u"\u012C": "I",   u"\u012D": "i",   # Ĭ, ĭ
    u"\u0134": "J",   u"\u0135": "j",   # Ĵ, ĵ
    u"\u0136": "K",   u"\u0137": "k",   # Ķ, ķ
    u"\u0141": "L",   u"\u0142": "l",   # Ł, ł
    u"\u0139": "L",   u"\u013A": "l",   # Ĺ, ĺ
    u"\u013D": "L",   u"\u013E": "l",   # Ľ, ľ
    u"\u013B": "L",   u"\u013C": "l",   # Ļ, ļ
    u"\u013F": "L",   u"\u0140": "l",   # Ŀ, ŀ
    u"\u0143": "N",   u"\u0144": "n",   # Ń, ń
    u"\u00D1": "N",   u"\u00F1": "n",   # Ñ, ñ
    u"\u0147": "N",   u"\u0148": "n",   # Ň, ň
    u"\u0145": "N",   u"\u0146": "n",   # Ņ, ņ
    u"\u014A": "N",   u"\u014B": "n",   # Ŋ, ŋ
    u"\u00D8": "OE",  u"\u00F8": "oe",  # Ø, ø
    u"\u00D3": "O",   u"\u00F3": "o",   # Ó, ó
    u"\u00D2": "O",   u"\u00F2": "o",   # Ò, ò
    u"\u00D4": "O",   u"\u00F4": "o",   # Ô, ô
    u"\u00D6": "OE",  u"\u00F6": "oe",  # Ö, ö
    u"\u00D5": "O",   u"\u00F5": "o",   # Õ, õ
    u"\u0150": "O",   u"\u0151": "o",   # Ő, ő
    u"\u014C": "O",   u"\u014D": "o",   # Ō, ō
    u"\u014E": "O",   u"\u014F": "o",   # Ŏ, ŏ
    u"\u0154": "R",   u"\u0155": "r",   # Ŕ, ŕ
    u"\u0158": "R",   u"\u0159": "r",   # Ř, ř
    u"\u0156": "R",   u"\u0157": "r",   # Ŗ, ŗ
    u"\u015A": "S",   u"\u015B": "s",   # Ś, ś
    u"\u015C": "S",   u"\u015D": "s",   # Ŝ, ŝ
    u"\u0160": "S",   u"\u0161": "s",   # Š, š
    u"\u015E": "S",   u"\u015F": "s",   # Ş, ş
    u"\u0166": "T",   u"\u0167": "t",   # Ŧ, ŧ
    u"\u0164": "T",   u"\u0165": "t",   # Ť, ť
    u"\u0162": "T",   u"\u0163": "t",   # Ţ, ţ
    u"\u00DA": "U",   u"\u00FA": "u",   # Ú, ú
    u"\u00D9": "U",   u"\u00F9": "u",   # Ù, ù
    u"\u00DB": "U",   u"\u00FB": "u",   # Û, û
    u"\u00DC": "UE",  u"\u00FC": "ue",  # Ü, ü
    u"\u0168": "U",   u"\u0169": "u",   # Ũ, ũ
    u"\u016C": "U",   u"\u016D": "u",   # Ŭ, ŭ
    u"\u0170": "U",   u"\u0171": "u",   # Ű, ű
    u"\u016E": "U",   u"\u016F": "u",   # Ů, ů
    u"\u0172": "U",   u"\u0173": "u",   # Ų, ų
    u"\u0174": "W",   u"\u0175": "w",   # Ŵ, ŵ
    u"\u00DD": "Y",   u"\u00FD": "y",   # Ý, ý
    u"\u0176": "Y",   u"\u0177": "y",   # Ŷ, ŷ
    u"\u0178": "Y",   u"\u00FF": "y",   # Ÿ, ÿ
    u"\u0179": "Z",   u"\u017A": "z",   # Ź, ź
    u"\u017D": "Z",   u"\u017E": "z",   # Ž, ž
    u"\u017B": "Z",   u"\u017C": "z",   # Ż, ż
    u"\u00DE": "TH",  u"\u00FE": "th",  # Þ, þ
    u"\u00C6": "AE",  u"\u00E6": "ae",  # Æ, æ
    u"\u0132": "IJ",  u"\u0133": "ij",  # Ĳ, ĳ
    u"\u0152": "OE",  u"\u0153": "oe",  # Œ, œ
    u"\u1E9E": "SS",  u"\u00DF": "ss"   # ẞ, ß
}

# https://www.icao.int/publications/Documents/9303_p3_cons_en.pdf
# https://en.wikipedia.org/wiki/List_of_Unicode_characters

# Function to get unicode string
'''
def str2unicode(string):
    """Prints the unicode hex representation of each char in a string

        Note: Only for development purposes"""
    def gv(s):
        return s[2:].zfill(4)
    print("{")
    for c in string:
        u = c.encode("unicode_escape").decode()  # é -> \xe9, a -> a, 𐍈 -> \U00010348
        ln = len(u)
        prefix = "\\u" if ln < 7 else u[:2]
        value = gv(hex(ord(u))) if ln < 2 else gv(u) if ln < 7 else u[2:]
        # print('%s: u"%s%s"' % (c, prefix, value.upper()))
        print('    u"%s%s": "%s",' % (prefix, value.upper(), c))
    print("}")
'''