import numpy as np
from numpy.random import random

import matplotlib.pyplot as plt
from scipy import misc # contains an image of a racoon!
from PIL import Image # for reading image files

my_array = np.array([1.1, 9.2, 8.1, 4.7])
# print(my_array.shape)
# print(my_array[2])
# print(my_array.ndim)

# array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

# print(f'array_2d has {array_2d.ndim} dimensions')
# print(f'Its shape is {array_2d.shape}')
# print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
# print(array_2d)
# print(array_2d[1,2])
# print(array_2d[0, :])


mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])


# print(f'We have {mystery_array.ndim} dimensions')
# print(f'The shape is {mystery_array.shape}')
# print(mystery_array[2, 1, 3])
# print(mystery_array[:, :, 0])
# print(mystery_array[2, 1, :])


# - Generating and Manipulating ndarrays

a = np.arange(10,30)
# print(a)

# # The last 3 values in the array:

# print(a[-3:])
# # An interval between two values:

# print(a[3:6])
# # All the values except the first 12:

# print(a[12:])
# # Every second value (i.e., all the even values in our case)

# print(a[::2])

# print(np.flip(a))
# # or 
# print(a[::-1])

# b = np.array([6,0,9,0,0,5,0])
# nz_indices = np.nonzero(b)
# # print(nz_indices)

# z = random((3,3,3))
# print(z)
# print(z.shape)

# - .linspace() function is very similar to .arange()
#  and great for generating evenly spaced numbers over an interval
x = np.linspace(0, 100, num=9)
# print(x)
# print(x.shape)

# y = np.linspace(start=-3, stop=3, num=9)
# plt.plot(x, y)
# plt.show()


# noise = np.random.random((128,128,3))
# print(noise.shape)
# plt.imshow(noise)
# plt.show()


# - Broadcasting, Scalars and Matrix Multiplication

# v1 = np.array([4, 5, 2, 7])
# v2 = np.array([2, 1, 3, 3])

# print(v1+v2)

# print(v1*v2)

# array_2d = np.array([[1, 2, 3, 4], 
#                      [5, 6, 7, 8]])

# print(array_2d + 10)
# print(array_2d * 5)

# Fun with Matrix Multiplication

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])
 
b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

c = np.matmul(a1, b1)
print(f'Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.')
print(c)