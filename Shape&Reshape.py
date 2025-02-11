import numpy as np

var = np.array(
    [
        [[1, 2, 3, 10], [4, 5, 6, 20], [7, 8, 9, 30]],
        [[1, 2, 3, 10], [4, 5, 6, 20], [7, 8, 9, 30]],
    ]
)
# print(var)
# print(var.shape)

var1 = np.array([1, 2, 3, 4], ndmin=5)
# print(var1)
# print(var1.shape)


# Reshape
var2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(var2)
# print(var2.ndim)

x = var2.reshape(3, 2, 2)
# print(x)
# print(x.ndim)

var3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(var3)
print(var3.ndim)

x1 = var3.reshape(3, 2, 2)
print(x1)
print(x1.ndim)

one = x1.reshape(-1)
print(one)
print(one.ndim)
