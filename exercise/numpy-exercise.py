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
"""
Problem 21
Normalize a 5x5 random matrix
"""
x = np.random.randint(20, size = (5, 5))
(x - np.mean(x)) / np.std(x)

"""
Problem 22
Create a custom dtype that describes a color as four unsigned bytes (RGBA)
"""
color = np.dtype([('r', np.ubyte, 1),
                  ('g', np.ubyte, 1),
                  ('b', np.ubyte, 1),
                  ('a', np.ubyte, 1)])

"""
Problem 23
Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
"""
X = np.matrix(np.random.randint(10, size = (5, 3)))
Y = np.matrix(np.random.randint(20, size = (3, 2)))
X * Y
np.dot(X, Y)

"""
Problem 24
Given a 1D array, negate all elements which are between 3 and 8, in place.
"""
x = np.random.randint(11, size = 15)
x[np.logical_and(3 < x, x < 8)] *= -1 


"""
Problem 25
What is the output of the following script?
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
"""
print(sum(range(5), -1))
print(np.sum(range(5), -1))  # --> ERROR!!

"""
Problem 26
Consider an integer vector Z, which of these expressions are legal?
Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z
"""
Z = int(3)
Z ** Z
2 << Z >> 2  # bitwise operation 2 << Z: return 2 with bits shifted to the left by Z
"""
    Explaination: (<< and >> in python)
        shift each bit in its left operand to the right, 0's are produced at left
        11100101 >> 1 --> 01110010
        11100101 >> 2 --> 00111001
        11100101 >> 3 --> 00011100, >> 1 equivalent to divide 2
        
        11100101 << 1 --> 1110010100
        11100101 << 2 --> 11100101000, << 1 equivalent to multiple 2 ** 1
        (number will increase)
        
        use bin() to test
"""
Z < -Z
1j * Z
Z / 1 / 1
Z < Z > Z

"""
Problem 27
What are the result of the following expressions?
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float)
"""
np.array(0) / np.array(0)  # RuntimeWarning: divide by zero encountered in divide
np.array(0) // np.array(0)  # RuntimeWarning: divide by zero encountered in floor_divide
np.array([np.nan]).astype(int).astype(float)  # array([ -2.14748365e+09])

"""
Problem 28
How to round away from zero a float array ?
"""


"""
Problem 29
How to find common values between two arrays?
"""
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))

"""
Problem 30
How to ignore all numpy warnings (not recommended)?
"""
