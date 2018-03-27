#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
sys.path.append(sys.path[0].replace("examples/mrz_checker_samples", ""))
from mrz.checker.td1 import TD1CodeChecker

print(TD1CodeChecker("IDESPBAA000589599999999R<<<<<<\n"
                     "8001014F2501017ESP<<<<<<<<<<<7\n"
                     "ESPANOLA<ESPANOLA<<CARMEN<<<<<"))

