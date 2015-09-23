# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    #  dummy = '''3
#  1 1024
#  11 2048
#  21 4196
#  '''
    #  lines = [x.strip('\n') for x in dummy.split('\n')]

    receipt_lines = lines[1: 1 + int(lines[0])]

    point = 0
    for line in receipt_lines:
        day, money = [int(x) for x in line.split()]
        day = str(day)

        if '3' in day:
            point += int(money * 0.03)
        elif '5' in day:
            point += int(money * 0.05)
        else:
            point += int(money * 0.01)

    print point

if __name__ == "__main__":
    main()
