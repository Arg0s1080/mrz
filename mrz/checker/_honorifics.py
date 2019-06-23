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
# (ɔ) Iván Rincón 2018


""" Forbidden titles

    ICAO SPECS:

    Prefixes and suffixes, including titles, professional and academic qualifications,
    honours, awards, and hereditary status (such as Dr., Sir, Jr., Sr., I I and III)
    shall not be included in the MRZ except where the issuing State considers these to
    be legally part of the name. In such cases, prefixes or suffixes shall be represented
    as components of the secondary identifier(s)

    Therefore, items in the list below will be reported as warnings or errors if they
    are found in the secondary id. or primary id.

    Add or delete items according to needs

"""
# Forbidden titles:


titles = [
    "MR",
    "SIR",
    "JR",
    "MRS",
    "MISS",
    "MS",
    "MADAM",
    "DAME",
    "DR",
    "LADY",
    "LORD",
    "MX",
    "ESQ",
    "HE",
    "HON",
    "PROF",
    "MEP",
    "MP",
    "BT",
    "HON",
    "QC",
    "KC",
    "HH",
    "HAH",
    "HE",
    "HMEH",
    "REVD",
    "REV",
    "FR",
    "PR",
    "BR",
    "IMAN",
    "MUFTI",
    "HAFIZ",
    "HAFIZAH",
    "QARI",
    "MAWLANA",
    "HAJI",
    "SAYYID",
    "SAYYIDAH",
    "SHARIF",
    "SRI",
    "SREE",
    "SHRI",
    "SHREE",
    "SIRI",
    "SERI",
    "SMT",
    "KUM",
    "HER",
    "FRAU",
    "SIE",
    "EXCMO",
    "ILMO"
]
