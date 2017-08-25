"""
Exercise 3
@author: Bangda Sun, bs2996
"""
import numpy as np

"""
Problem 1:
Create a 2-D array below without typing it in explicitly.
[[1, 6, 11],
[2, 7, 12],
[3, 8, 13],
[4, 9, 14],
[5, 10, 15]]
Hint: Use np.arange and np.reshape
"""
x = np.arange(1, 16)
x = np.transpose(x.reshape(3, 5))
print x

"""
Problem 2 - 1:
Create a diagnal matrix array shown below.
[ 1., 0., 0.],
[ 0., 1., 0.],
[ 0., 0., 1.]
"""
x = np.eye(3)
print x

"""
Problem 2 - 2:
Create a diagnal matrix with 1-5 as shown below.
[1, 0, 0, 0, 0],
[0, 2, 0, 0, 0],
[0, 0, 3, 0, 0],
[0, 0, 0, 4, 0],
[0, 0, 0, 0, 5]
"""
x = np.diag(np.arange(1, 6))
print x

"""
Problem 3:
Create two arrays
x = [1, 2, 4, 1]
y = [1, 2, 3]
[5, 6, 1]
And find the mean of X, median of X, median of Y, and standard dev. of X with 1 less degree of freedom.
"""
x = np.array([1, 2, 4, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
print "mean of X: ", x.mean()                  # Or np.mean(x)
print "median of X: ", np.median(x) 
print "median of Y: ", np.median(y, axis = -1) 
print "standard dev of X: ", x.std(ddof = 1)    # Or np.std(x)

"""
Problem 4:
Create an 1D array with 15 numbers. (must use NumPy) For all numbers between 3 and 8, make them
negative.
"""
x = np.random.randint(-8, -2, 15)
print x
x[(x > 3) & (x <= 8)] *= -1
# Alternative method
z = np.arange(15)
z[(3 < z) & (z <= 8)] *= -1

"""
Problem 5:
Set the seed as follows before doing this problem:
numpy.random.seed(seed=32)
• Create an random array of 10 elements drawn between [0,10] using a uniform distribution.
• Extract the integer parts of the your random array using three methods.
One is done for you:
# Z is your 10 element array
# Z = [ ... ]
print (np.trunc(Z))
At least one must use NumPy.
"""
np.random.seed(seed = 32)
z = np.random.random(10) * 10
print z
print np.array(z, dtype = int)   # z.astype(int)
print np.trunc(z)
print np.floor(z)
print np.ceil(z)
print (z - z%1)

"""
Problem 6:
• Create a random 8x2 matrixfrom the continuous uniform distribution.
• Convert them to polar coordinates.
• Print.
"""
x = np.random.random((8, 2))
r = np.sqrt(x[:, 0]**2 + x[:, 1]**2)
print x
theta = np.arctan(x[:, 1] / x[:, 0])
print np.array([r, theta]).transpose()
# Alternative method
theta = np.arctan2(x[:, 1], x[:, 0])
print theta

"""
Problem 7:
Use seed = 3.
numpy.random.seed(seed=3)
• Create a random uniform matrix that is 10x10, ith elements ranging from 0 to 1.
• Compute the rank of the matrix.
Hint: Use np.linalg.svd() to get the Singular Value Decomposition.
"""
np.random.seed(seed = 3)
x = np.random.random((10, 10))
x = np.matrix(x)
print np.linalg.matrix_rank(x)
# Alternative method
U, S, V = np.linalg.svd(x)
rank = np.sum(S > 1e-10)
print rank

"""
Problem 8:
Using the following 1D array, (make sure to set seed = 4)
K = np.random.randn(100)
• Resample the elements of K with replacement 1000 times.
• Compute the mean of each sample.
• Using each mean compute the 95% confidence interval.
• Print out the confidence interval
"""
np.random.seed(seed = 4)
K = np.random.randn(100)
sample = np.zeros((1000, 100))
for i in range(1000):
    sample[i] = np.random.choice(K, size = 100, replace = True)

mean = np.mean(sample, axis = 0)
lower = mean - 1.96 * np.std(sample, axis = 0) / 10 
upper = mean + 1.96 * np.std(sample, axis = 0) / 10
print np.array([lower, upper]).transpose()
# Alternative method
idx = np.random.randint(0, K.size, (1000, K.size))
means = K[idx].mean(axis = 1)
confint = np.percentile(means, [2.5, 97.5])
print confint
