# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# 1. Array Creation:
# Q. Create a NumPy array from a Python list [1, 2, 3, 4, 5].

array = np.array([1, 2, 3, 4, 5])
print(array) # OUTPUT: [1 2 3 4 5]

# Q. Create a 2D array with dimensions 3x4 filled with zeros.

array2D = np.zeros((3, 4))
print(array2D)
'''
OUTPUT: [[0. 0. 0. 0.]
         [0. 0. 0. 0.]
         [0. 0. 0. 0.]]
'''

# Q. Generate an array of integers from 0 to 9.

array_ = np.arange(10)
print(array_) # OUTPUT: [0 1 2 3 4 5 6 7 8 9]