# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]
day_max = int(lines[0])
day_lines = lines[1: 1 + day_max]

n_start = n_end = n_high = 0
n_low = sys.maxint

# 各行ごとにチェック
for i, line in enumerate(day_lines, 1):
    start, end, high, low = [int(x) for x in line.split()]

    if i == 1:
        n_start = start

    if i == day_max:
        n_end = end

    n_high = max(n_high, high)
    n_low = min(n_low, low)

print n_start, n_end, n_high, n_low
