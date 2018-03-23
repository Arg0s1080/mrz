#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td1 import TD1CodeGenerator
from mrz.checker.td1 import TD1CodeChecker
import examples.functions.functions as functions

mrz = str(TD1CodeGenerator("I", "LTU", "11810187", "681123", "F", "300101", "LTU", "BASANAVIČIENĖ", "BIRUTĖ",
                           "46411231034"))

td1_check = TD1CodeChecker(mrz)
print(td1_check)
