# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    pocket_num, card_num = [int(x) for x in lines[0].split()]
    # pocket_num, card_num = [157, 1518]

    # 奇数 or 偶数ページ?
    is_odd = ((card_num - 1) / pocket_num % 2 == 0)

    # 何ページ目?
    page_num = ((card_num - 1) / pocket_num) + 1

    # ページ内の何番目か(0始まり)
    num_in_page = (card_num - 1) % pocket_num

    back_number = 0

    if is_odd:
        back_page_start_num = page_num * pocket_num + 1
    else:
        back_page_start_num = page_num * pocket_num + 1 - pocket_num * 2

    back_number_list = range(back_page_start_num, back_page_start_num + pocket_num)
    back_number_list.reverse()
    back_number = back_number_list[num_in_page]

    print back_number

if __name__ == "__main__":
    main()
