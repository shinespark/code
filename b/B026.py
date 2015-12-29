# coding: utf-8
import io

coin_list = [500, 100, 50, 10]


def main():
    #  rest = list(map(int, input().split()))
    #  n = int(input())
    #  b = [[int(i) for i in (input.split())] for i in range(n)]
    d = '''5 7 0 9
5
130 1 0 0 0
120 1 0 0 0
180 0 2 0 2
180 0 1 5 3
130 1 0 0 0
'''
    b = io.StringIO(d)
    rest = list(map(int, b.readline().strip().split()))
    n = int(b.readline().strip())
    b = [[int(i) for i in (b.readline().strip().split())] for i in range(n)]

    for b_n in b:
        rest = buy(b_n, rest)


def buy(b_n, rest):
    price = b_n[0]
    pre_rest = [rest[i] + b_n[i + 1] for i in range(len(rest))]
    post = sum([coin_list[i] * v for i, v in enumerate(b_n[1:])])

    # お釣り
    change = post - price
    change_coins = calcChange(change, pre_rest)  # 釣り銭
    if change_coins:
        rest = [pre_rest[i] - change_coins[i] for i in range(len(rest))]
        print(' '.join(map(str, change_coins)))
    else:
        print('impossible')

    return rest


# お釣り出せるかチェック
def calcChange(change, rest):
    pre_change = change
    change_coins = [0] * len(coin_list)

    for i, v in enumerate(coin_list):
        # 50円硬貨, 10円硬貨でお釣り100円以上の場合はNG
        if v == 50 and pre_change >= 100:
            return False

        if rest[i] > 0:
            count = pre_change // v  # 在庫無視の最大硬貨枚数
            if count > rest[i]:  # 在庫考慮
                count = rest[i]

            change_coins[i] = count  # 釣り銭を格納
            pre_change -= v * count

        if pre_change == 0:
            return change_coins

    return False


if __name__ == "__main__":
    main()
    #  print(calcChange(130, [1, 1, 1, 20]))
    #  print(buy([130, 1, 0, 0, 0], [1, 3, 1, 20]))
