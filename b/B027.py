# coding: utf-8


def main():
    h, w, n = map(int, input().split())
    t = [[int(i) for i in (input().split())] for i in range(h)]
    c = int(input())
    a = [[int(i) - 1 for i in (input().split())] for i in range(c)]

    p = 0 # 操作プレイヤー
    r = {}
    for i in a:
        r1, r2 = t[i[0]][i[1]], t[i[2]][i[3]] # めくったカード
        if r1 == r2:
            r[p] = r.get(p, 0) + 2
        else:
            p = (p + 1) % n

    for i in range(n):
        print(r.get(i, 0))


if __name__ == "__main__":
    main()
