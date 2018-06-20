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


outfile_noRel = dyntools.CHNF('./t9Bus-PY-001.out')
short_title_noRel, chanid_dict_noRel, chandata_dict_noRel = outfile_noRel.get_data()

# print(chandata_dict_noRel[1])
# print(chandata_dict_noRel['time'])

time_noRel = chandata_dict_noRel['time']
angle_noRel = chandata_dict_noRel[1]  # based on the channel identifier set in the dynamic simulation



fig = plt.figure()
fig.patch.set_facecolor('0.8')   # set background color, could use float number and color name
plt.plot(time_noRel, angle_noRel, linestyle='-', linewidth=1, color='red', label=chanid_dict_noRel[1])
plt.plot(time_noRel, chandata_dict_noRel[2], linestyle='-', linewidth=1, color='green', label=chanid_dict_noRel[2])
plt.plot(time_noRel, chandata_dict_noRel[3], linestyle='-', linewidth=1, color='blue', label=chanid_dict_noRel[3])
plt.grid(linestyle='--', color='grey', linewidth=0.5)
plt.xlabel("Time")
plt.ylabel("Angle")
plt.title("No Relative Angle - Angle Curve")
plt.legend()
axes = plt.gca()
axes.set_xlim([0, 10])


plt.show()