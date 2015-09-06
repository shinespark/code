# -*- coding: UTF-8 -*-
import sys

l = []
for line in sys.stdin.readlines():
    l.append(int(line))

print(max(l))
print(min(l))
