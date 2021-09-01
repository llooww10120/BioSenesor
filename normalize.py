from sklearn import preprocessing
import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
# wb=load_workbook('text1.xlsx')
# sheet=wb["Sheet"]
# a=sheet["A"]
# b=sheet["M"]
df = pd.read_csv('text1.xlsx')
# minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
# data_minmax = minmax.fit_transform(df)
print(df.head().decode().replace('\n',''))