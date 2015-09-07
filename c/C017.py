# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]
splited_first_line = [int(x) for x in lines[0].split()]

parent_a, parent_b = splited_first_line
children_num = int(lines[1])
children_lines = lines[2: 2 + children_num]

# 子カードごとに
for child_line in children_lines:
    child_a, child_b = [int(x) for x in child_line.split()]

    if parent_a > child_a:
        print('High')
    elif parent_a == child_a:
        if parent_b < child_b:
            print('High')
        else:
            print('Low')
    else:
        print('Low')
