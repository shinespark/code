# coding: utf-8


def main():
    magic_num = 21
    n = int(input())

    d = magic_num % n
    if d == 0:
        print(n)
    else:
        print(d)

if __name__ == "__main__":
    main()
