# github.com/kaif-00z (c) (t.me/kaif_00z) (2023)

import numpy as np # importing numpy lib in as 'np' in program

# Q. Write A Program To Merge 2 1D Arrays Into 1 1D Array And Find Median After Sorting

def main(arr1: np.ndarray, arr2: np.ndarray):
    main_arr = np.concatenate((arr1, arr2)) # Merge the arrays into a single array.
    main_arr.sort() # sorting the merged array.
    size = len(main_arr) # size of array
    # Checking Even or Odd
    if size % 2 == 1: # Which Means If The Size Is Odd
        return float(main_arr[size // 2])
    else: # Which Means If The Size Is Even Then Getting 2 Middle Number And Applying Formula
        mide1 = main_arr[size // 2 - 1]
        mide2 = main_arr[size // 2]
        return (float(mide1) + float(mide2)) / 2

print(main(np.array([1,2,6]), np.array([4,3,5])))
