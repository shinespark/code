# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    splited_first_line = [int(x) for x in lines[0].split()]
    all_item_num, all_campaign_num = splited_first_line

    item_price_list = [int(x) for x in lines[1: 1 + all_item_num]]
    campaign_price_list = [int(x) for x in lines[1 + all_item_num: 1 + all_item_num + all_campaign_num]]

    pre_combination_price_list = [x + y for x in item_price_list for y in item_price_list]
    combination_price_list = []
    for i, price in enumerate(pre_combination_price_list):
        if i % (all_item_num + 1) == 0:
            continue
        combination_price_list.append(price)

    for campaign_price in campaign_price_list:

        # キャンペーン価格以上の組み合わせがあるかチェック
        none_flag = True
        for combination_price in combination_price_list:
            if campaign_price >= combination_price:
                none_flag = False

        if none_flag:
            print 0
            continue

        # キャンペーン価格との差額リストを生成
        abs_sub_price_list = [abs(campaign_price - x) for x in combination_price_list]

        # 差額が最も小さい金額出力
        print combination_price_list[abs_sub_price_list.index(min(abs_sub_price_list))]

if __name__ == "__main__":
    main()
