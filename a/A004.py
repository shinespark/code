# coding: utf-8
import sys


def main():
    lines = [s.strip() for s in sys.stdin.readlines()]
    dummy = '''7 4 5
1 3 1
3 2 2
2 3 5
3 4 4
1 6 6
'''
    lines = [s.strip('\n') for s in dummy.split('\n')]
    L, n, m = [int(s) for s in lines[0].split()]
    m_lines = lines[1: 1 + m]

    # 各横線の接続箇所(ワープ先)を格納した辞書を作る
    connects = {}
    for line in m_lines:
        x, y, y2 = [int(x) for x in line.split()]
        connects[(x, y)] = (x + 1, y2)
        connects[(x + 1, y2)] = (x, y)

    x = 1
    y = L
    while y > 0:
        # ワープ先を取得する or そのまま上る
        x, y = connects.get((x, y), (x, y))
        y -= 1
    print x

if __name__ == "__main__":
    main()
