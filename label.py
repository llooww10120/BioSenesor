from sklearn import svm
import pandas as pd
import csv
from sklearn.model_selection import train_test_split

pd.options.mode.chained_assignment = None
df = pd.read_csv("2021-11-16.csv")
label = df
ax = df["time"]

for i in range(len(ax)):
    for j in range(250):
        if df[str(j)][i] < 800:
            label[str(j)][i] = 1
        else:
            label.loc[str(j),i] = 0


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
label.to_csv("label.csv")


count_right = 0
count_false = 0
ratio = 0
test = []
right = []

with open('label11_16_right.csv','r',newline='') as csvfile:
    df_test=csv.reader(csvfile)
    for i in df_test:
        test.append(i[2:])
        

with open('label.csv','r',newline='') as csvfile:
    df_right=csv.reader(csvfile)
    for i in df_right:
        right.append(i[2:])

total = int(len(test))*250 


for i in range(len(test)):
    for j in range(250):
        # print(right[i][j])
        if right[i][j].replace('.0','') == test[i][j].replace('.0',''):
            count_right = count_right+ 1
        elif right[i][j].replace('.0','') != test[i][j].replace('.0',''):
            count_false = count_false+ 1

ratio = count_right/total
print('正確率 : '+str(ratio))
print('正確個數 : '+str(count_right))
print('錯誤個數 : '+str(count_false))
print('母體總數 : '+str(total))
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


