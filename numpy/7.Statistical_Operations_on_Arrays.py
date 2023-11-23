# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# DATA
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
]) # 2D Array
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # 1D Array 

# 7. Statistical Operations on Arrays:

# Q. Find the mean value of each column in a 2D array.

print(np.mean(arr_2d, axis=0)) # OUTPUT: [5. 6. 7. 8.]

# Q. Calculate the standard deviation along rows of a 3x3 array.

print(np.std(arr_2d, axis=1)) # OUTPUT: [1.11803399 1.11803399 1.11803399]

# Q. Determine the maximum value in a 1D array.

print(np.max(arr_1d)) # OUTPUT: 9