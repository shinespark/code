# coding: utf-8
import math


def main():
    m = int(input())
    n = int(input())
    l = [[int(i) for i in input().split()] for i in range(n)]

    c = {}
    for i in l:
        c[i[0]] = c.get(i[0], 0) + i[2]

    r = 0
    for v in c.values():
        r += math.ceil(v / m)

    print(r)


if __name__ == "__main__":
    main()
