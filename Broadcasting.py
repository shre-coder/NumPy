import numpy as np

# var1 = np.array([1, 2, 3, 4])
# var2 = np.array([1, 2, 3])
# print(var1 + var2)
# Give error : ValueError: operands could not be broadcast together with shapes (4,) (3,)

# var1 = np.array([1, 2, 3])
# print(var1.shape)
# print(var1)

# var2 = np.array([[1], [2], [3]])
# print(var2.shape)
# print(var2)

# print(var1 + var2)

var1 = np.array([1, 2])
var2 = np.array([[1, 2], [2, 3], [3, 4]])
print(var1 + var2)
