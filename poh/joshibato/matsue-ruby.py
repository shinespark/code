# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    dummy = '''11
sk
nw
jx
ob
oo
xj
uh
rn
wn
hu
nr
'''
    lines = [x.strip('\n') for x in dummy.split('\n')]

    word_num = int(lines[0])
    word_list = lines[1: 1 + word_num]

    match_word_list = []  # マッチする反転文字列がある単語
    mirror_word_list = []  # 自身で回文として成立する単語

    for word in word_list:
        # 反転文字列があるか調査
        mirror_word = word[::-1]

        if word == mirror_word:
            mirror_word_list.append(word)
            continue

        for _word in word_list:
            if mirror_word == _word:
                match_word_list.append(word)
                continue

    match_word_list = sorted(match_word_list)
    mirror_word_list = sorted(mirror_word_list)

    # 回文作成
    mirror_sentence = ''
    for i in range(len(match_word_list) / 2):
        word = match_word_list.pop(0)
        mirror_word = word[::-1]

        mirror_sentence += word
        match_word_list.remove(mirror_word)  # 使用した単語と対応する反転単語を削除

    mirror_sentence += mirror_word_list.pop(0) + mirror_sentence[::-1]

    print mirror_sentence

if __name__ == "__main__":
    main()
