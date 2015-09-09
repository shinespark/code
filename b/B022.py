# coding: utf-8
import sys

# 初期化
def make_support_d(candidate_num, citizen_num):
    support_d = {
        0: citizen_num
    }

    # 空配列の作成
    for i in range(candidate_num, 1):
        support_d[i] = 0

    return support_d

# スピーチ実行
def speech(support_d, candidate_id):
    new_support_d = {}

    get_citizen_count = 0
    for k, v in support_d.iteritems():
        # 他支持層からの減算
        if k != candidate_id:
            if v > 0:
                get_citizen_count += 1
                new_support_d[k] = v - 1
            else:
                new_support_d[k] = 0
        # 既存支持者の加算
        else:
            get_citizen_count += v

    # スピーチ実行者のキー格納
    new_support_d[candidate_id] = get_citizen_count

    return new_support_d

# メイン関数
def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    splited_first_line = [int(x) for x in lines[0].split()]

    candidate_num, citizen_num, speech_num = splited_first_line
    speech_lines = lines[1: 1 + speech_num]

    support_d = make_support_d(candidate_num, citizen_num)

    for line in speech_lines:
        candidate_id = int(line)
        support_d = speech(support_d, candidate_id)

    # 最も支持者の多い候補者の取得
    support_d.pop(0) # 無支持層の削除
    max_support_num = max(support_d.values())
    for k, v in support_d.iteritems():
        if v == max_support_num:
            print k


if __name__ == "__main__":
    main()
