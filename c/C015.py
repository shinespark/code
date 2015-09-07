# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]

max_num = int(lines[0])
receipt_lines = lines[1: 1 + max_num]

# receiptごとに処理
points = 0
for receipt_line in receipt_lines:
    splited_receipt_line = receipt_line.split()
    date = splited_receipt_line[0]
    value = int(splited_receipt_line[1])

    if date.find('3') >= 0:
        points += int(value * 0.03)
    elif date.find('5') >= 0:
        points += int(value * 0.05)
    else:
        points += int(value * 0.01)

print points
