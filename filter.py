import numpy as np
import matplotlib.pyplot as plt
def get_gaussian_kernel():
    x,y=np.mgrid[-1:2,-1:2]
    kernal=np.exp(-(x**2+y**2))
    return kernal/kernal.sum()
def convolution(data, kernel):
    data_size_x = data.shape[1]
    data_size_y = data.shape[0]
    kernel_size = kernel.shape[0]
    new_data_size_x = data_size_x-kernel_size+1
    new_data_size_y = data_size_y-kernel_size+1

    new_data = np.zeros((new_data_size_y,new_data_size_x))
    for i in range(new_data_size_y):
        for j in range(new_data_size_x):
            value=0
            for ki in range(kernel_size):
                for kj in range(kernel_size):
                    value += data[i+ki][j+kj]*kernel[ki][kj]
            new_data[i][j] = value
    return new_data
if __name__=="__main__":
    kernal = get_gaussian_kernel()
    test = np.array([[1023,1023,1023,1023,1023],
                     [1023,900,820,822,1023],
                     [1023,800,779,810,1023],
                     [1023,815,844,822,1023],
                     [1023,1023,1023,1023,1023],
                     [1023,1023,1023,1023,1023]])
    # kernal = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    kernal = np.ones((2,2))/4
    new = convolution(test,kernal)
    print(new)
    # plt.imshow(test)