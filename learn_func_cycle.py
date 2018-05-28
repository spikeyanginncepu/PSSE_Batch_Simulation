#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 11:17
# @Author  : Yang
# @File    : learn_func_cycle.py
# @Software: PyCharm

# def foo():
# 	m = 3
# 	def bar():	   		# 定义内置函数 bar()
# 		n = 4      			# 定义局部变量 n=4
# 		print(m + n)   # m相当于函数bar()的全局变量
# 	print(bar(), m+1)					# foo()函数内调用函数bar()
#
# foo()


print('1. 函数嵌套：\n')
#
# 　　在一个函数中定义了另外一个函数

def outer():
	def inner():
		print('inner')
	print('outer')
	inner()

outer()
# inner()    #  若运行此句，则会出错

print(input('敲回车继续...'))



print('2. 作用域：\n')
#
# 一个标识符的可见范围，这就是标识符的作用域。一般常说的是变量的作用域
# 全局作用域（global）：在整个程序运行环境中都可见
# 局部作用域：在函数、类等内部可见；局部变量使用范围不能超过其所在的局部作用域

x = 5
def f():
	global x
	x = 10
	x += 1
	print(x)

f()