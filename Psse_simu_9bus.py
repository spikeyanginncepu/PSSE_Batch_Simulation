#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 11:10
# @Author  : Yang
# @File    : Psse_simu.py
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

[bus_id, bus_kv, notrans_brch, trans_brch] = get_9businfo()
T = 1 / 60
clear_time = [i * T for i in range(5, 17)]  # 共 12 个不同的切除时间
fault_position = [0.1, 0.3, 0.5, 0.7, 0.9]  # 共 5 个不同的故障位置
num_bus = 9
num_notrans_brch = 6
num_trans_brch = 3

num_sample_id = 1


def do_simulation():
	global num_sample_id

	# set Samples Path
	sample_path = r'./Sample_9bus_' + input('请输入样本集编号：')
	if os.path.exists(sample_path):
		print('该样本集已存在，请重新输入...\n')
		sample_path = r'./Sample_9bus_' + input('请重新输入样本集编号：')
	else:
		os.makedirs(sample_path)

	# # 1 母线故障——样本编号：1~12*num_bus -> [1,  108]
	# for i in range(num_bus):
	# # for i in range(1):
	# 	for j in range(len(clear_time)):
	# 		# init
	# 		psspy.psseinit(50)
	# 		psspy.case(r""".\Models\9Bus-test\ieee9bus_v32.sav""")
	# 		psspy.fnsl([0, 0, 0, 1, 1, 0, 99, 0])
	# 		psspy.cong(0)
	# 		psspy.conl(0, 1, 1, [0, 0], [100.0, 0.0, 0.0, 100.0])
	# 		psspy.conl(0, 1, 2, [0, 0], [100.0, 0.0, 0.0, 100.0])
	# 		psspy.conl(0, 1, 3, [0, 0], [100.0, 0.0, 0.0, 100.0])
	# 		psspy.fact()
	# 		psspy.tysl(0)
	# 		psspy.dyre_new([1, 1, 1, 1], r""".\Models\9Bus-test\ieee9bus.dyr""", "", "", "")
	#
	# 		# perform Dynamic Simulation
	# 		# 1) set "Channal Setup Wizard"
	# 		psspy.chsb(0, 1, [-1, -1, -1, 1, 1, 0])    # Angle
	# 		psspy.chsb(0, 1, [-1, -1, -1, 1, 7, 0])    #
	# 		psspy.chsb(0, 1, [-1, -1, -1, 1, 13, 0])  #
	#
	# 		# 2) name output file
	# 		psspy.set_chnfil_type(0)  # 1 for OUTX format, 0 for (old) OUT format
	# 		psspy.strt_2([0, 1], sample_path + '\\t9Bus-PY-00' + str(num_sample_id) + '.out')
	# 		num_sample_id += 1
	#
	# 		# 3) in normal stat, run network to 1 seconds
	# 		psspy.run(0, 1.0, 0, 1, 1)
	#
	# 		# 4) set Balanced_bus_fault with R,X -> [0, 0]
	# 		psspy.dist_bus_fault(bus_id[i], 1, bus_kv[i], [0.0, -2E+2])		# --------  ! important
	#
	# 		# 5) set fault run time
	# 		psspy.run(0, 1 + clear_time[j], 0, 1, 1)
	#
	# 		# 6) clear fault, and run net to 10 seconds
	# 		psspy.dist_clear_fault(1)
	# 		psspy.run(0, 10.0, 0, 1, 1)
	#
	# 		# 7) 关闭本次仿真相关的文件, importaant !!!!!!!!!!!!!!!!!!!!!!
	# 		psspy.pssehalt_2()

	# 2 非变压器支路故障——样本编号： [108+1,  108+360]
	for i in range(num_notrans_brch):
	# for i in range(1):
		for k in range(len(fault_position)):
		# for k in range(1):
			for j in range(len(clear_time)):
				print('\n\n\n\n----------------我是分割线--------------\n')
				print('已仿真第 ' + str(num_sample_id) + ' 条样本\n\n\n\n')

				# init
				psspy.psseinit(50)
				psspy.case(r""".\Models\9Bus-test\ieee9bus_v32.sav""")
				psspy.fnsl([0, 0, 0, 1, 1, 0, 99, 0])
				psspy.cong(0)
				psspy.conl(0, 1, 1, [0, 0], [100.0, 0.0, 0.0, 100.0])
				psspy.conl(0, 1, 2, [0, 0], [100.0, 0.0, 0.0, 100.0])
				psspy.conl(0, 1, 3, [0, 0], [100.0, 0.0, 0.0, 100.0])
				psspy.fact()
				psspy.tysl(0)
				psspy.dyre_new([1, 1, 1, 1], r""".\Models\9Bus-test\ieee9bus.dyr""", "", "", "")

				# perform Dynamic Simulation
				# 1) set "Channal Setup Wizard"
				psspy.chsb(0, 1, [-1, -1, -1, 1, 1, 0])  # Angle
				psspy.chsb(0, 1, [-1, -1, -1, 1, 7, 0])  #
				psspy.chsb(0, 1, [-1, -1, -1, 1, 13, 0])  #

				# 1.1) set Relative Machine Angle
				psspy.set_relang(1, 1, r"""1""")

				# 2) name output file
				psspy.set_chnfil_type(0)  # 1 for OUTX format, 0 for (old) OUT format
				psspy.strt_2([0, 1], sample_path + '//t9Bus-PY-00' + str(num_sample_id) + '.out')
				num_sample_id += 1

				# 3) in normal stat, run network to 1 seconds
				psspy.run(0, 1.0, 0, 1, 1)

				# 4) set unbalanced_Branch_fault -- 3 Phase -- with R,X -> [0, 0]
				psspy.dist_spcb_fault_2(notrans_brch[i][0], notrans_brch[i][1], r"""1""",
										[3, 0, 3, 1, 0, 0, 1],
										[fault_position[k], 0.0, 0.0, 0.0, 0.0])  # --------  ! important

				# 5) set fault run time
				psspy.run(0, 1 + clear_time[j], 0, 1, 1)

				# 6) clear fault, and run net to 10 seconds
				psspy.dist_clear_fault(1)
				psspy.run(0, 10.0, 0, 1, 1)

				# 7) 关闭本次仿真相关的文件, importaant !!!!!!!!!!!!!!!!!!!!!!
				psspy.pssehalt_2()


# # 3 变压器支路故障——样本编号：[468+1,  468+36]
# for i in range(num_trans_brch):
# 	for j in range(len(clear_time)):
# 		# init
# 		psspy.psseinit(50)
# 		psspy.case(r""".\Models\9Bus-test\ieee9bus_v32.sav""")
# 		psspy.fnsl([0, 0, 0, 1, 1, 0, 99, 0])
# 		psspy.cong(0)
# 		psspy.conl(0, 1, 1, [0, 0], [100.0, 0.0, 0.0, 100.0])
# 		psspy.conl(0, 1, 2, [0, 0], [100.0, 0.0, 0.0, 100.0])
# 		psspy.conl(0, 1, 3, [0, 0], [100.0, 0.0, 0.0, 100.0])
# 		psspy.fact()
# 		psspy.tysl(0)
# 		psspy.dyre_new([1, 1, 1, 1], r""".\Models\9Bus-test\ieee9bus.dyr""", "", "", "")
#
# 		# perform Dynamic Simulation
# 		# 1) set "Channal Setup Wizard"
# 		psspy.chsb(0, 1, [-1, -1, -1, 1, 1, 0])  # Angle
# 		psspy.chsb(0, 1, [-1, -1, -1, 1, 7, 0])  #
# 		psspy.chsb(0, 1, [-1, -1, -1, 1, 13, 0])  #
#
# 		# 2) name output file
# 		psspy.set_chnfil_type(0)  # 1 for OUTX format, 0 for (old) OUT format
# 		psspy.strt_2([0, 1], sample_path + '\\t9Bus-PY-00' + str(num_sample) + '.out')
# 		num_sample += 1

# 		# 3) in normal stat, run network to 1 seconds
# 		psspy.run(0, 1.0, 0, 1, 1)
#
# 		# 4) set Balanced_branch_fault with R,X -> [0, 0]
# 		psspy.dist_branch_fault(trans_brch[i][0], trans_brch[i][1], r"""T2""",
# 								1, bus_kv[trans_brch[i][0]-1], [0.0, 0.0])		# --------  ! important
#
# 		# 5) set fault run time
# 		psspy.run(0, 1 + clear_time[j], 0, 1, 1)
#
# 		# 5) clear fault, and run net to 10 seconds
# 		psspy.dist_clear_fault(1)
# 		psspy.run(0, 10.0, 0, 1, 1)


if __name__ == '__main__':
	do_simulation()
