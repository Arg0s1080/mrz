#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from generator.td3 import *
import examples.functions.functions as oi


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

oi.open_image("passports", "Ukraine.png")
