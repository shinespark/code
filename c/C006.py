# coding: utf-8
import sys

lines = sys.stdin.readlines()

first_line_elems = lines[0].split()
item_count = int(first_line_elems[0])
user_count = int(first_line_elems[1])
rank_count = int(first_line_elems[2])

item_scores = lines[1].split()

result = []
for line in lines[2: user_count+2]:
    score = 0.0
    line_elems = line.split()

    for i, x in enumerate(line_elems[0: item_count]):
        score += float(x) * float(item_scores[i])

    result.append(int(round(score)))

result.sort()
result.reverse()
for i in result[0: rank_count]:
    print i
