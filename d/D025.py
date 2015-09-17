# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    first_line = int(lines[0])
    print('%03d' % first_line)

if __name__ == "__main__":
    main()
