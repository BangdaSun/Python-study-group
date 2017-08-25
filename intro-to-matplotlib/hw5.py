"""
Exercise 5
@author: Bangda Sun, bs2996
"""
import numpy as np
import matplotlib.pyplot as plt

"""
Problem 1.
Plot the following functions over span [0, 10]:
f(x) = e^(-x/10) sin(pi*x)
g(x) = x*e^(-x/3)
Include lablels {x-axes, y-axes}
Include legend showing which line is which plot.
"""

x = np.linspace(0, 10)
f = np.exp(-x / 10) * np.sin(np.pi * x)
g = x * np.exp(-x / 3)
plt.plot(x, f, '.-', x, g, '--')
plt.xlabel('x-axes')
plt.ylabel('y-axes')
plt.legend(('$f(x)$', '$g(x)$'))
plt.grid(True)

"""
Problem 2.
Create an array using numpy, of values spaced by .1 
with the range [0,2*pi). Assign this array to 't'.
Using the array, create points:
x = 16sin(t)
y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)
Plot your points using Matplotlib.
"""
t = np.linspace(0, 2 * np.pi, num = 2 * np.pi / 0.1)
x = 16 * np.sin(t)
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
plt.plot(t, x, '.-', t, y, '--')
plt.xlabel('$t$')
plt.ylabel('')
plt.legend(('$x(t)$', '$y(t)$'))
plt.grid(True)

"""
Problem 3.
Creating a density graph. Create one array with the following count and call it 'data':
Count -> Values
6 -> 1.3 (this means [1.3, 1.3, 1.3, 1.3, 1.3, 1.3]
2 -> 2.4
9 -> 3.1
4 -> 4.3
1 -> 5.8
10 -> 6.6
Change the array into a data frame using pandas, call this data frame 'df'.
"""
data = np.array([6, 2, 9, 4, 1, 10])
label = np.array([1.3, 2.4, 3.1, 4.3, 5.8, 6.6])
plt.bar(label, data, edgecolor = 'k', color = 'lightblue')
plt.xticks(label)

# another way
data = np.concatenate([[1.3] * 6, [2.4] * 2, [3.1] * 9, [4.3] * 4, [5.8], [6.6] * 10])
import pandas as pd
df = pd.DataFrame(data)
df.plot(kind = 'hist', edgecolor = 'k', color = 'lightblue')

"""
Problem 4.
We will be graphing two graphs in one figure. Use:
Temp : 98, 57, 69, 67, 59, 87, 59, 47, 69, 75
Speed : 269, 275, 214, 235, 214, 289, 278, 300, 345, 417
Lap : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Set appropriate labels and legends on each plot.
"""
temp = np.array([98, 57, 69, 67, 59, 87, 59, 47, 69, 75])
speed = np.array([269, 275, 214, 235, 214, 289, 278, 300, 345, 417])
lap = np.arange(1, 11)
plt.subplot(2, 1, 1)
plt.plot(temp, speed, 'o')
plt.xlabel('temp')
plt.ylabel('speed')
plt.subplot(2, 1, 2)
plt.plot(temp, lap, 'o', color = 'r', )
plt.xlabel('temp')
plt.ylabel('lap')

"""
Problem 5.
Create a sample of 100 values from the standard normal distribution(numpy), 
and create a side by side plot histogram of the PDF and the CDF of the values.
"""
x = np.random.randn(100)
plt.subplot(1, 2, 1)
plt.hist(x, edgecolor = 'k')
plt.subplot(1, 2, 2)
plt.hist(x, cumulative = True, edgecolor = 'k')

"""
Problem 6.
(3D plot)
"""
