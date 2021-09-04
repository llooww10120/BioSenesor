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

if __name__=="__main__":
    with open('./meanandstd.json','r') as f:
        dic=json.load(f)
    mean,sig=(dic['11'])
    print((938-mean)/sig)
    # initial()