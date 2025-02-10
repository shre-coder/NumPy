import numpy as np

var = np.array([1, 2, 3, 4, 5, 6, 7, 45, 78])

# print("Data Type : ", var.dtype)

var = np.array([1.5, 2.0, 3.5, 4.5])

# print("Data Type : ", var.dtype)

var = np.array(["A", "b", "C"])

# print("Data Type : ", var.dtype)

var = np.array(["A", "b", "C", 1, 2])

# print("Data Type : ", var.dtype)

x = np.array([1, 2, 3, 4], dtype=np.int8)

# print("Data Type : ", x.dtype)
# print(x)

x1 = np.array([1, 2, 3, 4], dtype="f")

# print("Data Type : ", x1.dtype)
# print(x1)

x2 = np.array([1, 2, 3, 4])

new = np.float32(x)

new_one = np.int_(new)

# print("Data Type : ", x2.dtype)
# print("Data Type : ", new.dtype)
# print("Data Type : ", new_one.dtype)
# print(x2)
# print(new)
# print(new_one)

x3 = np.array([1, 2, 3, 4])

new_1 = x3.astype(float)
print(x3)
print(new_1)
