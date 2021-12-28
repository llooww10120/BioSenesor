import pandas as pd

data = pd.read_csv('./test.csv',engine = "python")

for i in data:
    print(i)