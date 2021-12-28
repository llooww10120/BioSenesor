from os import write
from keras import models
from keras.models import load_model
import csv
from xgboost import XGBClassifier
from preprocess import balance_data
# model = load_model('./ml/train/model.h5')
# model.summary()
from sklearn.metrics import confusion_matrix
from preprocess import load_data,getsensorlist
import numpy as np
from preprocess import drop_open_sensor,get_x,get_y
import pandas as pd
xgbc = XGBClassifier()
xgbc.load_model('./ml/train/xgbc.h5')
# name = './ml/train/test/2021-10-14.csv'
test = pd.read_csv('./testdata/2021-10-20/1/2021-10-20.csv')
# X = get_serial_X_data(test)
X = []
for i in range(len(test)):
    X.append(get_x(drop_open_sensor(test[i:i+1])))
# X = get_x(drop_open_sensor(test))
X = np.array(X,dtype=float)
pre = []
print(X.shape)
for i in range(len(X)):
    pre.append((xgbc.predict(X[i])))
pre = np.array(pre,dtype=int)
# test_y = pd.read_csv('./ml/train/test/2021-12-05_ans.csv')
# y = get_serial_Y_data(test_y)
# y = get_y(drop_open_sensor(test_y))
# ty = []
# x_shape = X.shape
# y_shape = y.shape
# predictions = []
# for i in range(x_shape[0]):
#     for j in range(x_shape[1]):
#         predictions.append(model.predict(X[i][j]))
# predictions = np.array(predictions,dtype=float)
# for i in range(y_shape[0]):
#     for j in range(y_shape[1]):
#         ty.extend(y[i][j])

# predictions = model.predict(X)
# # get prediction result
# pred = []
# for i in predictions:
#     pre = []
#     for j in i:
#         if j >=0.5:
#             pre.append(1)
#         else:
#             pre.append(0)
#     pred.extend(pre)
# pred = np.array(pred,dtype=int)
# ty = np.array(ty,dtype=int)
# print(np.where(ty==1))
# print(np.where(pred==0))
# print(predictions)
# print(pred.shape)
# print(ty.shape)
# pred = np.array(pre,dtype=int)
# # print(y.shape)
# print(pred[0])
# mat = confusion_matrix(ty, pred, labels=None, sample_weight=None)
# print(name[-14:])
# print('Accuracy : ',(mat[0][0]+mat[1][1])/(mat[0][0]+mat[0][1]+mat[1][0]+mat[1][1]))
# print()
# X = X.reshape(20622,)
print(pre.shape)
pd_data = pd.DataFrame(pre)
pd_data.to_csv('test.csv')
# np.savetxt("test.csv", pre , delimiter=",")