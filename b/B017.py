# coding: utf-8
from collections import Counter


def main():
    line = raw_input()
    #  line = 'AAAA'
    c = Counter(line)

    if c.most_common(1)[0][1] == 4:
        print 'FourCard'
    elif c.most_common(1)[0][1] == 3:
        if '*' in c:
            print 'FourCard'
        else:
            print 'ThreeCard'
    elif c.most_common(1)[0][1] == 2:
        if '*' in c:
            print 'ThreeCard'
        elif c.most_common(2)[0][1] == c.most_common(2)[1][1]:
            print 'TwoPair'
        else:
            print 'OnePair'
    else:
        if '*' in c:
            print 'OnePair'
        else:
            print 'NoPair'


if __name__ == "__main__":
    main()
