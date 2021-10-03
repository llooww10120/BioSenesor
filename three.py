import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import senserlist 
import pandas as pd
import matplotlib
import os
fig = plt.figure(figsize=(8,6))
index=[str(i) for i in range(250)]

x=[i for i in range(1,26) for j in range(1,11)]
y=[j for i in range(1,26) for j in range(1,11)]
def get_Z():
    Z_list=[]
    name='1000-1'
    date='2021-09-28'
    path='./testdata/'+date+'/'+name
    data = pd.read_csv(path+'/'+date+'.csv',engine = "python")
    for i in index:
        data[i]=data[i].rolling(10).mean()
    data = data[10:]
    
    for i in range(len(data)):
        Z_list.append(senserlist.get_one_dim(data.iloc[i][1:]))

    return Z_list
Z_list=get_Z()
ax = plt.subplot(projection="3d")
ax.scatter(x,y,Z_list[490])
plt.show()