# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# 6. Splitting Arrays:

# DATA
# DATA
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
]) # 2D Array
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # 1D Array 

# Q. Split a 2D array into two along columns.

print(np.hsplit(arr_2d, 2))

# OUTPUT:
# [array([[ 1,  2],
#        [ 5,  6],
#        [ 9, 10]]),
#  array([[ 3,  4],
#        [ 7,  8],
#        [11, 12]])]

# Q. Split a 2D array into three along rows.

print(np.vsplit(arr_2d, 3)) # OUTPUT: [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]])]

# Q. Divide a 1D array into three equal parts.

print(np.array_split(arr_1d, 3)) # OUTPUT: [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]