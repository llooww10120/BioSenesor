# -*- coding: utf-8 -*-
import pandas as pd
from glob import glob
import numpy as np

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from sklearn.model_selection import train_test_split

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
import datetime
from packaging import version
import os
import tensorflow as tf
from tensorflow import keras


import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plts
kernel=np.array([[1,1,1],[5,10,5],[1,1,1]])/26
re_kernel=np.array([[1,1,1],[1,0,1],[1,1,1]])/8
def getsensorlist(listin):
    sensorlist = np.array([[listin[7]   ,listin[6]   ,listin[5]   ,listin[4]   ,listin[3]   ,listin[2]   ,listin[1]   ,listin[0]   ,listin[11]  ,listin[10]]  , #1
        [listin[9]  ,listin[8]   ,listin[12]  ,listin[13]  ,listin[14]  ,listin[15]  ,listin[23]  ,listin[22]  ,listin[21]  ,listin[20]]  , #2
        [listin[16]  ,listin[17]  ,listin[18]  ,listin[19]  ,listin[24]  ,listin[25]  ,listin[26]  ,listin[27]  ,listin[28]  ,listin[29]]  ,    #3
        [listin[30]  ,listin[31]  ,listin[39]  ,listin[38]  ,listin[37]  ,listin[36]  ,listin[35]  ,listin[34]  ,listin[33]  ,listin[32]]  ,    #4
        [listin[40]  ,listin[41]  ,listin[42]  ,listin[43]  ,listin[44]  ,listin[45]  ,listin[46]  ,listin[47]  ,listin[55]  ,listin[54]]  ,    #5
        [listin[53]  ,listin[52]  ,listin[51]  ,listin[50]  ,listin[49]  ,listin[48]  ,listin[56]  ,listin[57]  ,listin[58]  ,listin[59]]  ,    #6 
        [listin[60]  ,listin[61]  ,listin[62]  ,listin[63]  ,listin[71]  ,listin[70]  ,listin[69]  ,listin[68]  ,listin[67]  ,listin[66]]  ,    #7
        [listin[65]  ,listin[64]  ,listin[72]  ,listin[73]  ,listin[74]  ,listin[75]  ,listin[76]  ,listin[77]  ,listin[78]  ,listin[79]]  ,    #8
        [listin[87]  ,listin[86]  ,listin[85]  ,listin[84]  ,listin[83]  ,listin[82]  ,listin[81]  ,listin[80]  ,listin[88]  ,listin[89]]  ,    #9
        [listin[90]  ,listin[91]  ,listin[92]  ,listin[93]  ,listin[94]  ,listin[95]  ,listin[103] ,listin[102] ,listin[101] ,listin[100]] ,    #10
        [listin[99]  ,listin[98]  ,listin[97]  ,listin[96]  ,listin[104] ,listin[105] ,listin[106] ,listin[107] ,listin[108] ,listin[109]] ,    #11
        [listin[110] ,listin[111] ,listin[119] ,listin[118] ,listin[117] ,listin[116] ,listin[115] ,listin[114] ,listin[113] ,listin[112]] ,    #12
        [listin[120] ,listin[121] ,listin[122] ,listin[123] ,listin[124] ,listin[125] ,listin[126] ,listin[127] ,listin[135] ,listin[134]] ,    #13
        [listin[133] ,listin[132] ,listin[131] ,listin[130] ,listin[129] ,listin[128] ,listin[136] ,listin[137] ,listin[138] ,listin[139]] ,    #14
        [listin[140] ,listin[141] ,listin[142] ,listin[143] ,listin[151] ,listin[150] ,listin[149] ,listin[148] ,listin[147] ,listin[146]] ,    #15
        [listin[145] ,listin[144] ,listin[152] ,listin[153] ,listin[154] ,listin[155] ,listin[156] ,listin[157] ,listin[158] ,listin[159]] ,    #16
        [listin[167] ,listin[166] ,listin[165] ,listin[164] ,listin[163] ,listin[162] ,listin[161] ,listin[160] ,listin[168] ,listin[169]] ,    #17
        [listin[170] ,listin[171] ,listin[172] ,listin[173] ,listin[174] ,listin[175] ,listin[183] ,listin[182] ,listin[181] ,listin[180]] ,    #18
        [listin[179] ,listin[178] ,listin[177] ,listin[176] ,listin[184] ,listin[185] ,listin[186] ,listin[187] ,listin[188] ,listin[189]] ,    #19
        [listin[190] ,listin[191] ,listin[199] ,listin[198] ,listin[197] ,listin[196] ,listin[195] ,listin[194] ,listin[193] ,listin[192]] ,    #20
        [listin[200] ,listin[201] ,listin[202] ,listin[203] ,listin[204] ,listin[205] ,listin[206] ,listin[207] ,listin[215] ,listin[214]] ,    #21
        [listin[213] ,listin[212] ,listin[211] ,listin[210] ,listin[209] ,listin[208] ,listin[216] ,listin[217] ,listin[218] ,listin[219]] ,    #22
        [listin[220] ,listin[221] ,listin[222] ,listin[223] ,listin[231] ,listin[230] ,listin[229] ,listin[228] ,listin[227] ,listin[226]]])
    return sensorlist

def drop_open_sensor(data):
    new_data = []
    for i in range(len(data)):
        new_data.append(getsensorlist(data[i:i+1].values[0][1:]))
    new_data = np.array(new_data,dtype = int)
    shape = new_data.shape
    for i in range(shape[0]):
        for j in range(1,shape[1]-1):
            for k in range(1,shape[2]-1):
                if new_data[i][j][k] == 1023:
                    temp = 0
                    c= 0
                    for ki in range(3):
                        for kj in range(3):
                            kk = new_data[i][j+ki-1][k+kj-1]
                            if kk != 1023:
                                temp += new_data[i][j+ki-1][k+kj-1]*re_kernel[ki][kj]
                                c +=1
                    new_data[i][j][k] = temp/c
    return new_data
def get_gaussian_kernel():
    x,y=np.mgrid[-1:2,-1:2]
    kernal=np.exp(-(x**2+y**2))
    return kernal/kernal.sum()
def get_x(data):
    l,y_size,x_size = data.shape
    re = []
    for k in range(l):
        d = data[k]
        for i in range(1,y_size-1):
            for j in range(1,x_size-1):
                temp =[]
                for ki in range(3):
                    for kj in range(3):
                        temp.append((1-(d[i+ki-1][j+kj-1])/1023)*kernel[ki][kj])
                re.append(temp)
    # re=np.array(re,dtype=float)
    return re

def load_data():
    files = glob('./ml/train/data/*.csv')
    read_files=[]
    ans_files=[]
    for i in files:
        read_files.append(drop_open_sensor(pd.read_csv(i)))
        ans_files.append(pd.read_csv(i.replace('data','ans')[:-4]+'_ans.csv'))
    x=[]
    for i in read_files:
        x.extend(get_x(i))

    x=np.array(x,dtype=float)

    y=[]
    for i in ans_files:
        y.extend(get_y(i))
    y = np.array(y,dtype=int)

    new_x,new_y = balance_data(x,y)

    X_train,X_test,y_train,y_test = train_test_split(new_x,new_y,test_size = 0.25,random_state = 33)
    print('X_train:',X_train.shape)
    print('X_test:',X_test.shape)
    print('y_train:',y_train.shape)
    print('y_test:',y_test.shape)

    return X_train,X_test,y_train,y_test
def get_y(label_data):
    label_list = []
    for i in range(len(label_data)):
        temp = (getsensorlist(label_data[i:i+1].values[0][1:])[1:-1])
        for j in temp:
            label_list.extend(j[1:-1])
    return label_list


def balance_data(x,y):
    tt = np.where(y==0)[0]

    drop_size=len(np.where(y==0)[0])-len(np.where(y==1)[0])
    new_y_index = np.random.choice(tt,size=drop_size,replace=False)
    new_y = np.delete(y,new_y_index)
    new_x = np.delete(x,new_y_index,axis=0)
    return new_x,new_y

def get_test_data(xpath,ypath):
    data = pd.read_csv(xpath)
    tx = get_x(drop_open_sensor(data))
    tx =  np.array(tx,dtype= float)
    test_y = pd.read_csv(ypath)
    ty = get_y(test_y)
    ty = np.array(ty,dtype=int)

    return balance_data(tx,ty)
def get_serial_X_data(data):
    da = drop_open_sensor(data)
    l,y,x = da.shape
    new_data = np.zeros((y-2,x-2,l,3,3))
    for j in range(1,y-1):
        for k in range(1,x-1):
            for i in range(l):
                for ki in range(3):
                    for kj in range(3):
                        new_data[j-1][k-1][i][ki][kj] = da[i][j+ki-1][k+kj-1]*kernel[ki][kj]
    return new_data

def get_serial_Y_data(label_data):
    label_list = []
    for i in range(len(label_data)):
        temp = (getsensorlist(label_data[i:i+1].values[0][1:]))
        label_list.append(temp)
    label_list = np.array(label_list,dtype=int)
    y_l,y_y,y_x = label_list.shape
    new_label = np.zeros((y_y-2,y_x-2,y_l))
    for j in range(1,y_y-1):
        for k in range(1,y_x-1):
            for i in range(y_l):
                new_label[j-1][k-1][i] = label_list[i][j][k]
    return new_label
if __name__ == '__main__':
    print('')
    xpath = './ml/train/test/2021-12-04_3.csv'
    ypath = './ml/train/test/2021-12-04_3_ans.csv'
    tx,ty = get_test_data(xpath,ypath)