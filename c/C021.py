# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]
xc, yc, r_1, r_2 = [int(x) for x in lines[0].split()]

check_max_num = int(lines[1])
check_lines = lines[2: 2 + check_max_num]

def isBofu(x, y):
    if r_1 ** 2 <= (x - xc) ** 2 + (y - yc) ** 2 <= r_2 ** 2:
        return True
    else:
        return False

for line in check_lines:
    x, y = [int(x) for x in line.split()]
    if isBofu(x, y):
        print('yes')
    else:
        print('no')
