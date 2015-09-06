# -*- coding: UTF-8 -*-

import sys

s = 180
lines = sys.stdin.readlines()

for line in lines:
    s -= int(line)

print(s)
