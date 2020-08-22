# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

import mrz.base.string_checkers as check

from mrz.checker.td3 import *
from mrz.checker._honorifics import titles
from mrz.checker._report import Kind
from mrz.base.functions import hash_is_ok
from string import ascii_uppercase


class PassportINDCodeChecker(TD3CodeChecker):

    @property
    def optional_data_hash(self) -> bool:
        """Return True if hash of optional data is True, False otherwise."""
        if check.is_empty(self._optional_data) and self._optional_data_hash == "<":
            ok = True
        else:
            ok = hash_is_ok(self._optional_data, self._optional_data_hash)
        return self.report.add("optional data hash", ok)

    @property
    def identifier(self) -> bool:
        """Return True is the identifier is validated overcoming the checks, False otherwise."""
        full_id = self._identifier.rstrip("<")
        padding = self._identifier[len(full_id):]
        id2iter = full_id.lstrip("<<").split("<<") if full_id[2] in ascii_uppercase else full_id.split("<<")
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
            if False and not full_id.startswith("<<"):
                self.report.add("identifier doesn't starts with '<<'", level=Kind.ERROR)
                ok = False
                # If you want to report as a warning instead of as an error uncomment lines below
                # self._report("identifier doesn't starts with '<<'", kind=1)
                # ok = False if self._compute_warnings else ok
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
        return self.report.add("identifier", ok)



