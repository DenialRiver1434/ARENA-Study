
#### 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

#### 2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)

#### 3. Create a null vector of size 10 (★☆☆)
null_vector = np.zeros(10)
print(null_vector)

#### 4. How to find the memory size of any array (★☆☆)
print(null_vector.nbytes)

#### 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
# print(np.info(np.add))

#### 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
nv1 = np.zeros(10)
nv1[4] += 1
print(nv1)

#### 7. Create a vector with values ranging from 10 to 49 (★☆☆)
v = np.arange(10, 50)
print(v)

#### 8. Reverse a vector (first element becomes last) (★☆☆)
v = v[::-1]
print(v)

#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
v = np.arange(9)
v = v.reshape(3, 3)
print(v)

#### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)

v = np.array([1,2,0,0,4,0])
print(v.nonzero())