import numpy as np  
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.utils import np_utils  # 用來後續將 label 標籤轉為 one-hot-encoding  
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import load_model

data = pd.read_csv('2021-10-26.csv')
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
        [listin[220] ,listin[221] ,listin[222] ,listin[223] ,listin[231] ,listin[230] ,listin[229] ,listin[228] ,listin[227] ,listin[226]] ,    #23
        [listin[225] ,listin[224] ,listin[232] ,listin[233] ,listin[234] ,listin[235] ,listin[236] ,listin[237] ,listin[238] ,listin[239]] ,    #24
        [listin[247] ,listin[246] ,listin[245] ,listin[244] ,listin[243] ,listin[242] ,listin[241] ,listin[240] ,listin[248] ,listin[249]]]  )   #25
    return sensorlist
def convolution(data, kernel):
    data_size_x = data.shape[1]
    data_size_y = data.shape[0]
    kernel_size = kernel.shape[0]
    new_data_size_x = data_size_x-kernel_size+1
    new_data_size_y = data_size_y-kernel_size+1

    new_data = np.zeros((new_data_size_y,new_data_size_x,3,3))
    for i in range(new_data_size_y):
        for j in range(new_data_size_x):
            value=0
            for ki in range(kernel_size):
                for kj in range(kernel_size):
                    value += data[i+ki][j+kj]*kernel[ki][kj]
            new_data[i][j] = value
    return new_data
a = data[0:1]
a = a.values[0][1:]
a = getsensorlist(a)
temp = np.zeros((3,3))

y_size,x_size = a.shape

len(a[0])
re = []
for k in range(len(data)):
    d = data[k:k+1]
    for i in range(1,y_size-1):
        for j in range(1,x_size-1):
            temp = np.zeros(9)
            for ki in range(3):
                for kj in range(3):
                    temp[ki*3+kj]=a[i+ki-1][j+kj-1]
            re.append(temp)
re=np.array(re,dtype=int)
label = pd.read_csv('label10_26.csv')
label_list = []
for i in range(len(label)):
    temp = (getsensorlist(label[i:i+1].values[0][1:])[1:-1])
    for j in temp:
        label_list.extend(j[1:-1])
print(len(label_list))
x = re
y = label_list
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 33)
# # 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
# (X_train, y_train), (X_test, y_test) = mnist.load_data()


# 建立簡單的線性執行的模型
model = Sequential()
# Add Input layer, 隱藏層(hidden layer) 有 256個輸出變數
model.add(Dense(units=6, input_dim=9, kernel_initializer='normal', activation='relu')) 
# model.add(Dense(units=3, kernel_initializer='normal', activation='relu')) 
# model.add(Dense(units=128, kernel_initializer='normal', activation='relu')) 

# Add output layer
model.add(Dense(units=2, kernel_initializer='normal', activation='softmax'))

# 編譯: 選擇損失函數、優化方法及成效衡量方式
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 

# 將 training 的 label 進行 one-hot encoding，例如數字 7 經過 One-hot encoding 轉換後是 0000001000，即第7個值為 1
y_TrainOneHot = np_utils.to_categorical(y_train) 
y_TestOneHot = np_utils.to_categorical(y_test) 

# 將 training 的 input 資料轉為2維
# X_train_2D = X_train.reshape(60000, 28*28).astype('float32')  
# X_test_2D = X_test.reshape(10000, 28*28).astype('float32')  

# x_Train_norm = X_train_2D/255
# x_Test_norm = X_test_2D/255

# 進行訓練, 訓練過程會存在 train_history 變數中
train_history = model.fit(x=X_train, y=y_TrainOneHot, validation_split=0.2, epochs=10, batch_size=800, verbose=2)  

# 顯示訓練成果(分數)
scores = model.evaluate(X_test, y_TestOneHot)  
print()  
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))  

# 預測(prediction)
X = X_test[0:,:]
predictions = np.argmax(model.predict(X), axis=-1)
# get prediction result
print(predictions)
test = np.array([[800,800,863,800,600,800,800,800,830]])
predictions = np.argmax(model.predict(test), axis=-1)
print(predictions)
model.save('model.h5')