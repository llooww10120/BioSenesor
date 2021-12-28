# -*- coding: utf-8 -*-
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten,SimpleRNN
from sklearn.model_selection import train_test_split
import datetime
from packaging import version
import os
import tensorflow as tf
from tensorflow import keras
from preprocess import balance_data, get_test_data, load_data,drop_open_sensor
import numpy as np
print("TensorFlow version: ", tf.__version__)
assert version.parse(tf.__version__).release[0] >= 2, \
    "This notebook requires TensorFlow 2.0 or above."
X_train,X_test,y_train,y_test = load_data()

X_train = X_train.reshape(-1,3,3)       
X_test = X_test.reshape(-1,3,3) 
y_train = y_train.reshape(-1,1)
y_est = y_test.reshape(-1,1)

print(X_train.shape)
print(y_train.shape)

shape = X_train.shape
model = Sequential()
model.add(SimpleRNN(20 ,input_shape=(3,3),return_sequences=False))
  # output shape: (1, 1)
model.add((Dense(1)))    # or use model.add(Dense(1))

model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

logdir=os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)
hist = model.fit(X_train, y_train, epochs=10, batch_size=50,validation_split=0.2 , callbacks=[tensorboard_callback])
model.save('rnn.h5')
predictions = model.predict(X_test)
# get prediction result
pre = []
for i in predictions:
    if i >=0.5:
        pre.append(1)
    else:
        pre.append(0)


import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plts

score = model.evaluate(X_test, y_test,batch_size=10)
mat = confusion_matrix(y_test, pre, labels=None, sample_weight=None)

print("\t[Info] Accuracy of testing data = {:2.1f}%".format(score[1]*100.0))

print(mat)
# threshold = (1023-760)*10/27
# y=[]
# for i in range(len(X_test)):
#     x=X_test[i].reshape(9,1)
#     if x[5]> threshold:
#         y.append(1)
#     else:
#         y.append(0)
# y = np.array(y , dtype = int)
# c=0
# f=0
# for i in range(len(y)):
#     if y[i] == y_test[i]:
#         c = c+1
#     else :
#         f = f+1
# ratio = c/len(y)
# mat = confusion_matrix(y_test,y)

# print('正確率 : '+str(ratio))
# print('正確個數 : '+str(c))
# print('錯誤個數 : '+str(f))
# print('母體總數 : '+str(len(y)))
# print(str(mat))
