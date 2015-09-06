# coding: utf-8
import sys

def output(flag):
    print(str(flag))

lines = sys.stdin.readlines()

count = int(lines[0])

for address in lines[1:count + 1]:
    flag = True
    l = address.strip().split('.')

    if len(l) != 4:
        flag = False

    for num in l:
        if num.isdigit() and int(num) not in range(0,255):
            flag = False
            break

    output(flag)
