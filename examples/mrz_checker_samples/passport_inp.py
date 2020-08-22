#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mrz.checker.td3 import TD3CodeChecker

td3_check = TD3CodeChecker("P<INPSPECIMEN<<SAMPLE<<<<<<<<<<<<<<<<<<<<<<<\n"
                           "XX000000<0FRA1901012F16073021234567890<<<<70")


print("\n".join(td3_check.report.errors))
