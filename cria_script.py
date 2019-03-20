#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import csv
import os


def lookahead(iterable):
    it = iter(iterable)
    last = next(it)  # next(it) in Python 3
    for val in it:
        yield last, False
        last = val
    yield last, True


files = [f for f in os.listdir('C:\\tmp\\TabUnificada')]
for f in files:
    if f.endswith('_layout.txt'):
        print()
        with open('C:\\tmp\\TabUnificada\\' + f, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            linhas = list(spamreader)[1:]
            print('create table sigtap.' + f[:-11] + ' (')
            for row, last in lookahead(linhas):
                if last:
                    print('    ' + row[0] + ' ' + row[4] + "(" + row[1] + ")")
                else:
                    print('    ' + row[0] + ' ' + row[4] + "(" + row[1] + "),")

            print(");")
