# coding: utf-8
import sys

s = raw_input().strip()

leet = {
    'A': '4',
    'E': '3',
    'G': '6',
    'I': '1',
    'O': '0',
    'S': '5',
    'Z': '2',
}

for char in s:
    if char in leet:
        sys.stdout.write(leet[char])
    else:
        sys.stdout.write(char)
