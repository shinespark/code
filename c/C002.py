# coding: utf-8
nums = [int(x) for x in raw_input().split()]

if nums[0] == nums[1]:
    print('eq')
else:
    print(max(nums))
