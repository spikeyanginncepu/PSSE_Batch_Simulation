#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 14:37
# @Author  : Yang
# @File    : ieee_info.py
# @Software: PyCharm

# 1) 9 Bus system
def get_9businfo():
	bus_id = [i + 1 for i in range(9)]
	bus_kv = [16.5, 18.0, 13.8, 230.0, 230.0, 230.0, 230.0, 230.0, 230.0]
	notrans_brch = [[4, 5], [4, 6], [5, 7], [6, 9], [7, 8], [8, 9]]
	trans_brch = [[1, 4], [2, 7], [3, 9]]
	# businfo_dict = {'bus_id':bus_id, 'bus_kv':bus_kv,'notrans_brch':notrans_brch, 'trans_brch':trans_brch}
	# return businfo_dict
	return bus_id, bus_kv, notrans_brch, trans_brch


# 2) 14 Bus system
def get_14businfo():
	bus_id = [i + 1 for i in range(14)]
	bus_kv = [69.0, 69.0, 69.0, 69.0, 69.0, 138.0, 138.0, 69.0, 138.0, 138.0, 138.0, 138.0, 138.0, 138.0]
	notrans_brch = [[1, 2], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [4, 5], [6, 11], [6, 12], [6, 13], [7, 9], [9, 10],
					[9, 14], [10, 11], [12, 13], [13, 14]]
	trans_brch = [[4, 7], [4, 9], [5, 6], [7, 8]]
	return bus_id, bus_kv, notrans_brch, trans_brch

#  事实证明以下变量是可以通过导入本py文件进行调用的 -> para = bus_info.xt
# import numpy as np
# xt = np.array(range(10))
# yt = np.cos(xt)