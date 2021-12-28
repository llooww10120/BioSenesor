from numpy.lib.polynomial import RankWarning
from xgboost import XGBClassifier
from preprocess import load_data,get_x,get_y,drop_open_sensor
import pandas as pd
import numpy as np

import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plts
xgbc = XGBClassifier(objective = 'binary:logistic',
            learning_rate=0.1,
            n_estimators=2000,
            eval_metric = 'error')
X_train,X_test,y_train,y_test = load_data()

xgbc.fit(X_train,y_train)
predict = xgbc.predict(X_test)
print('accurary of XGboost',xgbc.score(X_test,y_test))

# test = pd.read_csv('./testdata/2021-10-14/1/2021-10-14.csv')
# X=[]
# for i in range(len(test)):
#     X.append(xgbc.predict( get_x(drop_open_sensor(test[i:i+1]))).reshape(21,8))
# X = get_x(drop_open_sensor(test[765:766]))
# test_y = pd.read_csv('./ml/train/test/2021-12-05_ans.csv')
# y = get_y(test_y)

# predictions =xgbc.predict(X)
# print(X[20320])
print(confusion_matrix(y_test, predict, labels=None, sample_weight=None))
# print(X)
xgbc.save_model('./ml/train/xgbc.h5')
# print(predict)