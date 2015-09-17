# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    dummy = '''5
091180422478189X
774123801013511X
973736969204716X
793180803472918X
358682935182058X
670891979616350X'''
    lines = [x.strip('\n') for x in dummy.split('\n')]
    card_line_num = int(lines[0])
    card_lines = lines[1: 1 + card_line_num]

    for line in card_lines:
        card_num = list(line[::-1])

        # 'x'を0に仮置き
        card_num[0] = 0
        # even = sum([int(x) * 2 if int(x) * 2 / 10 == 0 else (int(x) * 2 % 10 + int(x) * 2 / 10) for x in card_num[1::2]])
        even = sum([x if x / 10 == 0 else (x % 10 + x / 10) for x in [int(x) * 2 for x in card_num[1::2]]])
        odd = sum([int(x) for x in card_num[0::2]])

        for i in range(10):
            if (even + odd + i) % 10 == 0:
                print i



if __name__ == "__main__":
    main()
