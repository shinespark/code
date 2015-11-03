# coding: utf-8
import sys
import math

def main():
    #  input_num = raw_input()
    dummy = '''100.02651'''
    r = math.ceil(float(dummy))

    area = r ** 2 * 4
    print int(math.ceil(area))

if __name__ == "__main__":
    main()
