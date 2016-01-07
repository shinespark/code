# coding: utf-8
n = int(input())
print((lambda f: f(n,f))(lambda n,f: n*f(n-1,f) if n>0 else 1))
