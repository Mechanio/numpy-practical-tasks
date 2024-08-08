import numpy as np


def print_array(array, message="Numpy array"):
    print(message)
    print(f"{array}\n")


# 1 Array Creation
one_dim = np.arange(1, 11)
print_array(one_dim, "Initial one-dimensional array")
two_dim = np.arange(1, 10).reshape(3, 3)
print_array(two_dim, "Initial two dimensional array")
# 2 Basic Operations
third_elem_one_dim = one_dim[2]
print_array(third_elem_one_dim, "Third element of one-dimensional array")
sliced_two_dim = two_dim[:2, :2]
print_array(sliced_two_dim, "First two rows and columns of two-dimensional array")

one_dim_plus_five = one_dim + 5
print_array(one_dim_plus_five, "Each element +5 of one-dimensional array")
two_dim_multiply_two = two_dim * 2
print_array(two_dim_multiply_two, "Each element *2 of one-dimensional array")
