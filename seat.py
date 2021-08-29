import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook

def moniter():
    test = "0:23482.12"
    test = test.split(":")
    number,ohm = test
    ohm = float(ohm)
    if ohm < 8000 and ohm >100:            #潮濕
        print(number,": is wet")
    elif ohm > 8000 and ohm< 80000:          #乾燥
        print(number,": is dry")
    elif ohm > 80000 :         #錯誤_開路點
        print(number,": is open") 
    elif ohm <100:
        print(number,": is short")
