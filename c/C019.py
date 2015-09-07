# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]

num_count = int(lines[0])
target_lines = lines[1: 1 + num_count]


def getDivisior(num):
    l = [1]
    for i in range(2, num + 1 // 2):
        if num % i == 0:
            l.append(i)

    return l

def checkPerfectNumber(num):
    divisior = getDivisior(num)

    s = sum(divisior)

    if num == s :
        return 'perfect'
    elif abs(num - s) == 1:
        return 'nearly'
    else:
        return 'neither'


# 各ターゲットごとに求める
for line in target_lines:
    target_num = int(line)
    print checkPerfectNumber(target_num)
