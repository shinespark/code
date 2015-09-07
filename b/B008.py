# coding: utf-8
import sys

lines = sys.stdin.readlines()

splited_first_line = [int(x) for x in lines[0].split()]
member_num = splited_first_line[0]
event_num = splited_first_line[1]

profit_lines = lines[1: 1 + event_num]

# 利益が出るイベントのみ加算する
profit = 0
for raw_profit_line in profit_lines:
    profit_line = [int(x) for x in raw_profit_line.split()]

    subtotal = 0
    for member_profit in profit_line[:member_num]:
        subtotal += member_profit

    if subtotal > 0:
        profit += subtotal

print profit
