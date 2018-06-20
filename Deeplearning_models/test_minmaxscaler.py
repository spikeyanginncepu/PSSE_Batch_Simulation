#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 8:38
# @Author  : Yang
# @File    : test_minmaxscaler.py
# @Software: PyCharm

import numpy as np
from sklearn.preprocessing import MinMaxScaler, scale, StandardScaler

np.random.seed(2)

# x_solo = np.random.randint(3, 10, (2, 4))
# x_solo = x_solo.astype(np.float64)
# print(x_solo)
# print(x_solo.dtype)

x = np.zeros((3, 5, 4))
for i in range(3):
	x[i] = np.random.randint(3, 15, (5, 4))
x = x.astype(np.float64)
x[0][2, 2] = 60  # 设置一个非常大的值

print(x[0])
print()
print(np.transpose(x, (0, 2, 1)))  # 转置
#
# 把 所有页按列堆叠在一起
# print(x)
# print(x.dtype)
# print()
# print(np.reshape(x, (15, 4)))  # 这样可以把 所有页按列堆叠在一起
# print()
# print(np.max(np.reshape(x, (15, 4)), axis=0))  # 找到每一列的 max 值

# 定义放缩器--MinMaxScaler
# #               --> 只能对 (a,b) 二维数组进行缩放，默认对列缩放
# scaler = MinMaxScaler(feature_range=(0, 1))
# x_scaler_0 = scaler.fit_transform(x[0])
# x_scaler_1 = scaler.transform(x[1])
# print(x_scaler_0)
# print()
# print(x_scaler_1)

# # 定义放缩器--StandardScaler(), 放缩为指定x的mean/std 的正态分布
# scaler = StandardScaler().fit(x[0])
# print(scaler.mean_)
# # print(scaler.std_)
# print()
#
# x_scaler_0 = scaler.transform(x[0])
# x_scaler_1 = scaler.transform(x[1])
#
# print(x_scaler_0)
# print()
# print(x_scaler_1)
