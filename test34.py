import os
import sys
import pdb

sys_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'  # or where else you find the psspy.pyc
sys.path.append(sys_path_PSSE)

os_path_PSSE = r'D:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'  # or where else you find the psse.exe
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE


# PYTHONLIB = r'D:\Program Files (x86)\PTI\PSSE34EXplore\PSSLIB'
# PYTHONPRM = r'D:\Program Files (x86)\PTI\PSSE34EXplore\PSSPRM'
# MODELFOLDER = r'C:\IEEE39'


import pssexplore34
import pssarrays
import redirect
import dyntools
import bsntools
import psspy

# psspy.psseinit(39)

outfile = dyntools.CHNF('./t9bus-v34-001-Average.out')
short_title, chanid_dict, chandata_dict = outfile.get_data()
print('\n', short_title)
print('\n', chanid_dict.keys())
print('\n', chanid_dict.values())
print('\n', chandata_dict.keys())
print('\n', chandata_dict.values())
