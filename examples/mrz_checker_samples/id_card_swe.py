#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append(sys.path[0].replace("examples/mrz_checker_samples", ""))
from checker.td1 import TD1CodeChecker

print(bool(TD1CodeChecker("I<SWE59000002<8198703142391<<<\n"
                          "8703145M1701027SWE<<<<<<<<<<<8\n"
                          "SPECIMEN<<SVEN<<<<<<<<<<<<<<<<")))
