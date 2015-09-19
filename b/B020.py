# coding: utf-8
import sys
import re


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    dummy = '''7
go to blank page
go to nkah
use the back button
go to gi
go to in
go to nkah
use the back button'''
    lines = [x.strip('\n') for x in dummy.split('\n')]

    query_num = int(lines[0])
    query_lines = lines[1: 1 + query_num]

    histry_list = []

    for i, line in enumerate(query_lines):
        if i == 0:
            histry_list.append('blank page')
            print histry_list[-1]
        else:
            if line.find('go to ') == 0:
                histry_list.append(re.sub(r'go to ', '', line))
                print histry_list[-1]

            elif line == 'use the back button':
                histry_list.pop()
                print histry_list[-1]

if __name__ == "__main__":
    main()
