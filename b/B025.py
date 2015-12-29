# coding: utf-8


def main():
    n, m, k = map(int, input().split())
    r = [int(input()) for i in range(m)]

    # init
    bush = {}
    for i in range(1, n + 1):
        bush[i] = 0


    # set
    num = 1
    for i in r:
        bush[i] = num
        num += 1

    # round
    for i in range(k):

        # each round
        rabbit_num = 1

        for j in range(m):
            # each rabbit
            rabbit_place = {v: k for k, v in bush.items()}[rabbit_num]
            pre_rabbit_place = rabbit_place + 1
            while 1:

                if pre_rabbit_place >= n + 1:
                    pre_rabbit_place = 1

                if bush[pre_rabbit_place] == 0:
                    bush[rabbit_place] = 0
                    bush[pre_rabbit_place] = rabbit_num
                    rabbit_num += 1
                    break

                pre_rabbit_place += 1

    # output
    rabbit = {v: k for k, v in bush.items()}
    for k in rabbit:
        if k == 0:
            continue
        print(rabbit[k])


if __name__ == "__main__":
    main()
