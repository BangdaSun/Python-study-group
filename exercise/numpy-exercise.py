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
Problem 16X
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
Problem 17X
Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
"""
x = np.matrix(np.zeros((5, 5)))
for i in range(4):
    x[i+1, i] = i+1
x

# or
x = np.diag(1 + np.arange(4), k = -1)

"""
Problem 18X
Create a 8x8 matrix and fill it with a checkerboard pattern
"""
x = np.zeros((8, 8), dtype = int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
x

"""
Problem 19X
Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
"""
np.unravel_index(100, (6, 7, 8))  # ???


"""
Problem 20X
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
Problem 22X
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
Problem 29X
How to find common values between two arrays?
"""
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))

"""
Problem 30
How to ignore all numpy warnings (not recommended)?
"""

# -----------------------------------------------------------------------------
"""
Problem 31
Is the following expressions true? 
np.sqrt(-1) == np.emath.sqrt(-1)
"""
np.sqrt(-1)  # nan
np.emath.sqrt(-1)  # 1j

"""
Problem 32X
How to get the dates of yesterday, today and tomorrow?
"""
today = np.datetime64('today', 'D')
yesterday = today - np.timedelta64(1, 'D')
tomorrow  = today + np.timedelta64(1, 'D')

"""
Problem 33
How to get all the dates corresponding to the month of July 2016?
"""
alldate = np.arange('2016-07-01', '2016-08-01', dtype = 'datetime64')
alldate
# or
alldate = np.arange('2016-07', '2016-08', dtype = 'datetime64[D]')
alldate

"""
Problem 34
How to compute ((A+B)*(-A/2)) in place (without copy)?
"""
A = 1
B = 3
np.multiply(np.add(A, B), np.divide(-A, 2))

"""
Problem 35
Extract the integer part of a random array using 5 different methods
"""
x = 5. * np.random.randn(5)
np.floor(x)
np.trunc(x)
[int(i) for i in x]
x.astype(int)
x - x % 1

"""
Problem 36
Create a 5x5 matrix with row values ranging from 0 to 4
"""
np.matrix(np.random.randint(0, 5, size = (5, 5)))
# or
x = np.zeros((5, 5))
x += np.arange(5)

"""
Problem 37X
Consider a generator function that generates 10 integers and use it to build an array
"""
def generateInt(min, max):
    return np.random.randint(min, max, size = 10)

np.array(generateInt(0, 10))
# or
def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)

"""
Problem 38
Create a vector of size 10 with values ranging from 0 to 1, both excluded
"""
np.linspace(0, 1, 11, endpoint = False)[1:]

"""
Problem 39
Create a random vector of size 10 and sort it
"""
x = np.random.randn(10)
np.sort(x)

"""
Problem 40X
How to sum a small array faster than np.sum?
"""
x = np.arange(10)
np.add.reduce(x)

# -----------------------------------------------------------------------------
"""
Problem 41X
Consider two random array A and B, check if they are equal
"""
A = np.random.randn(5)
B = np.random.randn(5)
np.equal(A, B)
np.sum(A == B) == 5
np.array_equal(A, B)

"""
Problem 42X
Make an array immutable (read-only)
"""
z = np.zeros(10)
z.flags.writeable = False
z[0] = 1

"""
Problem 43
Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates
"""
x = np.random.randn(10, 2)
X, Y = x[:, 0], x[:, 1]
R = np.sqrt(X ** 2 + Y ** 2)
T = np.arctan2(Y, X)
print(R, T)

"""
Problem 44X
Create random vector of size 10 and replace the maximum value by 0
"""
x = np.random.randn(10)
x[x == x.max()] = 0
x[x.argmax()] = 0

"""
Problem 45X
Create a structured array with x and y coordinates covering the [0,1]x[0,1] area
"""
Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0, 1, 5),
                             np.linspace(0, 1, 5))

"""
Problem 46
Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))
"""
X = np.array([2., 3., 4., 5.])
Y = np.array([7., 8., 9., 1.])
C = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        C[i, j] = 1 / (X[i] - Y[j])
        
        
"""
Problem 47
Print the minimum and maximum representable value for each numpy scalar type
"""

"""
Problem 48
How to print all the values of an array?
"""


"""
Problem 49
How to find the closest value (to a given scalar) in a vector?
"""
x = np.random.randn(10)
s = .52
x[np.abs(x - s).argmin()]

"""
Problem 50
Create a structured array representing a position (x,y) and a color (r,g,b) 
"""

# -----------------------------------------------------------------------------
"""
Problem 51X
Consider a random vector with shape (100,2) representing coordinates, find point by point distances
"""
X = np.random.randn(100, 2)

# with scipy
import scipy
import scipy.spatial
D = scipy.spatial.distance.cdist(X, X)

"""
Problem 52
How to convert a float (32 bits) array into an integer (32 bits) in place?
"""
x = np.array([1, 2, 3], dtype = 'float32')
x.astype('int32', copy = False)

"""
Problem 53X
How to read the following file?
1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
"""
# use readLine or...
s = StringIO("""1, 2, 3, 4, 5\n
                6,  ,  , 7, 8\n
                 ,  , 9,10,11\n""")
Z = np.genfromtxt(s, delimiter=",", dtype=np.int)
print(Z)
 
"""
Problem 54X
What is the equivalent of enumerate for numpy arrays?
"""
# ndenumerate
# ndindex(.shape)

"""
Problem 55
Generate a generic 2D Gaussian-like array
"""
X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
D = np.sqrt(X **2  + Y ** 2)
sigma, mu = 1., 0.
G = np.exp(- (D - mu)**2 / (2. * sigma ** 2))

"""
Problem 56X
How to randomly place p elements in a 2D array?
"""
p = np.array([1, 2, 3, 4])
X = np.zeros((5, 5))
X.shape
idx = np.random.randint(low = 0, high = X.shape[0], size = len(p))
idy = np.random.randint(low = 0, high = X.shape[1], size = len(p))
X[idx, idy] = p
X
# or use ... np.put(), np.random.choice()

"""
Problem 57
Subtract the mean of each row of a matrix
"""
X = np.matrix(np.array([[1, 2, 4],
                        [0, 1, 3],
                        [3, 2, 2]]))
X - X.mean(axis = 1)  # 1 is horizontal, in R 1 is vertical

"""
Problem 58X
How to sort an array by the nth column? 
"""
X = np.array([[1, 2, 5],
              [3, 1, 4],
              [4, 3, 1]])
X[X[:, 1].argsort()]
    
"""
Problem 59X
How to tell if a given 2D array has null columns? 
"""
np.isnan(X)
# or...

"""
Problem 60
Find the nearest value from a given value in an array
"""
element = 0.3
X = np.random.randn(5, 3)
X.flat[np.abs(X - element).argmin()]

# X.flat --> expand X by row default
# -----------------------------------------------------------------------------
"""
Problem 61
Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator?
"""


"""
Problem 62X
Create an array class that has a name attribute 
"""
class array(object):
    def __init__(self, name):
        self.name = name;

# solution
class NamedArray(np.ndarray):
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', "no name")

Z = NamedArray(np.arange(10), "range_10")
print (Z.name)

"""
Problem 63
Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? 
"""

"""
Problem 64
How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? 
"""
# use np.bincount()

"""
Problem 65
Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors 
"""
# use np.bincount()

"""
Problem 66X
Considering a four dimensions array, how to get sum over the last two axis at once?
"""
X = np.random.randn(2, 2, 2, 2)
X.sum(axis=(-2, -1))
X.sum(axis=(2, 3))

"""
Problem 67
Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset indices? 
"""
D = np.array([1, 3, 6, 3, 2, 5, 6])
S = np.random.randint(0, len(D), size = len(D))
D[S].mean()

"""
Problem 68
How to get the diagonal of a dot product?
"""
X = np.matrix(np.array([[1, 0],
                        [3, 5]]))
Y = np.matrix(np.array([[1, 5],
                        [6, 4]]))
np.dot(X, Y).diagonal()

# or use np.bincount()


"""
Problem 69
Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? 
"""
x = [1, 2, 3, 4, 5]
char = '000'.join(str(i) for i in x)
lst = []
for i in char:
    lst.append(int(i))

# or
Z = np.array([1,2,3,4,5])
nz = 3
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print(Z0)

"""
Problem 70 X
71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)?
"""
X = np.random.randn(5, 5, 3)
Y = np.random.randn(5, 5)
X * Y[:, :, None]

"""
Problem 71
How to swap two rows of an array? 
"""
X = np.array([[1, 3, 4, 5],
              [4, 2, 3, 1]])

for i in range(X.shape[1]):
    X[0, i], X[1, i] = X[1, i], X[0, i] 

# or
X[[1, 0], :] = X[[0, 1], :]
