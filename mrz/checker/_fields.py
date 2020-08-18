# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from ..base.functions import anset
from ._report import _Report, Kind
from ._honorifics import titles
from datetime import datetime, date, timedelta

import mrz.base.string_checkers as check


class _FieldsChecker:
    def __init__(self, document_type: str, country: str, identifier: str, document_number: str, nationality: str,
                 birth_date: str, sex: str, expiry_date: str, optional_data: str, optional_data_2: str,
                 check_expiry: bool, compute_warnings: bool, mrz_code: str):
        self._compute_warnings = compute_warnings
        self._document_type = document_type
        self._country = country
        self._identifier = identifier
        self._document_number = document_number
        self._nationality = nationality
        self._birth_date = birth_date
        self._birth_date_check = True  # !?
        self._sex = sex
        self._expiry_date = expiry_date
        self._expiry_date_check = True  # !?
        self._optional_data = optional_data
        self._optional_data_2 = optional_data_2
        self._check_expiry = check_expiry
        self._mrz_code = mrz_code
        self.report = _Report()
        self._times()
        self._id_primary = self._id_secondary = None  # Will be set later

    @property
    def mrz_code(self):
        """Return Machine Readable Zone code string"""

        return self._mrz_code

    @property
    def document_type(self) -> bool:
        """Return True if document type code is validated, False otherwise"""

        ok = False
        try:
            ok = bool(check.document_type(self._document_type, self))
        except ValueError:  # as error:
            # print("%s: %s", (error.args[0], error.args[1]))
            pass
        finally:
            return self.report.add("document type format", ok)

    @property
    def country(self) -> bool:
        """Return True if the country code is validated, False otherwise."""

        import mrz.base.countries_ops as chk
        return self.report.add("valid country code", chk.is_code(self._country.replace("<", "")))

    @property
    def identifier(self) -> bool:
        """Return True is the identifier is validated overcoming the checks, False otherwise."""
        full_id = self._identifier.rstrip("<")
        padding = self._identifier[len(full_id):]
        id2iter = full_id.split("<<")
        id_len = len(id2iter)
        primary = secondary = None
        if not check.is_printable(self._identifier):
            ok = False
        elif check.is_empty(self._identifier):
            self.report.add("empty identifier", level=Kind.ERROR)
            ok = False
        else:
            if id_len == len([i for i in id2iter if i]):
                if id_len == 2:
                    primary, secondary = id2iter
                    ok = True
                elif id_len == 1:
                    primary, secondary = id2iter[0], ""
                    self.report.add("only one identifier", level=Kind.WARNING)
                    ok = not self._compute_warnings
                else:
                    self.report.add("more than two identifiers", level=Kind.ERROR)
                    ok = False
            else:  # too many '<' in id
                self.report.add("invalid identifier format", level=Kind.ERROR)
                ok = False
        # print("Debug. id2iter ............:", id2iter)
        # print("Debug. (secondary, primary):", (secondary, primary))
        # print("Debug. padding ............:", padding)
        if ok:
            if check.uses_nums(full_id):
                self.report.add("identifier with numbers", level=Kind.ERROR)
                ok = False
            if primary.startswith("<") or secondary and secondary.startswith("<"):
                self.report.add("some identifier begin by '<'", level=Kind.ERROR)
                ok = False
            if not padding:
                self.report.add("possible truncating", level=Kind.WARNING)
                ok = False if self._compute_warnings else ok
            for i in range(id_len):
                for itm in id2iter[i].split("<"):
                    if itm:
                        for tit in titles:
                            if tit == itm:
                                if i:  # secondary id
                                    self.report.add("Possible unauthorized prefix or suffix in identifier",
                                                 level=Kind.WARNING)
                                else:  # primary id
                                    self.report.add("Possible not recommended prefix or suffix in identifier",
                                                 level=Kind.WARNING)
                                ok = False if self._compute_warnings else ok
        self._id_secondary = str(secondary)
        self._id_primary = str(primary)
        return self.report.add("identifier", ok)

    @property
    def document_number(self) -> bool:
        """Return True if the document number format is validated, False otherwise."""

        s = self._document_number
        return self.report.add("document number format",
                            not check.is_empty(s) and check.is_printable(s) and not check.begin_by(s, "<"))

    @property
    def nationality(self) -> bool:
        """
        Return True if nationality code is validated, False otherwise.

        """
        import mrz.base.countries_ops as chk
        return self.report.add("valid nationality code", chk.is_code(self._nationality.replace("<", "")))

    @property
    def birth_date(self) -> bool:
        """Return True is the birth date is validated, False otherwise."""

        ok = False
        try:
            # TODO: Make comment about self._birth_date_check (if check_periods == True)
            ok = False if not self._birth_date_check else bool(check.date(self._birth_date))
        except ValueError:
            pass
        finally:
            return self.report.add("birth date", ok)

    @property
    def sex(self) -> bool:
        """Return True if the sex is "M", "F", "X", "<" or "", False otherwise."""

        ok = False
        try:
            ok = bool(check.sex(self._sex))
        except ValueError:
            pass
        finally:
            return self.report.add("valid genre format", ok)

    @property
    def expiry_date(self) -> bool:
        """Return True if the expiry date is validated, False otherwise."""

        ok = False
        try:
            # TODO: Make comment about self._expiry_date_check (if check_periods == True)
            ok = False if not self._expiry_date_check else bool(check.date(self._expiry_date))
        except ValueError:
            pass
        finally:
            return self.report.add("expiry date", ok)

    @property
    def optional_data(self) -> bool:
        """Return True if the format of the optional data field is validated, False otherwise."""
        s = self._optional_data
        return True if check.is_empty(s) else self.report.add("optional data format", check.is_printable(s))

    @property
    def optional_data_2(self) -> bool:
        """Return True if the format of the optional data field is validated, False otherwise."""
        s = self._optional_data_2
        return True if check.is_empty(s) else self.report.add("optional data 2 format", check.is_printable(s))

    def _times(self) -> bool:
        birth = expiry = None

        try:
            birth = datetime.strptime(self._birth_date, "%y%m%d")
        except ValueError:
            self._birth_date_check = False
        try:
            expiry = datetime.strptime(self._expiry_date, "%y%m%d") + timedelta(days=1)
        except ValueError:
            self._expiry_date_check = False

        if self._birth_date_check & self._expiry_date_check:
            today = datetime.combine(date.today(), datetime.min.time())
            leap = not today.year % 4 and date.today() == date(today.year, 2, 29)
            birth = birth if birth < today else birth.replace(year=birth.year - 100)   # cancel check2

            check1 = expiry > birth
            # check2 = birth < today  # Canceled
            check3 = expiry > today
            today = datetime.today().replace(month=3, day=1) if leap else today
            check4 = expiry < today.replace(year=today.year + 10)

            # print("Debug:", ("Birth:", str(birth.date())), ("Expiry:", str(expiry.date())))
            rep = lambda s, c, k=Kind.ERROR: not c and self.report.add(s, level=k)
            rep("expiry date before than birth date", check1)
            # rep("birth date after than today", check2)  # check2 canceled
            self._check_expiry and rep("document expired", check3, Kind.WARNING)
            self._check_expiry and rep("expiry date greater than 10 years", check4, Kind.WARNING)

            self._birth_date_check = check1  # & check2   # check2 canceled
            self._expiry_date_check = check1 if not self._compute_warnings else check1 & check3 & check4

        return self._birth_date_check & self._expiry_date_check

    def _all_fields(self) -> bool:
        return (self.document_type &
                self.country &
                self.nationality &
                self.birth_date &
                self.expiry_date &
                self.sex &
                self.identifier &
                self.document_number &
                self.optional_data &
                self.optional_data_2)

    def _str_common_fields(self, zfill: bool):
        fields = (self._id_primary.replace("<", " "),
                  self._id_secondary.replace("<", " "),
                  self._country.rstrip("<"),
                  self._nationality.rstrip("<"),
                  self._birth_date,
                  self._expiry_date,
                  self._sex,
                  self._document_type.rstrip("<"),
                  anset(self._document_number, zfill),
                  anset(self._optional_data, zfill))
        names = ("surname name country nationality birth_date expiry_date sex "
                 "document_type document_number optional_data ")
        return fields, names

    def __repr__(self) -> str:
        return str(self._all_fields())

