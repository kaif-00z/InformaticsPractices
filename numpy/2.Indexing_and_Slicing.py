# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# 2. Indexing and Slicing:

# Q. Access the element at the second row and third column of a given 2D array.
array2D = np.array([[6, 3, 7],
        [8, 9, 1]]) #Given

print(array2D[1, 2]) # OUTPUT: 1

# Q. Slice the first three elements of a 1D array.
arr = np.array([6, 3, 7, 9, 13]) #Given

print(arr[:3]) # OUTPUT: [6 3 7]

# Q. Extract the last two rows of a 3x3 array
arr2d = np.array([
    [4, 5, 6],
    [6, 4, 9],
    [2, 3, 7]
]) # Given

print(arr2d[-2:])
'''
OUTPUT:
[[6 4 9]
 [2 3 7]]
'''