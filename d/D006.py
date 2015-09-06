# coding: utf-8
a = raw_input().split()
value = int(a[0])
unit = a[1]

if unit == 'km':
    print(value * 1000 * 1000)
elif unit == 'm':
    print(value * 1000)
elif unit == 'cm':
    print(value * 10)
