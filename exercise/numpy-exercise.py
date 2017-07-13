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
