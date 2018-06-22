#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 15:47
# @Author  : Yang
# @File    : test_1d_cov_14bus.py
# @Software: PyCharm

import time
import keras
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Conv1D, GlobalMaxPooling1D, MaxPooling1D
from keras.optimizers import SGD, Adam

# 加载样本数据 alone .txt 文件 — 100条全耗时 48.458 秒
#                                                    100条[0.5s,3s]片段耗时14s
#
# 注： ../ 是珊瑚及目录下； ./ 是本级目录下
# 计时程序
# time_start = time.time()
# time_end=time.time()
# print('totally cost',time_end-time_start)


# 1 导入数据
data = np.load('../Samples/Sample_14bus_2/Sample_txt_1/a_data.npy')
labels = np.load('../Samples/Sample_14bus_2/Sample_txt_1/a_label.npy')
time_seq = np.load('../Samples/Sample_14bus_2/Sample_txt_1/a_time.npy')  # 切片后的time

# 将data的 channel 和 采样点 转置 --> 方便后续 1dcov 数据输入
data = np.transpose(data, (0, 2, 1))
print('通道&采样点 axis 交换后数据结构为：', data.shape)

# 1.1 生成故障切除时刻索引：
#                --> 方便shuffle后还能定位到指定的故障前后时刻
time_clear_idx = []
for i in range(80):
	for j in range(12):
		time_clear_idx.append(j)
time_clear_idx = np.array(time_clear_idx)
# print('前36个sample的 time_clear_idx 索引为：\n', time_clear_idx[:36])

# # 确定故障切除时间
# clear_time = [i * 1/60 for i in range(5, 28, 2)]  # 共 12 个不同的切除时间->[1.0833, 1.45]
# print(clear_time)

# print(time_seq[62])  # 1s末
# print(time_seq[62 + 5 * 2])  # 1.0833s末
# print(time_seq[62 + 27 * 2])  # 1.45s末

# 1.2 对data的采样点进行进一步切片
slice_flag = 1

# 切片方案 1：取故障切除后的 3个T，
if slice_flag == 1:
	slice_t = 3     # 取故障后 3T 的采样点
	slice_len = slice_t * 2  # 故障切除后的采样长度
	data_tmp = np.zeros((data.shape[0], slice_len, data.shape[2]))
	print('data_tmp 占位符的 shape 为：', data_tmp.shape)

	for i in range(len(data)):
		# 经历5T施加故障；    每隔2T再施加故障，总共12次间隔
		data_tmp[i] = data[i][62 + 5 * 2 + (time_clear_idx[i] * 2) * 2:62 + 5 * 2 + (time_clear_idx[i] * 2) * 2 + slice_len, :]
	# print(data_tmp[0][:, 0])
	print('切片后第 1 个sample的每一列长度为：', data_tmp[0][:, 0].shape)
	del data
	data = data_tmp

# 切片方案 2：取所有样本 从“故障开始到 n*T”的切片
#                  	理论上分类是不可能准确的
if slice_flag == 2:
	slice_t = 3
	slice_len = slice_t*2
	data_tmp = np.zeros((data.shape[0], slice_len, data.shape[2]))
	print('data_tmp 占位符的 shape 为：', data_tmp.shape)

	for i in range(data.shape[0]):
		data_tmp[i] = data[i][62:62+slice_len, :]

	print('切片后第 1 个sample的每一列长度为：', data_tmp[0][:, 0].shape)
	del data
	data = data_tmp


# 2 分割样本为 train/test
# 2.1 生成样本集索引, 并shuffle
# np.random.seed(3)  # 随机可复现
data_shuffle_idx = np.arange(data.shape[0])
np.random.shuffle(data_shuffle_idx)
# print(data_shuffle_idx)

# 2.2 按shuffle后的index进行样本集分割
tt_flag = 2

# 方案一： , 比例为 2：1
if tt_flag == 1:
	idx_tt = int(len(data_shuffle_idx) / 3) * 2  # 定位到前2/3的index位置
# 方案一： , 比例为 4：1
if tt_flag == 2:
	idx_tt = int(len(data_shuffle_idx) /6)  # 定位到前2/3的index位置

train_idx = data_shuffle_idx[0:idx_tt]  # train set 的 index
test_idx = data_shuffle_idx[idx_tt:]  # test set 的 index
# print(len(train_idx))
# print(test_idx.shape)


# 2.3 生成 train/test set
x_train = data[train_idx]  # (640, 303, 108)
y_train = labels[train_idx]
time_clear_idx_train = time_clear_idx[train_idx]
# print(time_clear_idx_train.shape)
# print(len(x_train))  # 返回数组的 最外层 层数

x_test = data[test_idx]  # (320, 303, 108)
y_test = labels[test_idx]
time_clear_idx_test = time_clear_idx[test_idx]

# 3 数据归一化
scaler_flag = 2  # 选择归一化方案
x_train_norm = np.empty_like(x_train)  # 创建占位符
x_test_norm = np.empty_like(x_test)

# 方案一：按 sample1 的各feature的max/min为基准，将所有样本map到 [0,1]
if scaler_flag == 1:
	scaler = MinMaxScaler(feature_range=(0, 1))
	x_train_norm[0] = scaler.fit_transform(x_train[0])  # 以 x[0] 作为归一化标准

	for i in range(1, len(x_train)):
		x_train_norm[i] = scaler.transform(x_train[i])
	for i in range(len(x_test)):
		x_test_norm[i] = scaler.transform(x_test[i])

# print(x_train_norm[0][:, 7])
# print(x_train_norm[0].shape)

# 方案二：转换shape 为 (640*303, 108), 按 train set 总样本的各feature的max/min为基准，将所有样本map到 [0,1]
if scaler_flag == 2:
	x_train_tmp = np.reshape(x_train, (len(x_train) * x_train.shape[1], x_train.shape[2]))
	# print(x_train_tmp.shape) # 观察数据结构，注意在一开始 data 转置果，即channel和采样点交换过
	scaler = MinMaxScaler(feature_range=(0, 1))
	scaler.fit_transform(x_train_tmp)

	for i in range(len(x_train)):
		x_train_norm[i] = scaler.transform(x_train[i])
	for i in range(len(x_test)):
		x_test_norm[i] = scaler.transform(x_test[i])

# print(x_train_norm[0][:, 107])
# print(x_train_norm[0].shape)

# 4 标签转换
# # 原始结构 --> （+1:稳定；-1:失稳；-2.角度未拉开，但功角小于0°）
label_flag = 3  # 选择标签转换方案

# 方案一：分3类，(1,-1,-2) map --> （0, 1, 2）
if label_flag == 1:
	y_train[y_train == 1] = 0
	y_train[y_train == -1] = 1
	y_train[y_train == -2] = 2

	y_test[y_test == 1] = 0
	y_test[y_test == -1] = 1
	y_test[y_test == -2] = 2

	# print(y_train)
	print(y_train.shape)

	# 将labels 转换成 categorical one-hot encoding
	y_train = keras.utils.to_categorical(y_train, num_classes=3)
	y_test = keras.utils.to_categorical(y_test, num_classes=3)

# print(y_train[0:10], '\n\n', y_train[0:10])

# 方案二：分两类，(1,-1,-2) map --> （0, 1, 0）
# #                          把 -2 角度未拉开当作 ‘稳定’，map 1 失稳 的样本量会很少--27条
# # 原始结构 --> （+1:稳定；-1:失稳；-2.角度未拉开，但功角小于0°）
if label_flag == 2:
	y_train[y_train == 1] = 0
	y_train[y_train == -1] = 1  # 27条
	y_train[y_train == -2] = 0

	y_test[y_test == 1] = 0
	y_test[y_test == -1] = 1
	y_test[y_test == -2] = 0

	print(np.sum(y_train == 1))
# print(y_train)

# 方案三：分两类，(1,-1,-2) map --> （0, 1, 1）
# #                          把 -2 角度未拉开当作 ‘失稳’，map 1 失稳 量会相对较多
# # 原始结构 --> （+1:稳定；-1:失稳；-2.角度未拉开，但功角小于0°）
if label_flag == 3:
	y_train[y_train == 1] = 0
	y_train[y_train == -1] = 1  # 共286条
	y_train[y_train == -2] = 1

	y_test[y_test == 1] = 0
	y_test[y_test == -1] = 1
	y_test[y_test == -2] = 1

# # 观察数据结构
# print(np.sum(y_train == 0))  # 稳定
# print(np.sum(y_train == 1))  # 失稳
# print()
# print(np.sum(y_test == 0))
# print(np.sum(y_test == 1))

# 5 搭建模型

# 模型创建和训练
print('Build model...')
model = Sequential()

# 第一层：1d Conv
# 		- 输入： （None, 303, 108）
#     - 输出：    (None, 303-2, num_filters=200)
#     - kernel_size = 3
model.add(Conv1D(10, 3, padding='valid', activation='relu', strides=1, input_shape=data[0].shape))

# 第二层：pooling，全局池化层
# 	    - 输出为 (None，1，num_filters=200)
model.add(GlobalMaxPooling1D())
# model.add(MaxPooling1D())  # 默认 max 步长为 2

# 第三层：hidden layer
#       - 输出为 (None，1，num_hidden_units=350)
model.add(Dense(300))
model.add(Dropout(0.5))
model.add(Activation('relu'))

# 第四层：output layer
# 方案一：3分类
# 		  - 输出为：(None, 1, 3), 并用 softmax 得到输出概率
if label_flag == 1:
	model.add(Dense(3, activation='softmax'))

	# 模型编译
	model.compile(optimizer='rmsprop',
				  loss='categorical_crossentropy',
				  metrics=['accuracy'])

# 方案二、三：2分类
#       - 输出为 (None，1，1)， 并用 sigmiod 得到输出概率
if label_flag == 2 or label_flag == 3:
	model.add(Dense(1, activation='sigmoid'))

	adam = Adam(lr=0.0005, beta_1=0.9, beta_2=0.999,epsilon=1e-8)
	# 模型编译
	model.compile(loss='binary_crossentropy',
				  optimizer=adam,
				  metrics=['accuracy'])

# metrics 还可用用下面的方式定义
# metrics = ['accuracy', 'mae'])

# 6 模型训练
train_flag = 1
if train_flag == 1:
	#  参数设置：
	batch_size = len(x_train_norm)
	epochs = 800

	model.fit(x_train_norm, y_train,
			  batch_size=batch_size,
			  epochs=epochs,
			  verbose=1,
			  validation_data=(x_test_norm, y_test))

	# print(model.summary())

	print()
	print('测试集的数据结构：', x_test_norm.shape)

	# test 1 --> predict 3 分类
	# 预测输出的是 softmax 概率，和为 1
	if label_flag == 1:
		pred_idx = 0
		x_pred = model.predict(x_test_norm[pred_idx].reshape(1, data.shape[1], data.shape[2]))
		# x_pred = model.predict(x_test_norm[pred_idx]) # 奇怪，必须按上式reshape，否则报错
		print('第 '+str(pred_idx+1)+' 个test样本的预测输出 softmax 为：\n', x_pred)
		print()
		print('预测输出 softmax 概率之和为：\n', np.sum(x_pred))
		print()
		print('预测输出的分类为：\n', (x_pred == np.max(x_pred)) * 1)
		print()
		print('实际类标签为：\n', y_test[pred_idx])
		print()

	if label_flag == 2 or label_flag == 3:
		pred_idx = 2
		x_pred = model.predict(x_test_norm[pred_idx].reshape(1, data.shape[1], data.shape[2]))
		print('第 ' + str(pred_idx + 1) + ' 个test样本的预测输出 sigmoid 为：\n', x_pred)
		print()
		print('预测输出的分类为：\n', (x_pred>0.5)*1)
		print()
		print('实际类标签为：\n', y_test[pred_idx])


	# test --> evaluate 得分
	# 输出全 测试样本的 loss 和 acc
	score = model.evaluate(x_test_norm, y_test, batch_size=16, verbose=0)
	print('test set 全样本的 loos,acc 分别为：', score)
