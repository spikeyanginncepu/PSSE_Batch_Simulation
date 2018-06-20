#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 14:36
# @Author  : Yang
# @File    : out_to_txt.py
# @Software: PyCharm

import os
import sys
import matplotlib.pyplot as plt

sys_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'  # or where else you find the psspy.pyc
sys.path.append(sys_path_PSSE)

os_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'  # or where else you find the psse.exe
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import dyntools

# file PATH
outfile = dyntools.CHNF('./Sample_14bus_1/t14Bus-PY-001.out')

short_title, chanid_dict, chandata_dict = outfile.get_data()
print('\n标题“short_title”是：', short_title)
print('类型是：', type(short_title), '--字符串')
print('字符串长度为: ', len(short_title))
# print(input('按回车继续...'))

print('\n通道 id“chanid_dict”，以及通道 data“chandata_dict“')
print('类型是：', type(chanid_dict), '--字典')
print('字典的 keys 均为：', chanid_dict.keys())
print('其长度为: ', len(chanid_dict))
# print(input('按回车继续...'))

print('\n通道 id“chanid_dict”的 values 为:\n ', chanid_dict.values())
# print(input('按回车继续...'))

# print('\n通道 data“chandata_dict”的 values 为: \n', chandata_dict.values())
# print('观察 len(chandata_dict.values()) 为：', len(chandata_dict.values()))
# print(input('按回车继续...'))
#
# # 由于dict.values() 是 dict_values 对象，不能直接索引，因此先转换为列表再去取列表中第 0 个元素
# # values = list(chandata_dict.values())
# # print('观察 len(values[0] 为：', len(values[0]))
# print('观察 ”通道 data“ 字典取值 为：', chandata_dict[1])
# print('观察 ”通道 data“ 字典取值 长度 为：', len(chandata_dict[1]))

# 作图观察某个通道
time = chandata_dict['time']
angle1_name = chanid_dict[6]
angle1_values = chandata_dict[6]
print('\n时间序列：', time)

print('时间序列差值', time[1]-time[0], time[11]-time[10])
print('而一个周波 T = 1/60Hz = '+str(1/60)+' s')
print('可以看到PSSE的时间步长大概为半个周波')
print('因此 5s 末大概取 time[603]：', time[603])
# plt.plot(time, volt1_values, label=volt1_name)
# plt.xlabel('time(s)')
# plt.ylabel('Voltage(pu)')
# plt.legend()
# plt.show()
