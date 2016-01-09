# coding: utf-8
import io


def main():
    #  n = int(input())
    #  l = [[int(i) for i in (input().split())] for i in range(n)]
    d = '''3
-1 2
3 -1
-2 -2
'''
    b = io.StringIO(d)
    n = int(b.readline().strip())
    l = [tuple(int(i) for i in (b.readline().strip().split())) for i in range(n)]
    print(n, l)

    # init
    table = {}
    dwarfs = []
    for i, v in enumerate(l):
        table[v] = 1
        dwarfs.append(Dwarf(i, v))
        print(dwarfs[i].position)

    t = 0
    while 1:
        pre_positions = []
        for dwarf in dwarfs:
            if dwarf.is_move:


        t += 1
        if t > 10:
            break


class Dwarf:
    def __init__(self, i, position):
        self.id = i
        self.is_move = True
        self.position = position
        self.vector = (1, 0)
        self.next_turn_point = (1, 0)

    def move():  # 次の座標へ移動する
        pass

    def fetchNextTurnPointAndVector(next_turn_point, vector):  # 次の方向転換座標を取得
        x, y = next_turn_point
        if vector == (1, 0):  # 右 to 上
            next_turn_point = x, - x
        elif vector == (0, -1):  # 上 to 左
            next_turn_point = y, y
        elif vector == (-1, 0):  # 左 to 下
            next_turn_point = x, - y
        else:  # 下 to 右
            next_turn_point = y + 1, y

        return (next_turn_point, (vector[1], - vector[0]))


# 衝突チェック
def isDuplicate(pre_positions):
    return len(pre_positions) != len(set(pre_positions))


if __name__ == "__main__":
    main()
