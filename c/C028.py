# coding: utf-8


def main():
    n = int(input())
    l = [[i for i in (input().split())] for i in range(n)]

    score = 0
    for i in l:
        if i[0] == i[1]:
            score += 2
        elif len(i[0]) != len(i[1]):
            continue
        else:
            diff = 0
            for j in range(len(i[0])):
                if i[0][j] != i[1][j]:
                    diff += 1

            if diff == 1:
                score += 1

    print(score)


if __name__ == "__main__":
    main()
