# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]

    count = 0
    for line in lines:
        if line == 'no':
            count += 1

    print count


if __name__ == "__main__":
    main()
