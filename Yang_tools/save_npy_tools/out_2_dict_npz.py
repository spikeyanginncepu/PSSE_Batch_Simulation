#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 16:09
# @Author  : Yang
# @File    : out_2_dict.py
# @Software: PyCharm

import numpy as np
import time
import os
import sys
import json
import codecs

sys_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'  # or where else you find the psspy.pyc
sys.path.append(sys_path_PSSE)
os_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'  # or where else you find the psse.exe
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import dyntools


def get_out_dict(outpath):
	outfile = dyntools.CHNF(outpath)
	short_title, chanid_dict, chandata_dict = outfile.get_data()

	# 将chandata_dict所有values截取区间为0.5s末到3s末，对应索引为62, 364
	for chan_keys in chandata_dict.keys():
		chandata_dict[chan_keys] = chandata_dict[chan_keys][62:364 + 1]

	out_dict = {'id_dict': chanid_dict, 'data_dict': chandata_dict}
	return out_dict


def save_dict_txt(sample_dict, target_folder, txt_filename):
	with open(target_folder + '/' + txt_filename, 'w') as f:
		f.write(str(sample_dict))


def save_dict_json(sample_dict, target_folder, json_filename):
	with codecs.open(target_folder + '/' + json_filename, 'a', 'utf-8') as f:
		json.dump(sample_dict, f, ensure_ascii=False)


# outfile.write('\n')


if __name__ == '__main__':
	n_sample = 800

	# 判断 Sample_txt 文件夹是否存在
	target_folder = r'./Sample_txt_' + input('请输入 dict_to_txt 目标文件夹编号：')
	if os.path.exists(target_folder):
		print('该目标文件夹已存在，请重新输入...\n')
		target_folder = r'./Sample_txt_' + input('请重新输入 dict_to_txt 目标文件夹编号：')
	else:
		os.makedirs(target_folder)

	# # 方案一：将样本 dict 逐条保存为 .txt，生成 960 个 .txt 文件
	# for i in range(n_sample):
	# 	out_path_tmp = r'./t14Bus-PY-00' + str(i + 1) + '.out'
	#
	# 	# 获取当前样本的总dict
	# 	out_dict_tmp = get_out_dict(out_path_tmp)
	#
	# 	# 逐条将 dict 保存为 txt 文件
	# 	save_dict_txt(out_dict_tmp, target_folder, 't14Bus-save-dict-00' + str(i + 1) + '.txt')
	#
	# 	# 逐条将 dict 保存为 json 文件
	# 	# save_dict_json(out_dict_tmp, target_folder, 't14Bus-save-dict-00' + str(i + 1) + '.json')
	#
	# 	print('已写入' + str(i + 1) + '/' + str(n_sample) + '条样本')  # 观察进写入进度

	# 方案二：将字典 用 np.save() 方法，将所有 dict 一次性保存为 .npz 文件
	#               - 坑：从 .out 导出实在 python3.4 环境
	#                         只要一次性保存的数据占用内存过大就会 raise Memory Error
	#                      * 原因：python 32bit 最大只能使用 2G 内存，大于报错；64bit 无限制
	#              - 耗时：500条 20.9s
	#              - 测试1：600条能保存成功；
	#              - 测试2：800条能保存成功；
	#              - 测试3：900条 失败 ！
	time_start = time.time()  # 计时 - start

	all_dict = {}
	for i in range(n_sample):
		out_path_tmp = r'./t14Bus-PY-00' + str(i + 1) + '.out'
		out_dict_tmp = get_out_dict(out_path_tmp)
		all_dict['sample_' + str(i + 1)] = out_dict_tmp
		print('已写入' + str(i + 1) + '/' + str(n_sample) + '条样本')  # 观察进写入进度

	np.save(target_folder + '/data_all_dict.npy', [all_dict])

	time_end = time.time()  # 计时 - end
	print('总共耗时：', time_end - time_start)
