# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    mx = 100
    rest = int(lines[0])
    print mx - rest

if __name__ == "__main__":
    main()
