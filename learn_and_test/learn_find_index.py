#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 16:51
# @Author  : Yang
# @File    : sample_mark.py
# @Software: PyCharm

# def sm_mark(list1, list2):


ls1 = [i * 1 / 11 for i in range(20)]
print('原数组为：', ls1, '\n')
print('1.0在原数组的索引是：', ls1.index(1), '\n')

num_range = [x for x in ls1 if (x > 0.9) & (x < 1.3)]
print('范围在 [0.9, 1.3]的数有：', num_range, '\n')

print('我想找”1.0“在ls1中的索引，用语句：ls1.index(num_range[1])')
print('索引为：', ls1.index(num_range[1]))
