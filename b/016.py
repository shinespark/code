# coding: utf-8
import sys


def get_point(line):
    return int(line[2])


def main():
    #  lines = [x.strip() for x in sys.stdin.readlines()]
    dummy = '''7 6 2
3 4
U 17
R 2'''
    lines = [x.strip('\n') for x in dummy.split('\n')]
    width, height, log_count = [int(x) for x in lines[0].split()]
    x, y = [int(x) for x in lines[1].split()]
    log_lines = lines[2: 2 + log_count]

    for line in log_lines:
        if line.find('L') == 0:
            x -= get_point(line)
            if x < 0:
                x += width
        elif line.find('R') == 0:
            x += get_point(line)
            if x >= width:
                x %= width
        elif line.find('D') == 0:
            y -= get_point(line)
            if y < 0:
                y += height
        elif line.find('U') == 0:
            y += get_point(line)
            if y >= height:
                y %= height

    print x, y


if __name__ == "__main__":
    main()
