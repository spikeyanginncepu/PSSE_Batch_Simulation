#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 15:00
# @Author  : Yang
# @File    : learn_dict2json_file.py
# @Software: PyCharm

# 保存
dict_sav1 = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
dict_sav2 = {'haha': [1, 2, 3, 4], 2: {3: 4, 4: 5}}

f = open('test_sav_dict.txt', 'w')
f.writelines([str(dict_sav1) + '\n', str(dict_sav2)])
f.close()

# 读取方式一： f.readlines()
# f = open('test_sav_dict.txt', 'r')
# a = f.readlines()
# dict_load1 = eval(a[0])
# dict_load2 = eval(a[1])
# f.close()
# print(dict_load1.items(), '\n\n', dict_load2.items())

# 读取方式2:   f.readline()
with open('test_sav_dict.txt', 'r') as f:
	a1 = f.readline()
	a2 = f.readline()
	dict_load1 = eval(a1)
	dict_load2 = eval(a2)
print(dict_load1.items(), '\n\n', dict_load2.items())


# 补充：dict & zip 构造字典方式举例
# dict(zip(['bt','hh','rt'],[{'sd':[5,6,4]},2,3]))