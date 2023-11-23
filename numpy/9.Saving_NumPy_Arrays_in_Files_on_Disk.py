# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# DATA
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
]) # 2D Array
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # 1D Array 

# 9. Saving NumPy Arrays in Files on Disk:
# Q. Save a 1D array to a text file.

np.savetxt('saved_1d.txt', arr_1d)

# Q. Write a 2D array to a CSV file.

np.savetxt('saved_2d.csv', arr_2d, delimiter=',')

# Q. Save an array in binary format.

arr_2d.tofile('saved_binary.bin')