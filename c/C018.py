# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]

foodstuff_max_num = int(lines[0])
foodstuffs = lines[1: 1 + foodstuff_max_num]

your_foodstuff_max_num = int(lines[1 + foodstuff_max_num])
your_foodstuffs = lines[2 + foodstuff_max_num: 2 + foodstuff_max_num + your_foodstuff_max_num]

def dicted(lines):
    d = {}
    for line in lines:
        name, value = line.split()
        d[name] = int(value)
    return d

def isOver(your_foodstuff_d):
    for k, v in recipe_d.iteritems():
        if v > your_foodstuff_d[k]:
            return True

    return False

def reduce(your_foodstuff_d):
    for k, v in recipe_d.iteritems():
        your_foodstuff_d[k] -= v

    return your_foodstuff_d


# レシピの必要食材を辞書化
recipe_d = dicted(foodstuffs)
recipe_set = set(recipe_d.keys())

# 所有食材を辞書化
your_foodstuff_d = dicted(your_foodstuffs)

# 所有食材から調理可能な人数を計算
serve_count = 0
while True:
    # そもそも食材揃ってなければ終了
    your_foodstuff_set = set(your_foodstuff_d.keys())
    if len(recipe_set & your_foodstuff_set) != len(recipe_set):
        print serve_count
        sys.exit()

    # 材料足りてなかったら終了
    if isOver(your_foodstuff_d):
        print serve_count
        sys.exit()

    # 揃っていれば減算してインクリメント
    your_foodstuff_d = reduce(your_foodstuff_d)
    serve_count += 1
