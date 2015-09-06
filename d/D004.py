# -*- coding: UTF-8 -*-
import sys
lines = sys.stdin.readlines()

count = int(lines[0])
print('Hello '),
for line in lines[1:count]:
    sys.stdout.write(line.strip() + ',')

sys.stdout.write(lines[count].strip() + '.')
