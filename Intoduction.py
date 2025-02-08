import numpy as np
import timeit

x = np.array([1, 2, 3, 4])
# print(x)
# print(type(x))


y = [1, 2, 3, 4]
# print(y)
# print(type(y))


# Time taken
def list_operation():
    return [j**4 for j in range(1, 1000)]


def numpy_operation():
    return np.arange(1, 1000) ** 4


# Time taken for list comprehension
list_time = timeit.timeit(list_operation)

# Time taken for NumPy array operation
numpy_time = timeit.timeit(numpy_operation)

print("Time taken for list comprehension:", list_time)
print("Time taken for NumPy array operation:", numpy_time)
