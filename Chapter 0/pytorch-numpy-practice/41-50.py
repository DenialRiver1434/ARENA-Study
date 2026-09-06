import numpy as np

#### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
v = np.random.random((10, 2))
x = v[:,0]; y = v[:,1]
r = np.sqrt(x * x + y * y)
t = np.arctan2(y, x)
print(np.column_stack((r, t)))

#### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)

v = np.random.random(10)
print(v)
v[v == v.max()] = 0
print(v)

#### 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)

v = np.zeros((5, 5), [('x', float), ('y', float)])

#### 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)

X = np.random.random(3)
Y = np.random.random(3)
print(X)
print(Y)
X = X[:, np.newaxis]
print(1 / (X - Y))

#### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)

X = np.random.random(10)
print(X[abs(X - 0.5).argmin()])