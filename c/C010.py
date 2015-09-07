# coding: utf-8
import sys

lines = sys.stdin.readlines()
first_line = lines[0].split()

base_x = int(first_line[0])
base_y = int(first_line[1])
base_r = int(first_line[2])
square_r = pow(base_r, 2)

tree_num = int(lines[1])
trees = lines[2: 2 + tree_num]

for tree in trees:
    splited_line = tree.split()
    tree_x = int(splited_line[0])
    tree_y = int(splited_line[1])

    if pow(base_x - tree_x, 2) + pow(base_y - tree_y, 2) >= square_r:
        print('silent')
    else:
        print('noisy')
