import numpy as np
a = np.array([1,2,3,4])
print(a)

b = a.reshape(2,2)  # 2 x 2 is 4 which is the size of array a
print(b)  # This is the multidim array we got

# Another method to create array
a = np.arange(24)
print(a)

b = a.reshape(2,4,3)
print(b)

# Array of zeros

x = np.zeros(5)
print(x)  # we got float 0s ie 0.

x = np.zeros(5,dtype=int)
print(x)