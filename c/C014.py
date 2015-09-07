# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]
first_line = [int(x) for x in lines[0].split()]

box_num = first_line[0]
ball_accross = first_line[1] * 2

box_lines = lines[1: 1 + box_num]

for i, box_line in enumerate(box_lines, 1):
    box_sizes = [int(x) for x in box_line.split()]
    h = box_sizes[0]
    w = box_sizes[1]
    d = box_sizes[2]

    if h >= ball_accross and w >= ball_accross and d >= ball_accross:
        print i
