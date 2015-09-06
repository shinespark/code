# -*- coding: UTF-8 -*-
import collections
string = raw_input()
count_dict = collections.Counter(string)

print(count_dict['A'])
