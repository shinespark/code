# coding: utf-8


def main():
    n, s, p = map(int, input().split())
    l = [[int(i) for i in (input().split())] for i in range(n)]
    for i, e in enumerate(l[:]):
        l[i].append(i + 1)

    l = sorted(l, key=lambda l: l[2])
    l = sorted(l, key=lambda l: l[0], reverse=True)

    for i in l:
        g = i[1]
        if s - p <= g <= s + p:
            print(i[2])
            return

    print('not found')

if __name__ == "__main__":
    main()
