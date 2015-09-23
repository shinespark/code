# coding: utf-8


def main():
    #  input_num = raw_input().strip()
    input_num = '16'

    number_display = {
        0: '1111110',
        1: '0110000',
        2: '1101101',
        3: '1111001',
        4: '0110011',
        5: '1011011',
        6: '1011111',
        7: '1110000',
        8: '1111111',
        9: '1111011'
    }

    # まず各数字ごとの変化セットを作る
    add_number_display = {}  # 1本足したら出来る数字セット
    for num in range(10):
        for elem in range(7):
            if number_display[num][elem] == '1':  # 元々1ならスルー
                continue

            number_display_list = list(number_display[num])
            number_display_list[elem] = '1'
            _number_display = ''.join(number_display_list)

            for number, number_value in enumerate(number_display.values()):

                if _number_display == number_value:
                    if num not in add_number_display:
                        add_number_display[num] = []
                    add_number_display[num].append(number)

    print add_number_display

    sub_number_display = {}  # 1本足したら出来る数字セット
    for num in range(10):
        for elem in range(7):
            if number_display[num][elem] == '0':  # 元々0ならスルー
                continue

            number_display_list = list(number_display[num])
            number_display_list[elem] = '0'
            _number_display = ''.join(number_display_list)

            for number, number_value in enumerate(number_display.values()):

                if _number_display == number_value:
                    if num not in sub_number_display:
                        sub_number_display[num] = []

                    sub_number_display[num].append(number)

    print sub_number_display

    same_number_display = {}  # 自身を組み替えてできる数字セット
    for num in range(10):
        for elem in range(7):
            if number_display[num][elem] == '0':  # 元々0ならスルー
                continue

            number_display_list = list(number_display[num])
            number_display_list[elem] = '0'

            for i, char in enumerate(number_display[num]):
                if elem == i:  # 同じ位置はスルー
                    continue

                if number_display_list[i] == '1':  # 最初から1のものはスルー
                    continue

                _number_display_list = number_display_list
                _number_display_list[i] = '1'
                _number_display = ''.join(_number_display_list)

                for number, number_value in enumerate(number_display.values()):

                    if _number_display == number_value:
                        if num not in same_number_display:
                            same_number_display[num] = []

                        same_number_display[num].append(number)

    print same_number_display

    combination_list = []
    combination_num_base = list(input_num)
    # 1文字目を-1, 2文字目を+1, 3文字目そのまま... でパターンを作っていく
    for i, char in enumerate(input_num):
        # 1文字目が-1, +-0 不可であれば次へ
        if char not in sub_number_display and char not in same_number_display:
            continue

        # 同じ数値の組み換え
        if char in same_number_display:
            for same_char in same_number_display:
                combination_num = combination_num_base
                combination_num[i] = same_char
                combination_list.append(''.join(combination_num))

        # 1文字目が-1本可能であれば, その組み合わせ数分combination_listに追加する
        for sub_char in sub_number_display[char]:
            for j, other_char in enumerate(input_num):
                if i == j:
                    continue

                if other_char in add_number_display:
                    for add_char in add_number_display[other_char]:
                        combination_num = combination_num_base
                        combination_num[i] = sub_char
                        combination_num[j] = add_char

                        combination_list.append(''.join(combination_num))

    print combination_list
    print sorted(set(combination_list))

if __name__ == "__main__":
    main()
