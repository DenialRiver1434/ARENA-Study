import numpy as np

#### 54. How to read the following file? (★★☆)
inp = """
1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
"""

from io import StringIO
s = StringIO(inp)
Z = np.genfromtxt(s, delimiter=",", dtype = float, filling_values = np.nan)
print(Z)

#### 55. What is the equivalent of enumerate for numpy arrays? (★★☆)
v = np.arange(24).reshape(2, 3, 4)
for ind, val in np.ndenumerate(v):
    print(ind, val)

#### 82. Compute a matrix rank (★★★)

a = np.random.random(5); b = np.random.random(5)
v = np.array([a, b, 2 * a + 1.5 * b])
print(np.linalg.matrix_rank(v))
