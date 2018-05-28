#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 9:54
# @Author  : Yang
# @File    : learn_debug.py
# @Software: PyCharm

def twice(n):
    n *= 2
    return n

a = float(input("a:"))
b = float(input("b:"))
# print("====a,b:", a, b)

if a > 3:
    b += 4
    # print("====1 b:", b)
    if b > 5:
        c = a + twice(b)
        # print("====1 c:", c)
    else:
        c = twice(a) + b
        # print("====2 c:", c)
else:
    b -= 2
    # print("====2 b:", b)
    if b < 1:
        c = a - twice(b)
        # print("====3 c:", c)
    else:
        c = twice(a) - b
        # print("====4 c:", c)
print(c)