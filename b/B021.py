# coding: utf-8
import sys
import re


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    word_num = int(lines[0])
    word_lines = lines[1: 1 + word_num]

    for line in word_lines:
        if line.endswith(('s', 'sh', 'ch', 'o', 'x')):
            print(line + 'es')
        elif line.endswith(('f', 'fe')):
            print(re.sub(r'fe?$', 'ves', line))
        elif line.endswith('y') and line[-2] not in 'aiueo':
            print(re.sub(r'y$', 'ies', line))
        else:
            print(line + 's')

if __name__ == "__main__":
    main()
