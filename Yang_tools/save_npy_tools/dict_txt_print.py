#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 18:59
# @Author  : Yang
# @File    : out_txt_print.py
# @Software: PyCharm

import numpy as np

i = 0
# sample_path = r'../Sample_14bus_3/Sample_txt_2/t14Bus-save-dict-00' + str(i + 1) + '.txt'
sample_path = r'./Sample_txt_1/t14Bus-save-dict-00' + str(i + 1) + '.txt'

with open(sample_path, 'r') as f:
	sample_dict_str = f.read()
	sample_dict = eval(sample_dict_str)

print(len(sample_dict['data_dict'].keys()))
print(sample_dict['data_dict'].keys())
print(sample_dict['id_dict'].values())


# # 保存 time [0.5, 3] 的事件切片，单个 txt 已经是切片过的了
# time = sample_dict['data_dict']['time']
# print(time)
#
# time_path = r'./Sample_txt_1/a_time.npy'
# np.save(time_path, time)