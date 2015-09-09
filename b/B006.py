# coding: utf-8
import sys
import math

g = 9.8

def calculate(o_y, s, deg, x, y, a):
    # ans = o_y + xtanθ - (gx^2)/2s^2cos^2θ)
    # y - a/2 <= ans <= y + a/2 ならHit
    rad = math.radians(deg)

    x_1 = o_y
    x_2 = x * math.tan(rad)
    x_3 = (g * x * x) / (2 * s * s * math.cos(rad) * math.cos(rad))

    ans = round(x_1 + x_2 - x_3, 2)

    if y - a/2 <= ans <= y + a/2:
        distance = abs(round(y - ans, 1))
        return 'Hit %s' % str(distance)
    else:
        return 'Miss'

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    splited_first_line = [int(x) for x in lines[0].split()]
    splited_second_line = [int(x) for x in lines[1].split()]
    o_y, s, deg = splited_first_line
    x, y, a = splited_second_line

    print calculate(o_y, s, deg, x, y, a)

if __name__ == "__main__":
    main()
