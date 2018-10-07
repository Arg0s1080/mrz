#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.checker.td1 import TD1CodeChecker

mrz_td1 = ("I<BAD<BAD<<<<<0<<<<<<BAD<<<<<<\n"
           "0105998<0512868BAD<<<<BAD<<<<0\n"
           "<SPECIMEN1<<SPECIMEN2<<BAD<<<<")

td1_check = TD1CodeChecker(mrz_td1)

assert bool(td1_check) is False
