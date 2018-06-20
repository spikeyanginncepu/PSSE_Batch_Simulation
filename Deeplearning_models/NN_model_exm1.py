#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 10:02
# @Author  : Yang
# @File    : NN_model_1.py
# @Software: PyCharm

from sklearn.neural_network import MLPClassifier

X = [[0., 0.], [1., 1.]]
y = [0, 1]

# 创建分类器
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

# 训练
print(clf.fit(X, y))

# 预测
print(clf.predict([[2., 2.], [-1., -2.]]))

