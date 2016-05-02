# coding: utf-8


def main():
    l = [[int(i) for i in (input().split())] for i in range(3)]

    if l[0] == l[1] == l[2]:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
