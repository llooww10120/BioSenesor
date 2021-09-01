import numpy as np
import matplotlib.pyplot as plt

X=[[2,2,2],[3,3,3]]

fig = plt.figure(figsize=(10,10))
plt.imshow(X,cmap="inferno")
plt.title("Plot 2D array")
plt.colorbar()
plt.show()