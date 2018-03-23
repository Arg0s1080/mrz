#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import examples.functions.functions as oi
from mrz.generator.td2 import TD2CodeGenerator

print(TD2CodeGenerator("I",
                       "Utopia",
                       "ERIKSSON",
                       "ANNA MARIA",
                       "D23145890",
                       "UTO",
                       "740812",
                       "F",
                       "120415"))

oi.open_image("other", "TD2_ICAO_Example.png")
