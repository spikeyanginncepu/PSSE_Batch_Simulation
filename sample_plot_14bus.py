#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 15:48
# @Author  : Yang
# @File    : out_to_plot.py
# @Software: PyCharm

import os
import sys

sys_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'  # or where else you find the psspy.pyc
sys.path.append(sys_path_PSSE)
os_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'  # or where else you find the psse.exe
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import dyntools
import matplotlib.pyplot as plt


sample_id = 1

for i in range(0, 5):
	for j in range(12):
		outfile_noRel = dyntools.CHNF('./t14Bus-PY-00' + str(sample_id) + '.out')
		sample_id += 1
		short_title_noRel, chanid_dict_noRel, chandata_dict_noRel = outfile_noRel.get_data()
		time_noRel = chandata_dict_noRel['time']

		fig = plt.figure(i + 1)
		fig.patch.set_facecolor('0.8')  # set background color, could use float number and color name
		# plt.subplots_adjust(top=0.95, bottom=0.06, left=0.05, right=0.98, wspace=0.15, hspace=0.45)  # 调整 subplot在 fig中的边界距离

		plt.subplot(4, 3, j + 1)
		plt.plot(time_noRel, chandata_dict_noRel[1], linestyle='-', linewidth=1, color='red',
				 label=chanid_dict_noRel[1])
		plt.plot(time_noRel, chandata_dict_noRel[2], linestyle='-', linewidth=1, color='green',
				 label=chanid_dict_noRel[2])
		plt.plot(time_noRel, chandata_dict_noRel[3], linestyle='-', linewidth=1, color='blue',
				 label=chanid_dict_noRel[3])
		plt.plot(time_noRel, chandata_dict_noRel[4], linestyle='-', linewidth=1,
				 label=chanid_dict_noRel[4])
		plt.plot(time_noRel, chandata_dict_noRel[5], linestyle='-', linewidth=1,
				 label=chanid_dict_noRel[5])

		plt.grid(linestyle='--', color='grey', linewidth=0.5)
		plt.xlabel("Time")
		plt.ylabel("Angle")
		plt.title("No Relative Angle - Angle Curve")
		plt.legend()
		axes = plt.gca()
		axes.set_xlim([0, 10])
		# _adjust() 语句放在句末，防止还没出现列子图，导致 hspace 参数报错
		plt.subplots_adjust(top=0.95, bottom=0.06, left=0.05, right=0.98, wspace=0.15, hspace=0.45)  # 调整 subplot在 fig中的边界距离


plt.show()
