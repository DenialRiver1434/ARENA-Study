import numpy as np
np.random.seed(42)

#### 11. Create a 3x3 identity matrix (★☆☆)
print(np.eye(3))

#### 12. Create a 3x3x3 array with random values (★☆☆)
print(np.random.random((3, 3, 3)))

#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
v = np.random.random((10, 10))
print(np.min(v), np.max(v))

#### 14. Create a random vector of size 30 and find the mean value (★☆☆)
v = np.random.random(30)
print(np.mean(v))

#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
v = np.ones((10, 10))
v[1:-1,1:-1] -= 1
print(v)

#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
v = np.random.random((5,5))
v = np.pad(v, pad_width = 1, mode = 'constant', constant_values = 0)
print(v)

#### 17. What is the result of the following expression? (★☆☆)

"""
0 * np.nan -> np.nan
np.nan == np.nan -> False
np.inf > np.nan -> False
np.nan - np.nan -> np.nan
np.nan in set([np.nan]) -> True
0.3 == 3 * 0.1 -> False
"""

#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
print(np.diag([1,2,3,4],k=-1))

#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
v = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        v[i][j] = (i + j) % 2
print(v)

#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
# (1,5,3)
np.unravel_index(99, (6,7,8))
