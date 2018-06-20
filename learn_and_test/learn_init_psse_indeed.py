#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 19:59
# @Author  : Yang
# @File    : learn_init_psse_indeed.py
# @Software: PyCharm

import os
import sys

sys_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'  # or where else you find the psspy.pyc
sys.path.append(sys_path_PSSE)
os_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'  # or where else you find the psse.exe
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import pssexplore34
import pssarrays
import redirect
import dyntools
import bsntools
import psspy
from bus_info import *

for i in range(5):
	print(str(i), '\n')
	psspy.psseinit(50)
	psspy.pssehalt_2()