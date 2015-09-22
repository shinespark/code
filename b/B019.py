# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    #  dummy = '''6 3
#  1 2 3 4 5 6
#  1 2 3 4 5 6
#  1 2 3 4 5 6
#  4 5 6 1 2 3
#  4 5 6 1 2 3
#  4 5 6 1 2 3
#  '''
    #  lines = [x.strip('\n') for x in dummy.split('\n')]
    n, k = [int(x) for x in lines[0].split(' ')]
    pixel_lines = lines[1: 1 + n]

    sum_pixel_block = [[0 for x in range(n / k)] for y in range(n / k)]
    for i, line in enumerate(pixel_lines):
        for j, value in enumerate(line.split(' ')):
            sum_pixel_block[i/k][j/k] += int(value)

    new_pixel_block = [[0 for x in range(n / k)] for y in range(n / k)]
    for i, line in enumerate(new_pixel_block):
        for j, value in enumerate(line):
            new_pixel_block[i][j] = sum_pixel_block[i][j] / k ** 2

    for line in new_pixel_block:
        print ' '.join(map(str, line))

if __name__ == "__main__":
    main()
