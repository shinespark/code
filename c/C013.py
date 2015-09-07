# coding: utf-8
import sys

lines = sys.stdin.readlines()

dislike_num_set = set(lines[0].strip())
room_max_num = int(lines[1])
room_nums = [x.strip() for x in lines[2: 2 + room_max_num]]

enable_flag = False
for room_num in room_nums:
    room_num_set = set(room_num)

    if len(dislike_num_set & room_num_set) == 0:
        print room_num
        enable_flag = True


if not enable_flag:
    print 'none'
