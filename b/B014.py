# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    #  dummy = '''5 5 5
#  #####
#  #####
#  #####
#  #####
#  #####
#  --
#  #####
#  #...#
#  #...#
#  #...#
#  #####
#  --
#  #####
#  #...#
#  #...#
#  #...#
#  #####
#  --
#  #####
#  #...#
#  #...#
#  #...#
#  #####
#  --
#  #####
#  #####
#  #####
#  #####
#  #####
#  --'''
    #  lines = [x.strip('\n') for x in dummy.split('\n')]
    depth, width, height = [int(x) for x in lines[0].split()]

    block = [['.' for y in range(width)] for z in range(height)]

    for i, line in enumerate(lines[1:], 1):
        if i % (depth + 1) == 0:
            continue

        for j, char in enumerate(line):
            if char == '#':
                block[i / (depth + 1)][j] = '#'

    for line in reversed(block):
        print ''.join(line)


if __name__ == "__main__":
    main()
