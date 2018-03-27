#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td2 import TD2CodeGenerator
from examples.functions.functions import open_image

print(TD2CodeGenerator("I",
                       "Utopia",
                       "ERIKSSON",
                       "ANNA MARIA",
                       "D23145890",
                       "UTO",
                       "740812",
                       "F",
                       "120415"))

open_image("other", "TD2_ICAO_Example.png")
