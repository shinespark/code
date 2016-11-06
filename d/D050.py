# coding: utf-8


def main():
    li = [int(i) for i in input().strip().split()]

    s = 0
    for l in li:
        if l > 5:
            l = 5
        s += l
    print(s)

if __name__ == "__main__":
    main()
