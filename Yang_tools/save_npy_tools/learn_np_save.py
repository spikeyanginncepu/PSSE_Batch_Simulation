#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 14:28
# @Author  : Yang
# @File    : learn_np_save.py
# @Software: PyCharm

import numpy as np

# 创建 lst 和 dict，测试时，此行不能注释
a_lst = [[i for i in range(1, 5)], [j for j in range(6, 10)]]
a_dict = {'a': [4, 5, 6], 'b': [7, 9, 1], 'c': 'haha'}

# # 方案一：np.save() 直接存内容, 但是若存字典，先将其装到 [], 再读取时
# #               lst[0], 也能成功读取 dict
# #			     - 特点: 一个 .npy 文件一次只能装一个 lst
# np.save('a_lst', [a_lst])
# np.save('a_dict', [a_dict])
#
# aa1 = np.load('a_lst.npy')
# aa2 = np.load('a_dict.npy')
#
# # 即使 lst 不转为np.array进行保存，读取时自动变成np.array
# print(aa1[0])
# print(aa1[0].shape)
# print(type(aa1[0]))
# print()
#
# # 但是将 dict 保存为 .npy 文件，读取时变成了 .npy文件
# print(aa2.dtype)
# print(type(aa2[0]))
# print(aa2[0])
# print(aa2[0]['a'])


# 方案二：用 np.savez()，传入的参数相当于 keys，传入的内容装到 list->[]里
#              读取时，先取 lst[0], 就能成功读取字典的内容！！
#              - 特点: 用传递关键字的方式，一个 .npz 文件可以保存多个 lst, lst里可以
#                          装 lst, dict, string

np.savez('a_all', savedict=[a_dict], savelst=[a_lst], savestr=['this is a np.savez() test.'])

aa_all = np.load('a_all.npz')
aa1 = aa_all['savelst']
aa2 = aa_all['savedict']
aa3 = aa_all['savestr']

# 类似字典的 .keys() 方法
print(aa_all.keys())

# lst 变为 np.array() 众望所归，一切正常
print()
print(type(aa1))
print(type(aa1[0]))
print(aa1[0])

# dict 先 从 lst[0] 中取出，成功变为字典
print()
print(type(aa2))
print(type(aa2[0]))
print(aa2[0])
print(aa2[0]['b'])

# 看看保存的字符串能否成功读取
print()
print(type(aa3))
print(type(aa3[0]))
print(type(str(aa3[0])))
print(aa3[0])
