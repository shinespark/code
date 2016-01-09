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
    for i in l:
        table[i] = 1

    vector = (1, 0)  # 進行方向
    relative_point = (0, 0)  # 相対進行座標
    next_turn_point = (1, 0)  # 方向転換座標

    t = 0
    _l = [list(x) for x in l]
    print(_l)
    print(table)
    while 1:
        print('')
        print('t', t)

        # 各小人の進行予定座標の計算
        pre_positions = []
        for i in _l:
            if i == ():  # 停止した小人はスルー
                continue

            pre_positions.append((i[0] + vector[0], i[1] + vector[1]))

        # 衝突したら停止
        if isDuplicate(pre_positions):
            for i, v in enumerate(pre_positions):
                for j in range(i, len(pre_positions)):
                    if pre_positions[i] == pre_positions[j]:
                        print('衝突', pre_positions[i])
                        _l[i] = ()  # 停止

        print('pre_positions', pre_positions)
        # 進行
        print('vector', vector)
        print('_l', _l)
        for i, pre_position in enumerate(pre_positions):
            print('pre_position', i, pre_position)
            if _l[i] == ():  #停止した小人はスルー
                continue

            if pre_position in table:
                print('すでにある', pre_position)
                _l[i] = ()  # 停止
            else:
                table[pre_position] = 1
                _l[i] = pre_position
        print('_l', _l)

        # 次のvector計算
        relative_point = (relative_point[0] + vector[0], relative_point[1] + vector[1])

        # 方向転換ポイントなら進行座標を変更する
        if relative_point == next_turn_point:
            next_turn_point, vector = fetchNextTurnPointAndVector(next_turn_point, vector)

        t += 1
        print('t, table', t, table)
        if len(_l) == 0:
            print('t, table', t, table)
            break

        if t == 30:
            break


# 衝突チェック
def isDuplicate(pre_positions):
    return len(pre_positions) != len(set(pre_positions))


# 次の方向転換座標を取得
def fetchNextTurnPointAndVector(next_turn_point, vector):
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


if __name__ == "__main__":
    main()
    #  print(fetchNextTurnPoint(5, 0))
