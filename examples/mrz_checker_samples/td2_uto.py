#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Adding mrz to PYTHONPATH to execute this example as script
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
#############################################################

from mrz.checker.td2 import TD2CodeChecker

print(TD2CodeChecker("I<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<\n"
                     "D231458907UTO7408122F1204159<<<<<<<6"))
