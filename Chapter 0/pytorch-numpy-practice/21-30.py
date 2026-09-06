import numpy as np

#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
print(np.tile([[0, 1], [1, 0]], (4,4)))

#### 22. Normalize a 5x5 random matrix (★☆☆)
v = np.random.random((5, 5))
v = (v - np.mean (v)) / (np.std (v))
print(v)

#### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
a = np.random.random((5, 3))
b = np.random.random((3, 2))
print(a @ b)

#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
v = np.random.random(10)
v[2:8] *= -1
print(v)
# If it means values between 3, 8
v = 10 * np.random.random(10)
v[(v > 3) & (v < 8)] *= -1
print(v)


#### 26. What is the output of the following script? (★☆☆)
"""
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
"""
print(np.sum(np.arange(15).reshape(3,5),0))


#### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
"""
Z**Z ok
2 << Z >> 2 ok
Z <- Z ok it is Z < (-Z)
1j*Z ok
Z/1/1 ok
Z<Z>Z no
"""

#### 30. How to find common values between two arrays? (★☆☆)

a = np.array([3, 4, 4, 9, 2])
b = np.array([2, 4, 5, 8])
print(np.intersect1d(a, b))
