import numpy as np

#### 32. Is the following expressions true? (★☆☆)
print(np.sqrt(-1))
print(np.emath.sqrt(-1))

#### 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)
A = np.random.random(10) * 10
print(np.floor(A))
print(A - A % 1)
print(A // 1)

#### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)

v = np.zeros((5,5))
v += np.arange(5)
