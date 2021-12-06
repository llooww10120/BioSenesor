from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np
import csv
from senserlist import getsensorlist


def hard_decision(name,threshold,name_test):
    pd.options.mode.chained_assignment = None
    df = pd.read_csv(name)
    label = df
    ax = df["time"]

    for i in range(len(ax)):
        for j in range(250):
            if df[str(j)][i] < threshold:
                label[str(j)][i] = 1
            else:
                label[str(j)][i] = 0

    for i in range(len(ax)):
        for j in range(250):
            if i > 10:
                if label[str(j)][i] == 1:
                    dist_1 = abs(df[str(j)][i-1] - df[str(j)][i])
                    dist_5 = abs(df[str(j)][i-5] - df[str(j)][i])
                    dist_10 = abs(df[str(j)][i-10] - df[str(j)][i])
                    if dist_10 > 100:
                        label[str(j)][i] = 0
                    elif dist_5 > 70:
                        label[str(j)][i] = 0
                    elif dist_1 > 50:
                        label[str(j)][i] = 0
    label.to_csv(name_test)

def get_y(label_data):
    label_list = []
    for i in range(0,len(label_data),250):    
        temp1 = getsensorlist(label_data[i:i+250])
        temp = temp1[1:-2]
        for j in temp:
            label_list.extend(j[1:-1])
    return label_list

def data(name_test,name_label):
    test = []
    right = []
    with open(name_test,'r',newline='') as csvfile:
        df_test=csv.reader(csvfile)
        for i in df_test:
            test.append(i[2:])
        
    with open(name_label,'r',newline='') as csvfile:
        df_right=csv.reader(csvfile)
        for i in df_right:
            right.append(i[1:])

    reright = right[1:]
    right_1dim = np.array([i for item in reright for i in item])
    x_ll = np.array(get_y(right_1dim))
    x_l = x_ll.astype(int)

    retest = test[1:]
    test_1dim = np.array([i for item in retest for i in item])
    for i in range(len(test_1dim)):
        test_1dim[i] = test_1dim[i].replace('.0','')

    y_ll = test_1dim.astype(int)
    y_l = get_y(y_ll)
    return x_l,y_l

def balance(y_l,x_l):
    tt = np.where(x_l==0)[0]
    drop_size=len(np.where(x_l==0)[0])-len(np.where(x_l==1)[0])
    new_y_index = np.random.choice(tt,size=drop_size,replace=False)
    new_y = np.delete(y_l,new_y_index)
    new_right = np.delete(x_l,new_y_index)
    return new_y,new_right

def compute(new_y,new_right):
    count_right = 0
    count_false = 0
    ratio = 0
    mat = confusion_matrix(new_y,new_right)
    for i in range(len(new_y)):
        if new_y[i] == new_right[i]:
            count_right = count_right+1
        elif new_y[i] != new_right[i]:
            count_false = count_false+ 1
    total = len(new_y)
    # for i in range(len(test)):
    #     for j in range(250):
    #         # print(right[i][j])
    #         if right[i][j].replace('.0','') == test[i][j].replace('.0',''):
    #             count_right = count_right+ 1
    #         elif right[i][j].replace('.0','') != test[i][j].replace('.0',''):
    #             count_false = count_false+ 1
    ratio = count_right/total
    print('正確率 : '+str(ratio))
    print('正確個數 : '+str(count_right))
    print('錯誤個數 : '+str(count_false))
    print('母體總數 : '+str(total))
    print(str(mat))

# print(len(df_test))
# for  in df_test:
#     for j in range(250):
#         if df_test 

# for i in range(len(ax)):
#     for j in range(250):
#         if df_test[str(j)][i] == df_correct[str(j)][i]:
#             count_right = count_right+ 1
#         else:
#             count_false = count_false+ 1

# ratio = count_right/total
# print(ratio)
# print(count_right)
# print(count_false)


if __name__=="__main__":
    name = "2021-12-05.csv"
    name_test = '12-05_label.csv'
    name_label = '2021-12-05label.csv'
    
    threshold = 800
    hard_decision(name,threshold,name_test)
    x_l,y_l = data(name_test,name_label)
    new_y,new_right = balance(y_l,x_l)
    compute(new_y,new_right)