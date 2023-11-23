# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# 3. Operations on Arrays:

# Q. Add two matrices of dimensions 3x3.
arr1 = np.array([
    [4, 5, 6],
    [6, 4, 9],
    [2, 3, 7]
]) # Given
arr2 = np.array([
    [5, 9, 1],
    [3, 2, 4],
    [1, 1, 1]
]) # Given

print(arr1 + arr2) 

# OUTPUT:
# [[ 9 14  7]
#  [ 9  6 13]
#  [ 3  4  8]]

# Q. Multiply each element of an array by 2.
arr1 = np.array([
    [4, 5, 6],
    [6, 4, 9],
    [2, 3, 7]
]) # Given

arr1 = np.array(arr1)
print(arr1 * 2)

# OUTPUT:
# [[ 8 10 12]
#  [12  8 18]
#  [ 4  6 14]]

# Q. Calculate the square root of each element in an array.
arr1 = np.array([
    [4, 5, 6],
    [6, 4, 9],
    [2, 3, 7]
]) # Given

print(np.sqrt(arr1))

# OUTPUT:
# [[2.         2.23606798 2.44948974]
#  [2.44948974 2.         3.        ]
#  [1.41421356 1.73205081 2.64575131]]