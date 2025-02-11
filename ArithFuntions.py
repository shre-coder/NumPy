import numpy as np

var = np.array([1, 2, 3, 4, 7, 8, 6, 50, 55, 80, 90])
# print("min : ", np.min(var), "position : ", np.argmin(var))
# print("max : ", np.max(var), "position : ", np.argmax(var))


var_33 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
min_var_row = np.min(var_33, axis=1)
min_var_col = np.max(var_33, axis=0)
# print("min along x-axis(row) : ", min_var_row)
# print("max along y-axis(coloum) : ", min_var_col)
# print(min_var_row.dtype)
# print(min_var_col.dtype)

# print("sqrt", np.sqrt(var))
# print("sin", np.sin(var))
# print("cos", np.cos(var))

print(np.cumsum(var_33))
