#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import *
from examples.functions.functions import open_image


print(PassportCodeGenerator(
        "P",
        "UKRAINE",
        "ТКАЧЕНКО",
        "МАР'ЯНА",
        "XX000000",
        "UKRAINE",
        "910824",
        "F",
        "230925",
        "1234567890",
        dictionary.cyrillic_ukrainian()))

open_image("passports", "Ukraine.png")
