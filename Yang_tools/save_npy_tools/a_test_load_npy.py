#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/18 15:49
# @Author  : Yang
# @File    : test_load_npy.py
# @Software: PyCharm

import numpy as np

# 读取 (960,108,303) 结构的样本数据 -- > .npy 文件
data = np.load('./Sample_txt_1/a_data.npy')
print(type(data))
print(data.shape)

# 读取 (960,) 的标签数据
label = np.load('./Sample_txt_1/a_label.npy')
print(type(label))
print(label.shape)
# print(label)

# 读取 (303,）的时间切片数据
time = np.load('./Sample_txt_1/a_time.npy')
print(type(time))
print(time.shape)
# print(time)


