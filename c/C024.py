# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]
command_max = int(lines[0])
command_lines = lines[1: 1 + command_max]

var = {'1': 0, '2': 0}

# コマンド操作関数
def command(line):
    command_name = line.split()[0]
    if command_name == 'SET':
        set_var, set_val = line.split()[1:]
        var[set_var] = int(set_val)
    elif command_name == 'ADD':
        var['2'] = var['1'] + int(line.split()[1])
    elif command_name == 'SUB':
        var['2'] = var['1'] - int(line.split()[1])

for line in command_lines:
    ccommand(line)

# 結果出力
print var['1'], var['2']
