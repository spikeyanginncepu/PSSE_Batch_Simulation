#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 17:18
# @Author  : Yang
# @File    : make_ori_sample.py
# @Software: PyCharm

import time
import numpy as np

# 加载样本数据 —— 100条全耗时 48.458 秒
#                                100条[0.5s,3s]片段耗时14s
#
# 注： ../ 是珊瑚及目录下； ./ 是本级目录下

time_start = time.time()                     # 计时 - start

X_lst = []

# 2018.6.10 不知为何，除了第1条样本--.out file 是114条通道 （113条 + 'time'）
# 仿真样本从第2条开始，无故多了114-150 通道，和前面重复

# 删除多余的通道，包括前面的‘功角’，和后面多余的
# extra_chan = [1, 2, 3, 4, 5, 'time']
# for i in range(114, 151):
# 	extra_chan.append(i)

extra_chan = [1, 2, 3, 4, 5, 'time']

# 循环添加每条样本到 X_lst
n_sample = 960
for i in range(n_sample):
	X_tmp = []
	sample_path = r'./Sample_txt_1/t14Bus-save-dict-00' + str(i + 1) + '.txt'
	with open(sample_path, 'r') as f:
		sample_dict_str = f.read()
		sample_dict = eval(sample_dict_str)
	chanid_dict = sample_dict['id_dict']
	chandata_dict = sample_dict['data_dict']

	for data_keys in chandata_dict.keys():
		if data_keys in extra_chan:
			continue
		X_tmp.append(chandata_dict[data_keys])

	X_lst.append(X_tmp)

	print('已加载第' + str(i + 1) + '条样本')

print()

time_end = time.time()                        # 计时 - end
print('总共耗时：', time_end - time_start)

print()
print('总共保存的样本数：', len(X_lst))
print('每条样本的通道数：', len(X_lst[0]))
print('每个通道截取剩下的采样点数：', len(X_lst[0][0]))

# 测试是否能将前套 list 转换为相应的 np 数组
#   --  除非嵌套 list 保持内部 list 长宽一致，否则每一页 np 矩阵shape将不识别
import numpy as np

xx = np.array(X_lst)
print()
print(xx.shape)  # 预期为 (960,108,303)

# # 方案一
# 将 X_train 列表 X_lst 一次性写进 txt -- 2018.6.10
# with open(r'./Sample_txt_1/a_data_lst.txt', 'w') as f:
# 	f.write(str(X_lst))

# # 方案二
# # 分行写进 txt -- 2018.6.11，避免内存爆炸
# with open(r'./Sample_txt_1/a_data_lst_row.txt', 'w') as f:
# 	for row_txt in range(n_sample):
# 		f.write(str(X_lst[row_txt])+'\n')

# # 方案三
# # X_lst 一次性存储为 .npy 格式
# data_path = r'./Sample_txt_1/a_data.npy'
# np.save(data_path, X_lst)