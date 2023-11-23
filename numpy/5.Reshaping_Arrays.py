# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# 5. Reshaping Arrays:

# Q. Reshape a 1D array into a 2D array with dimensions 3x4.

arr1D = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # Always Take Like Wise Size Of Array Here I Have Taken an array of length 12 which is also equal to 3x4=12
print(arr1D.reshape(3, 4))
# OUTPUT:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Q. Flatten a 2D array into a 1D array.

arr2D = np.array(
    [[1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12]]
)
print(arr2D.flatten()) # OUTPUT: [ 1  2  3  4  5  6  7  8  9 10 11 12]

# Q. Convert a 1D array to a column vector.

arr1D = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr1D[:, np.newaxis])
# OUTPUT:
# [[ 1]
#  [ 2]
#  [ 3]
#  [ 4]
#  [ 5]
#  [ 6]
#  [ 7]
#  [ 8]
#  [ 9]
#  [10]
#  [11]
#  [12]]