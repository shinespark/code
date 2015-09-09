# coding: utf-8
import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    # dummy = '''B 7
# 86 36 55 88 10 82 53 107 83 22 15
# 69 38 48 73 21 50 27 1 41 24 103'''
    # lines = [x.strip('\n') for x in dummy.split('\n')]

    splited_first_line = [x for x in lines[0].split()]
    pass_team= splited_first_line[0]
    pass_player= int(splited_first_line[1]) - 1

    players = {'A': [int(x) for x in lines[1].split()], 'B': [int(x) for x in lines[2].split()]}

    offside_players = []

    # パスプレイヤーの座標を取得する
    pass_player_coodinate = players[pass_team][pass_player]

    # オフサイド座標の取得
    if pass_team == 'A':
        offside_coodinate = sorted(players['B'], reverse=True)[1]
    elif pass_team == 'B':
        offside_coodinate = sorted(players['B'])[1]

    # パスプレイヤーより前にいて、
    # かつ敵チームのゴールラインから2人目の敵チーム選手よりもゴールラインに近くて、
    # かつ敵チーム座標に居るプレイヤーを取得する
    for player, player_coodinate in enumerate(players[pass_team]):
        if pass_team == 'A':
            if pass_player_coodinate < player_coodinate and offside_coodinate < player_coodinate and 55 <= player_coodinate <= 110:
                offside_players.append(player)

        elif pass_team == 'B':
            if player_coodinate < pass_player_coodinate and player_coodinate < offside_coodinate and 0 <= player_coodinate <= 55:
                offside_players.append(player)

    if offside_players == []:
        print 'None'
    else:
        for player in offside_players:
            print player + 1


if __name__ == "__main__":
    main()
