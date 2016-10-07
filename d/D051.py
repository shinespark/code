# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
from collections import Counter

input_lines = input()
counter = Counter(input_lines.split())

if counter['W'] >= 5:
    print('OK')
else:
    print('NG')
