#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from checker.td3 import TD3CodeChecker


print(TD3CodeChecker("P<CANMARTIN<<SARAH<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
                     "ZE000509<9CAN8501019F2301147<<<<<<<<<<<<<<08",
                     check_expiry=True,
                     compute_warnings=True))
