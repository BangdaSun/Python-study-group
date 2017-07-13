### Basic intro to Numpy
# notes of introduction to data science at datacamp
#   numpy has high speed in calculation, much more faster than built-in func

#   numpy array
#   unlike list in python, numpy array can only contrains one data type
import numpy as np
num_arr = np.array(num)

#   shape of array
num_arr.shape

#   summary statistics (here the num_arr can be viewed as vector)
np.sum(num_arr)
np.mean(num_arr)
np.sort(num_arr)
np.median(num_arr)
np.corrcoef(num_arr[:25], num_arr[25:])

#    normal random numbers (useful in many situations)
np.random.normal(loc = 2, scale = 3, size = 30)

#    reshape (by row default)
num_arr2d = num_arr.reshape((10, 5))

#   indexing and slicing
num_arr2d[0, :]
num_arr2d[:, 1]
num_arr2d[3, 4]

#   boolean expression
#   good for just one condition, with multiple conditions, use np.logical_op functions
num_arr2d > 10
np.logical_and(num_arr2d > 4, num_arr2d < 6)
