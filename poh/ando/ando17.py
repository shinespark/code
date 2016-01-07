# coding: utf-8


def main():
    n = int(input())
    m = int(input())
    color = {-1: 'R', 1: 'W'}
    c_id = 1
    for i in range(m):
        if i % n == 0:
            c_id *= -1
        print(color[c_id], end='')


if __name__ == "__main__":
    main()
