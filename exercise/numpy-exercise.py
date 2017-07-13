""" Numpy exercise """
import numpy as np

"""
Problem 1
Print numpy configuration and version
"""
np.__config__
np.__version__


"""
Problem 2
Create a null vector of size 10
"""
np.zeros(10)


"""
Problem 3
How to find the memory size of any array 
"""
z = np.zeros((10, 10))
print('%d bytes' % (z.size * z.itemsize))  # size = 100

"""
Problem 4
How to get the documentation of the numpy add function from the command line? 
"""
help(np.add)

"""
Problem 5
Create a null vector of size 10 but the fifth value which is 1
"""
x = np.zeros(10)
x[4] = 1
x

"""
Problem 6
Create a vector with values ranging from 10 to 49 
"""
x = np.arange(10, 50)
x

"""
Problem 7
Reverse a vector (first element becomes last)
"""
x = np.arange(10)
x[::-1]


"""
Problem 8
Create a 3x3 matrix with values ranging from 0 to 8
"""
np.arange(9).reshape((3, 3))

"""
Problem 9
Find indices of non-zero elements from [1,2,0,0,4,0]
"""
x = np.array([1, 2, 0, 0, 4, 0])
np.arange(len(x))[x != 0]

# or -->
np.nonzero([1, 2, 0, 0, 4, 0])

"""
Problem 10
Create a 3x3 identity matrix 
"""
np.eye(3)

# -----------------------------------------------------------------------------
"""
Problem 11
Create a 3x3x3 array with random values
"""
np.random.rand(3, 3, 3)

"""
Problem 12
Create a 10x10 array with random values and find the minimum and maximum values
"""
x = np.random.rand(10, 10)
x.max()
x.min()

"""
Problem 13
Create a random vector of size 30 and find the mean value
"""
x = np.random.rand(30)
x.mean()


"""
Problem 14
Create a 2d array with 1 on the border and 0 inside
"""
x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
x

"""
Problem 15
How to add a border (filled with 0's) around an existing array?
"""
x = np.random.rand(5, 5) 
y = np.zeros((x.shape[0] + 2, x.shape[1] + 2))
y[1:-1, 1:-1] = x[:]
x, y

# or -->
x = np.pad(x, pad_width = 1, mode = 'constant', constant_values = 0)


"""
Problem 16
What is the result of the following expression
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 * 0.1
"""
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 * .1

"""
Problem 17
Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
"""
x = np.matrix(np.zeros((5, 5)))
for i in range(4):
    x[i+1, i] = i+1
x

# or
x = np.diag(1 + np.arange(4), k = -1)

"""
Problem 18
Create a 8x8 matrix and fill it with a checkerboard pattern
"""
x = np.zeros((8, 8), dtype = int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
x

"""
Problem 19
Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
"""
np.unravel_index(100, (6, 7, 8))  # ???


"""
Problem 20
Create a checkerboard 8x8 matrix using the tile function
"""
x = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))

# -----------------------------------------------------------------------------
