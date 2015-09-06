# coding: utf-8
import sys
import math

lines = sys.stdin.readlines()
count = int(lines[0])
water = 0.0
coffee = 0.0

for line in lines[1:]:
    line_list = line.split()

    code = int(line_list[0])
    gram = int(line_list[1])

    if code == 1:
        water += gram
    elif code == 2:
        coffee += gram
    elif code == 3:
        s = water + coffee
        water -= gram * water / s
        coffee -= gram * coffee / s

s = water + coffee
print(int(math.floor((coffee / s) * 100)))
