# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# 8. Loading Arrays from Files:

# Q. Load a 2D array from a CSV file.

csv_data = np.genfromtxt('saved_2d.csv', delimiter=',')

# Q. Read a text file containing integers into a NumPy array.

text_data = np.loadtxt('saved_1d.txt')

# Q. Load an array from a binary file.

binary_data = np.fromfile('saved_binary.bin', dtype=np.int32) # Depends 