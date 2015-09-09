# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]
splited_first_line = [int(x) for x in lines[0].split()]

max_frame_count, max_pin_count, max_throw_count = splited_first_line
throw_list = lines[1].split()[:max_throw_count]

total_score = 0
strike_flag = spare_flag = False

frame_count = 1
frame_score = 0
score_ques = [] # スペア, ストライク計算用のQue

# ストライク判定
def isStrike(throw_score, throw_count):
    return throw_count == 1 and throw_score == max_pin_count

# スペア判定
def isSpare(frame_score, throw_count):
    return throw_count != 1 and frame_score == max_pin_count

# スコアキューの処理
def handle_score_ques(throw_score):
    global score_ques, total_score
    _score_ques = score_ques
    for i, que in enumerate(score_ques):
        if 'strike' in que:
            if len(que['strike']) < 2:
                _score_ques[i]['strike'].append(throw_score)

            if len(que['strike']) == 2:
                # 足して削除
                strike_sum = sum(que['strike'])
                total_score += strike_sum
                _score_ques.pop(i)

        elif 'spare' in que:
            if len(que['spare']) < 1:
                _score_ques[i]['spare'].append(throw_score)

            if len(que['spare']) == 1:
                # 足して削除
                spare_sum = sum(que['spare'])
                total_score += spare_sum
                _score_ques.pop(i)

    score_ques = _score_ques


# フレームごとに処理
# フレームの初期
throw_count = 1
while max_frame_count >= frame_count: # フレーム
    if len(throw_list) == 0:
        break
    throw_score = throw_list.pop(0)

    # ガーター
    if throw_score == 'G':
        throw_score = 0
    else:
        throw_score = int(throw_score)

    handle_score_ques(throw_score)

    if max_frame_count != frame_count: # 最終フレーム以外
        # ストライク
        if isStrike(throw_score, throw_count):
            total_score += throw_score
            score_ques.append({'strike': []})

            frame_score = 0
            frame_count += 1
            throw_count = 1
            continue

        # スペア
        if isSpare(throw_score, throw_count):
            total_score += throw_score
            score_ques.append({'spare': []})

            frame_score = 0
            frame_count += 1
            throw_count = 1
            continue

        # 通常(1投目: 2投目へ, 2投目: 次のフレームへ)
        if throw_count == 1:
            frame_score += throw_score
            total_score += throw_score
            throw_count += 1
        else:
            frame_score = 0
            total_score += throw_score
            throw_count = 1

    else: # 最終フレーム
        # ストライク
        if isStrike(throw_score, throw_count):
            total_score += throw_score
            score_ques.append({'strike': []})

        # スペア
        if isSpare(throw_score, throw_count):
            total_score += throw_score
            score_ques.append({'spare': []})

        # 通常(1投目: 2投目へ, 2投目: 次のフレームへ)
        if throw_count == 1:
            frame_score += throw_score
            total_score += throw_score
            throw_count += 1
        else:
            frame_score = 0
            total_score += throw_score
            throw_count = 1

print total_score
