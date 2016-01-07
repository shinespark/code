# coding: utf-8
from collections import Counter
l = [input() for i in range(5)]
count = Counter()
for w in l:
    count[w] += 1
print(count.most_common(1)[0][0])
