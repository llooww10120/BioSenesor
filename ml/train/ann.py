from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
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
model = Sequential()
# Add Input layer, 隱藏層(hidden layer) 有 256個輸出變數
model.add(Dense(units=128, input_dim=9, kernel_initializer='normal', activation='relu')) 
# Add output layer
model.add(Dense(units=2, kernel_initializer='normal', activation='softmax'))

# 編譯: 選擇損失函數、優化方法及成效衡量方式
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 
x_Train_norm = X_train
x_Test_norm = X_test

y_TrainOneHot = np_utils.to_categorical(y_train) 
y_TestOneHot = np_utils.to_categorical(y_test)

logdir=os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)
train_history = model.fit(x=x_Train_norm, y=y_TrainOneHot, validation_split=0.2, epochs=10, batch_size=800, verbose=2, callbacks=[tensorboard_callback])

scores = model.evaluate(X_test, y_TestOneHot)  
print()  
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))

X = x_Test_norm[0:,:]
predictions = np.argmax(model.predict(X), axis=-1)
# get prediction result
np.set_printoptions(threshold=100)
print(predictions)

import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plts

np.sum((y_test==1))

confusion_matrix(y_test, predictions, labels=None, sample_weight=None)

# model.save('/content/drive/MyDrive/train/model.h5')

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs
xpath = './ml/train/test/2021-12-05.csv'
ypath = './ml/train/test/2021-12-05_ans.csv'
tx,ty = get_test_data(xpath,ypath)

new_tx,new_ty = balance_data(tx,ty)

new_y_TrainOneHot = np_utils.to_categorical(new_ty) 


scores = model.evaluate(new_tx,new_y_TrainOneHot,batch_size=100)

print()  
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))

nn_predictions = np.argmax(model.predict(new_tx), axis=-1)
print(confusion_matrix(new_ty, nn_predictions, labels=None, sample_weight=None))

