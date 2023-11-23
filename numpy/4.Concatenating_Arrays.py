# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# 4. Concatenating Arrays:

# Q. Concatenate two arrays vertically.
array1 = np.array([1, 3, 5]) #given
array2 = np.array([2, 4, 6]) #given

print(np.vstack((array1, array2)))
# OUTPUT: 
# [[1 3 5]
#  [2 4 6]]

# Q. Concatenate two 2D arrays horizontally.
array1 = np.array([
    [1, 3, 5],
    [4, 9, 1]
]) #given
array2 = np.array([
    [6, 2, 1],
    [0, 7, 5]
]) #given

print(np.hstack((array1, array2))) 
# OUTPUT:
# [[1 3 5 6 2 1]
#  [4 9 1 0 7 5]]


# Q. Combine multiple 1D arrays into a single 1D array.
array1 = np.array([1, 3, 5]) #given
array2 = np.array([2, 4, 6]) #given
array3 = np.array([1, 7, 2]) #given

print(np.concatenate((array1, array2, array3))) # OUTPUT: [1 3 5 2 4 6 1 7 2]

