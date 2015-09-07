# coding: utf-8
import sys

lines = sys.stdin.readlines()
atari = [int(x) for x in lines[0].split()]
atari_set = set(atari)

sheet_num = int(lines[1])
sheets = lines[2: 2 + sheet_num]

for sheet_line in sheets:
    sheet = [int(x) for x in sheet_line.split()]
    sheet_set = set(sheet)

    print (len(atari_set & sheet_set))
