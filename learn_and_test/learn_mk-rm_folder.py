#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 10:28
# @Author  : Yang
# @File    : learn_create_folder.py
# @Software: PyCharm

import os
import shutil

# 主要涉及到三个函数
# 1、os.path.exists(path) 判断一个目录是否存在
#
# 2、os.makedirs(path) 多层创建目录
#
# 3、os.mkdir(path) 逐级创建目录

if not os.path.exists('./Sample1/t2'):
	os.makedirs('./Sample1/t2')  # 多级目录的一次性创建，不用先创建父文件夹

else:
	print('该目录已存在')
	del_flag = input('是否删除该目录？(y/n)')
	if del_flag == 'y':
		path_Flag = input('删除哪个目录?\n1."./Sample1/t2"\n2."./Sample1"')
		if path_Flag == '1':
			os.rmdir('./Sample1/t2')
			print('删除成功')
		if path_Flag == '2':
			del_methed = path_Flag = input('哪种方式删除?\n1."os.rmdir()"\n2."shutil.rmtree()"')
			if del_methed == '1':
				os.rmdir('./Sample1')
			if del_methed == '2':
				shutil.rmtree('./Sample1')
				print('删除成功')
		else:
			pass
	if del_flag == 'n':
		pass
	else:
		pass