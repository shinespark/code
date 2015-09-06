# coding: utf-8
import sys

lines = sys.stdin.readlines()

masu_length = int(lines[0]) - 1
masu_values = lines[1].split()
deme_count = int(lines[2])
deme_list = lines[3: 3 + deme_count]

def get_masu_value(elem):
    return int(masu_values[elem])

def isOver(new_masu):
    return new_masu > masu_length

def isLoop(loopCount):
    return loopCount >= 10

def isGoal(new_masu):
    return (new_masu == masu_length)

def isZero(new_masu):
    return get_masu_value(new_masu) == 0

def shake(now_masu, step, loopCount = 0):
    # マス超えてないか
    if isOver(now_masu + step):
        return('No')

    # 次のマスを見る
    new_masu = now_masu + step
    new_masu_value = get_masu_value(new_masu)

    # ループ判定
    if isLoop(loopCount):
        return('No')

    # ゴール判定
    if isGoal(new_masu):
        return('Yes')

    # 0マス判定
    if isZero(new_masu):
        return('No')

    loopCount += 1
    return shake(new_masu, int(new_masu_value), loopCount)


# 出目ごとにチェック
for i in deme_list:
    # 初期値
    result = shake(0, int(i))
    print(result)
