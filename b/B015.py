# coding: utf-8
import sys
import re


def main():
    lines = [re.sub(r' ', '', x.strip()) for x in sys.stdin.readlines()]
    dummy = '''0 0 0 0 1 1 0
1 1 0 1 1 1 1'''
    lines = [re.sub(r' ', '', x.strip()) for x in dummy.split('\n')]
    number_display = [
        '1111110',
        '0110000',
        '1101101',
        '1111001',
        '0110011',
        '1011011',
        '1011111',
        '1110010',
        '1111111',
        '1111011'
    ]

    correct_flag = 'Yes'
    mirror_correct_flag = 'Yes'
    turn_correct_flag = 'Yes'

    for line in lines:

        # そのままチェック
        if line not in number_display:
            correct_flag = 'No'

        # 線対称チェック
        mirror_num = line[0] + line[5] + line[4] + line[3] + line[2] + line[1] + line[6]
        if mirror_num not in number_display:
            mirror_correct_flag = 'No'

        # 点対称チェック
        turn_num = line[3] + line[4] + line[5] + line[0] + line[1] + line[2] + line[6]
        if turn_num not in number_display:
            turn_correct_flag = 'No'

    print correct_flag
    print mirror_correct_flag
    print turn_correct_flag


if __name__ == "__main__":
    main()
