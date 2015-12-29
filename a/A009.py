# coding: utf-8


def main():
    h, w = map(int, input().split())
    box = [input() for i in range(h)]
    vector = [1, 0]  # 方向(加算数値), 初期値は右へ
    x = y = 0  # 座標

    # 脱出するまで
    count = 0
    while 1:
        count += 1

        point = box[y][x]
        if point == '\\':
            vector = [vector[1], vector[0]]
        elif point == '/':
            vector = [vector[1] * - 1, vector[0] * - 1]

        x, y = x + vector[0], y + vector[1]

        if x < 0 or w <= x or y < 0 or h <= y:
            break

    print(count)


if __name__ == "__main__":
    main()
