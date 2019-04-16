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


# Modern hebrew (Experimental)

transliteration = {
    u"\u0027": "",                 # '

    # Consonants
    u"\u05D0":             "",     # א
    u"\u05D1":             "V",    # ב
    u"\u05D1" + u"\u05BC": "B",    # בּ
    u"\uFB31":             "B",    # בּ
    u"\u05D2":             "G",    # ג
    u"\u05D2" + u"\u05BC": "G",    # גּ
    u"\uFB32":             "G",    # גּ‬‬
    u"\u05D2" + u"\u05F3": "J",    # ג׳
    u"\u05D3":             "D",    # ד
    u"\u05D3" + u"\u05BC": "D",    # דּ
    u"\uFB33":             "D",    # דּ
    u"\u05D3" + u"\u05F3": "DH",   # ד׳
    u"\u05D4":             "H",    # ה
    u"\u05D4" + u"\u05BC": "H",    # הּ
    u"\uFB34":             "H",    # הּ
    u"\u05D5":             "V",    # ו‬
    u"\u05D5" + u"\u202C": "V",    # ו‬
    u"\u05D5" + u"\u05BC": "V",    # וּ
    # u"\uFB35":             "V",  # וּ  # To vowels "U"
    u"\u05D6":             "Z",    # ז
    u"\u05D6" + u"\u05BC": "Z",    # זּ
    u"\uFB36":             "Z",    # זּ‬
    u"\u05D6" + u"\u05F3": "ZH",   # ז׳
    u"\u05D7":             "CH",   # ח
    u"\u05D8":             "T",    # ט
    u"\u05D8" + u"\u05BC": "T",    # טּ
    u"\uFB38":             "T",    # טּ
    u"\u05D9":             "Y",    # י
    u"\u05D9" + u"\u05BC": "Y",    # יּ
    u"\u05D9" + u"\u05BC" +
    u"\u202C":             "Y",    # יּ‬
    u"\uFB39":             "Y",    # יּ‬
    u"\u05DB":             "CH",   # כ
    u"\u05DB" + u"\u05BC": "CH",   # כּ
    u"\u05DB" + u"\u05BC" +
    u"\u202C":             "CH",   # כּ
    u"\uFB3B":             "C",    # כּ
    u"\u05DA":             "CH",   # ך
    u"\u05DA" + u"\u05BC": "CH",   # ךּ
    u"\u05DA" + u"\u05BC" +
    u"\u202C":             "CH",   # ךּ‬
    u"\uFB3A":             "CH",   # ךּ
    u"\u05DC":             "L",    # ל‬
    u"\u05DC" + u"\u05BC": "L",    # לּ
    u"\uFB3C":             "L",    # לּ
    u"\u05DD":             "M",    # ם
    u"\u05DE":             "M",    # מ‬
    u"\u05DE" + u"\u05BC": "M",    # מּ
    u"\uFB3E":             "M",    # מּ‬
    u"\u05DF":             "N",    # ן
    u"\u05E0":             "N",    # נ
    u"\u05E0" + u"\u05BC": "N",    # נּ
    u"\uFB40":             "N",    # נּ
    u"\u05E1":             "S",    # ס
    u"\u05E1" + u"\u05BC": "S",    # סּ
    u"\uFB41":             "S",    # סּ
    u"\u05E2":             "",     # ע
    u"\u05E3":             "F",    # ף
    u"\u05E3" + u"\u05BC": "P",    # Possible problem u05BC # ףּ
    u"\uFB43":             "P",    # ףּ
    u"\u05E4":             "F",    # פ‬
    u"\u05E4" + u"\u05BC": "P",    # פּ
    u"\uFB44":             "P",    # פּ
    u"\u05E5":             "TZ",   # ץ
    u"\u05E5" + u"\u05F3": "TSH",  # Possible problem u05F3  # ץ׳
    u"\u05E6":             "TZ",   # צ‬
    u"\u05E6" + u"\u05BC": "TZ",   # צּ
    u"\uFB46":             "TZ",   # צּ‬
    u"\u05E6" + u"\u05F3": "TSH",  # Possible problem u05F3  # צ׳
    u"\u05E7":             "Q",    # ק
    u"\u05E7" + u"\u05BC": "Q",    # קּ
    u"\uFB47":             "Q",    # קּ‬
    u"\u05E8":             "R",    # ר
    u"\u05E8" + u"\u05BC": "R",    # רּ
    u"\uFB48":             "R",    # רּ
    u"\u05E9":             "S",    # ש
    u"\u05E9" + u"\u05BC": "S",    # שּ
    u"\uFB49":             "S",    # שּ‬
    u"\u05E9" + u"\u05C2" +
    u"\u202C":             "S",    # שׂ
    u"\uFB2B":             "S",    # שׂ
    u"\u05E9" + u"\u05C1": "SH",   # שׁ
    u"\uFB2A":             "SH",   # שׁ
    u"\u05E9" + u"\u05BC" +
    u"\u05C2" + u"\u202C": "S",    # שּׂ‬
    u"\uFB2D":             "S",    # שּׂ
    u"\u05EA":             "T",    # ת
    u"\u05EA" + u"\u05BC": "T",    # תּ
    u"\uFB4A":             "T",    # תּ
    u"\u05EA" + u"\u05F3": "T",    # ת׳

    # Niqqud vowels
    u"\u05B0":             "E",    # ( ְ‬ )
    u"\u05B1":             "E",    # ( ֱ )
    u"\u05B2":             "A",    # ( ֲ )
    u"\u05B3":             "O",    # ( ֲ )
    u"\u05B4":             "I",    # ( ִ )
    u"\u05B5":             "E",    # ( ֵ )
    u"\u05B6":             "E",    # ( ֶ )
    u"\u05B7":             "A",    # ( ַ )
    u"\u05B8":             "O",    # ( ָ ) # It could be "A" too
    u"\u05B9":             "O",    # ( ֹ )
    u"\u05BB":             "U",    # ( ֻ )
    u"\u05D5" + u"\u05BC": "U",    # ( וּ )
    u"\uFB35":             "U",    # ( וּ )

    # Diphthongs
    u"\u05B5" + u"\u05D9": "EI",   # ( ֵי )
    u"\u05B6" + u"\u05D9": "EI",   # ( ֶי )
    u"\u05B7" + u"\u05D9": "AI",   # ( ַי )
    u"\u05B7" + u"\u05D9" +
    u"\u05B0":             "AI",   # ( ַיְ )
    u"\u05B7" + u"\u05D9" +
    u"\u05B0" + u"\u202C": "AI",   # ( ַיְ‬ )
    u"\u05B8" + u"\u05D9": "AI",   # ( ָי )
    u"\u05B8" + u"\u05D9" +
    u"\u202C":             "AI",   # ( ָי‬ )
    u"\u05B8" + u"\u05D9" +
    u"\u05B0":             "AI",   # ( ָיְ )
    u"\u05B8" + u"\u05D9" +
    u"\u05B0" + u"\u202C": "AI",   # ( ָיְ‬ )
    u"\u05B9" + u"\u05D9": "OI",   # ( ֹי )
    u"\u05B9" + u"\u05D9" +
    u"\u05B0":             "OI",   # ( ֹיְ )
    u"\u05B9" + u"\u05D9" +
    u"\u05B0" + u"\u202C": "OI",   # ( ֹיְ‬ )
    u"\u05BB" + u"\u05D9": "UI",   # ( ֻי )
    u"\u05BB" + u"\u05D9" +
    u"\u05B0":             "UI",   # ( ֻיְ )
    u"\u05BB" + u"\u05D9" +
    u"\u05B0" + u"\u202C": "UI",   # ( ֻיְ‬ )
    u"\u05D5" + u"\u05BC" +
    u"\u05D9":             "UI",   # ( וּי )
    u"\u05D5" + u"\u05BC" +
    u"\u05D9" + u"\u05B0": "UI",   # ( וּיְ )
    u"\u05D5" + u"\u05BC" +
    u"\u05D9" + u"\u05B0" +
    u"\u202C":             "UI",   # ( וּיְ‬ )

}

# https://en.wikipedia.org/wiki/Romanization_of_Hebrew
