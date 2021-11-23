import numpy as np
import pandas as pd
import json
def initial():
    df = pd.read_csv(r'0800\2021-09-03.csv')
    index=[str(i) for i in range(250)]
    x=df['time']
    print(x)
    dict={}
    for i in index:
        y=df[i].to_numpy()
        sig=np.std(y,ddof=0)
        mean=np.mean(y)
        dict[i]=[mean,sig]
    with open("meanandstd.json",'w') as f:
        json.dump(dict,f)
# print(dict)

def humidtest(value,mean,sig):
    print((value-mean)/sig)

def movingaverage(data,window_size):
    sum=np.cumsum(data,dtype=int)
    sum[window_size:] = sum[window_size] - sum[:-window_size]
    return sum[window_size-1:]/window_size

if __name__=="__main__":
    name = '2021-09-07.csv'
    df  = pd.read_csv(name)
    # nmp=df['1'].rolling(10).mean()
    print(nmp)