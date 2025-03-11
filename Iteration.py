import numpy as np

var = np.array([9, 8, 7, 6, 5, 4])
# print(var)

# for i in var:
# print(i)

var1 = np.array([[1, 2, 3, 4], [9, 8, 7, 6]])

# for j in var1:
#     print(j)

# for k in var1:
#     for l in k:
#         print(l)

var2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# print(var2.ndim)

# for i in var2:
#     for j in i:
#         for k in j:
#             print(k)

var2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

# for i in np.nditer(var2, flags=["buffered"], op_dtypes=["S"]):
#     print(i)

for i, d in np.ndenumerate(var2):
    print(i, d)
