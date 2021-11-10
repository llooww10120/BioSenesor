from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split


df = pd.read_csv("2021-10-22.csv")
label = df
ax = df["time"]

for i in range(len(ax)):
    for j in range(250):
        if df[str(j)][i] < 890:
            label[str(j)][i] = 1
        else:
            label[str(j)][i] = 0


label.to_csv("label.csv")

