#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 9:21
# @Author  : Yang
# @File    : load_ori_data.py
# @Software: PyCharm

import numpy as np
import time

# 方案一 ：pass
#     -缺点： 必须知道每个列表的长度，才能确定每次读取多少字节；
# 					如果lst嵌套，更难算; 如果列表内容是 float，更难算
#           *计算：列表长为 n, 读取字节数为 (n-1)*3 +3

# # 一次性写文件
# a = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
# with open('a_test.txt', 'w') as f:
# 	f.write(str(a))
#
# # 依赖指针读文件
# with open('a_test_1.txt', 'rb') as f:
# 	f.seek(1, 0)
# 	b1 = f.read(15)
#
# 	f.seek(2, 1)  # 从当前位置，偏移2个字节; 注：必须用rb模式打开，才能用相对指针
# 	b2 = f.read(15)
#
# 	f.seek(2, 1)
# 	b3 = f.read(15)
#
# print(b1, len(b1), '\n')
# print(type(b2), len(b2), '\n')
# print(type(eval(b3)), len(b3), '\n')


# # 方案二 ：
#
# # 1 按行写文件
# a = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
# with open('a_test_2.txt', 'w') as f:
# 	for i in range(len(a)):
# 		f.write(str(a[i]) + '\n')
#
# # # 2.1 按行读文件 -- 方式1
# # with open('a_test_2.txt', 'r') as f:
# # 	b1 = eval(f.readline())
# # 	b2 = eval(f.readline())
# # 	b3 = eval(f.readline())
# #
# # print(b1, '\n', len(b1), '\n')
# # print(type(b2), '\n', len(b2), '\n')
# # print(b3, '\n', len(b3), '\n')
#
#
# # 2.2 按行读文件 -- 方式2
# tmp = 0
# with open('a_test_2.txt', 'r') as f:
# 	for i in f:
# 		tmp += 1
# 		b = eval(i)
# 		print(b, '\n', len(b), '\n')
#
# 	print('文件行数：', tmp)
# print(b1, '\n', len(b1), '\n')


# 按方案二 读 a_data.txt
#
# # 测试 -- 960 条，时间大概为 82.27s
# # 数据 shape 为 (960,108,303)
# time_start = time.time()  # 计时
# filepath = r'./Sample_txt_1/a_data_lst_row.txt'
# tmp = 0
# X_read = []
# with open(filepath, 'r') as f:
# 	for i in f:
# 		tmp += 1
# 		b = eval(i)
# 		X_read.append(b)
# 		# print('已读出 '+str(tmp)+' 条样本\n', type(b), '\n', len(b), '\n')
# 		print('已读出 ' + str(tmp) + ' 条样本\n')
# 		if tmp == 960:
# 			break
#
# time_end = time.time()  # 计时 - end
# print('总共耗时：', time_end - time_start)
#

# 方案三：用 np.save() 存为 np 数组，读写效率明显增加
#
# # 存为 np 数组
# time_start = time.time()  # 计时 - start 2
# X_read = np.array(X_read)
# np.save(r'./Sample_txt_1/a', X_read)
#
# print(X_read.shape)
# print(type(X_read[0, 0, 0]))
# print(len(str(X_read[0, 0, 0])))
# time_end = time.time()   # 计时 - end 2
# print('总共耗时：', time_end - time_start)


# # 实践1：读取 14bus-system 截取后存为 (960,108,303) lst 样本文件 a.npy
# #            - 耗时: 0.749s
# time_start = time.time()  # 计时 - start 3
# X_np = np.load(r'./Sample_txt_1/a.npy')
#
# # 压力测试：统计一次能读取多少条 '截取后' 样本进内存
# #               - 测试环境：python3.6 64bit
# #               - 测试1：20*960 = 18 200 条; 耗时：3.94s；内存冲到 64%
# #               - 测试2：25*960 = 24 000 条; 耗时：8.84s；内存冲到 96%
# #               - 测试3：30*960 = 28 800 条; 耗时：14.03s; 内存冲到 99%
# xx = {}
# for i in range(25):
# 	xx['X_np' + str(i + 1)] = np.load(r'./Sample_txt_1/a.npy')
#
# time_end = time.time()  # 计时 - end 3
# print('总共耗时：', time_end - time_start)
# print(X_np.shape)

# 实践2：读取保存了 800 条 dict 样本 14bus-system 的 data_all_dict.npy
#              - 耗时：2.26s
#              - 总结：只要能存，就能取 ！
time_start = time.time()  # 计时 - start 4

x_read = np.load('./Sample_txt_2/data_all_dict.npy')
# print(x_read.dtype)
# print(x_read[0].keys())
# print(type(x_read[0]))
# print(x_read[0]['sample_1']['id_dict'].keys())

# 2018.6.18  观察 总dict 的结构，显然这是截取为303采样点的 单个dict 汇聚而成,
#                  并非从1单个 txt 中导出的，而是直接从 .out 文件中截取 堆叠而成的
print(x_read[0]['sample_1'].keys())
print(len(x_read[0]['sample_1']['data_dict'][1]))

time_end = time.time()  # 计时 - end 4
print('总共耗时：', time_end - time_start)
