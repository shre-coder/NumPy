import numpy as np

var = np.array([1, 2, 3, 4])
var_add = var + 3
# print(var_add)

var1 = np.array([1, 2, 3, 4])
var2 = np.array([1, 2, 3, 4])
var_add = var1 + var2
# print(var_add)

var = np.array([1, 2, 3, 4])
var_add = var - 3
# print(var_add)

var = np.array([1, 2, 3, 4])
var_add = var * 3
# print(var_add)

var = np.array([1, 2, 3, 4])
var_add = var / 3
# print(var_add)

var = np.array([1, 2, 3, 4])
var_add = var % 3
# print(var_add)

var1 = np.array([1, 2, 3, 4])
var2 = np.array([1, 2, 3, 4])
# var_add = np.add(var1, var2)
var_add = np.add(var1, 5)
# print(var_add)


# For 2-D Arrays
var21 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
var22 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
var_add = var21 + var22
# print(var_add)

var = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
var_new = var.astype(float)
var_reciprocal = np.reciprocal(var_new)

print(var_reciprocal)
