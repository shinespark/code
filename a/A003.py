# coding: utf-8
import sys

# 0: blank, 1: white, 2: black

lines = [x.strip() for x in sys.stdin.readlines()]
max_move_count = int(lines[0])
move_lines = lines[1: 1 + max_move_count]
# move_lines = ['B 6 5', 'W 4 6']
BOARD = []

WHITE = -1
BLANK = 0
BLACK = 1
STONE = {'W': WHITE, 'B': BLACK}

# 初期化
def init():
    global BOARD
    BOARD = [[0 for i in range(8)] for j in range(8)]
    BOARD[3][3] = BOARD[4][4] = WHITE
    BOARD[3][4] = BOARD[4][3] = BLACK

def view():
    for line in BOARD:
        print line
    print ''

def move(stone, x, y):
    global BOARD
    print x, y

    # 石を置く
    BOARD[y][x] = stone

    # ひっくり返す
    reverse(stone, x, y, -1, -1)
    reverse(stone, x, y, -1, 0)
    reverse(stone, x, y, -1, 1)
    reverse(stone, x, y, 0, -1)
    reverse(stone, x, y, 0, 1)
    reverse(stone, x, y, 1, -1)
    reverse(stone, x, y, 1, 0)
    reverse(stone, x, y, 1, 1)

# ひっくり返す処理
def reverse(stone, x, y, dx, dy):
    global BOARD

    reverse_list = []
    _x = x + dx
    _y = y + dy
    reverse_flag = False
    while 0 <= _x <= 7 and 0 <= _y <= 7:
        if BOARD[_y][_x] == BLANK: # 空きマスで終了
            reverse_flag = False
            break
        elif BOARD[_y][_x] == stone: # 同色で終了
            reverse_flag = True
            break
        elif BOARD[_y][_x] == stone * (-1): # 別色ならひっくり返すリストに格納
            reverse_list.append((_y, _x))

        _x += dx
        _y += dy

    # ひっくり返してOKならひっくり返す
    if reverse_flag:
        for masu in reverse_list:
            BOARD[masu[0]][masu[1]] = BOARD[masu[0]][masu[1]] * (- 1)


# ゲーム終了
def gameset():
    black_count = white_count = 0
    for line in BOARD:
        for masu in line:
            if masu == BLACK:
                black_count += 1
            elif masu == WHITE:
                white_count += 1

    print('%d-%d' % (black_count, white_count)),

    if black_count > white_count:
        print('The black won!')
    elif black_count < white_count:
        print('The white won!')
    elif black_count == white_count:
        print('Draw!')



# 棋譜を1手ずつ処理
init()
view()
print 'start'
for line in move_lines:
    splited_line = line.split()
    who = splited_line[0]
    x = int(splited_line[1]) - 1
    y = int(splited_line[2]) - 1

    move(STONE[who], x, y)
    view()

gameset()
