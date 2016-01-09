# coding: utf-8
import io


def main():
    n = int(input())
    m1 = int(input())
    x_l = [int(i) for i in (input().split())][:m1]
    m2 = int(input())
    y_l = [int(i) for i in (input().split())][:m2]
    d = '''8
5
1 3 5 6
3
5 6 4 2 1
'''
    b = io.StringIO(d)
    n = int(b.readline().strip())
    m1 = int(b.readline().strip())
    x_l = [int(i) for i in (b.readline().strip().split())][:m1]
    m2 = int(b.readline().strip())
    y_l = [int(i) for i in (b.readline().strip().split())][:m2]
    print(x_l)

    diff = set(y_l) - set(x_l)
    if len(diff) > 0:
        print(' '.join(map(str, diff)))
    else:
        print('None')


if __name__ == "__main__":
    main()
