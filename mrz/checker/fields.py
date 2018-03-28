# GNU General Public License v3.0

import mrz.base.string_checkers as check
import mrz.checker.honorifics as honorifics
from datetime import datetime, date, timedelta
from mrz.checker.report import Report


class FieldChecker(Report):
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
        self._birth_date_check = True
        self._sex = sex
        self._expiry_date = expiry_date
        self._expiry_date_check = True
        self._optional_data = optional_data
        self._optional_data_2 = optional_data_2
        self._check_expiry = check_expiry
        self._mrz_code = mrz_code
        self._times()

    @property
    def mrz_code(self):
        """Return Machine Readable Zone code string"""

        return self._mrz_code

    @property
    def document_type(self) -> bool:
        """Return True if document type code is validated, False otherwise"""

        ok = False
        try:
            ok = bool(check.document_type(self._document_type))
        except ValueError:  # as error:
            # print("%s: %s", (error.args[0], error.args[1]))
            pass
        finally:
            return self._report("document type format", ok)

    @property
    def country(self) -> bool:
        """Return True if the country code is validated, False otherwise."""

        import mrz.base.countries_ops as chk
        return self._report("valid country code", chk.is_code(self._country.replace("<", "")))

    @property
    def identifier(self) -> bool:
        """Return True is the identifier is validated overcoming the checks, False otherwise."""

        from mrz import checker
        id_ = self._identifier
        if not check.is_printable(id_):
            return self._report("identifier", False)
        ok = True
        if check.is_empty(id_):
            return self._report("empty identifier", kind=2)
        if check.uses_nums(id_):
            self._report("identifier with numbers", kind=2)
            ok &= False
        id2iter = id_.split("<<")
        if len(id2iter) == 1:
            secondary = id2iter[0]
            primary = ""
            ok &= False if self._compute_warnings else ok
            # print("Only one identifier")
            self._report("only one identifier", kind=1)
        else:
            secondary = id2iter[1]
            primary = id2iter[0]
        # print("Debug. (name, surname):", (secondary, primary))
        # secondary is not ok. secondary -= padding  # secondary.replace(padding, "")
        padding = id_[id_.find(secondary) + len(secondary):]
        padding = padding if primary != secondary else padding.replace(secondary, "")
        # print("Debug. padding:", padding)
        if not len(padding) and id_[-1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self._report("possible truncating", kind=1)
            ok &= False if self._compute_warnings else ok  # TODO: compute as False?
        if not check.is_empty(padding):
            # print("Error, Padding is not empty")
            self._report("more than two identifiers", kind=2)
            ok &= False
        if check.begin_by(primary, "<") or check.begin_by(secondary, "<"):
            self._report("some identifier begin by '<'", kind=2)
            ok &= False
        for i in range(2):
            for itm in id2iter[i].split("<"):
                if not itm:
                    pass
                else:
                    for tit in checker.honorifics.titles:
                        if tit == itm:
                            if i == 1:
                                self._report("Possible unauthorized prefix or suffix in identifier", kind=1)
                            else:
                                self._report("Possible not recommended prefix or suffix in identifier", kind=1)
                            ok &= False if self._compute_warnings else ok
        return self._report("identifier", ok)

    @property
    def document_number(self) -> bool:
        """Return True if the document number format is validated, False otherwise."""

        s = self._document_number
        return self._report("document number format",
                            not check.is_empty(s) and check.is_printable(s) and not check.begin_by(s, "<"))

    @property
    def nationality(self) -> bool:
        """
        Return True if nationality code is validated, False otherwise.

        """
        import mrz.base.countries_ops as chk
        return self._report("valid nationality code", chk.is_code(self._nationality.replace("<", "")))

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
            return self._report("birth date", ok)

    @property
    def sex(self) -> bool:
        """Return True if the sex is "M", "F" or "X", False otherwise."""

        ok = False
        try:
            ok = bool(check.sex(self._sex))
        except ValueError:
            pass
        finally:
            return self._report("valid genre format", ok)

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
            return self._report("expiry date", ok)

    @property
    def optional_data(self) -> bool:
        """Return True if the format of the optional data field is validated, False otherwise."""

        s = self._optional_data
        return True if check.is_empty(s) else self._report("optional data format", check.is_printable(s)
                                                           and not check.begin_by(s, "<"))

    @property
    def optional_data_2(self) -> bool:
        """Return True if the format of the optional data field is validated, False otherwise."""
        s = self._optional_data_2
        return True if check.is_empty(s) else self._report("optional data 2 format", check.is_printable(s)
                                                           and not check.begin_by(s, "<"))

    def _times(self) -> bool:
        birth, expiry = "", ""

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

            rep = lambda s, c, k=2: not c and self._report(s, kind=k)
            rep("expiry date before than birth date", check1)
            # rep("birth date after than today", check2)  # check2 canceled
            self._check_expiry and rep("document expired", check3, 1)
            self._check_expiry and rep("expiry date greater than 10 years", check4, 1)

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

    def __repr__(self) -> str:
        return str(self._all_fields())
