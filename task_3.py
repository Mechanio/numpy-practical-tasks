import numpy as np


def print_array(array, message="Numpy array"):
    print(message)
    print(f"{array}\n")


def to_transpose(data):
    return np.transpose(data)


def to_reshape(data):
    return np.reshape(data, (3, 12))


def to_split(data, axis=0):
    return np.split(data, 3, axis=axis)


def to_combine(data, axis=0):
    return np.concatenate(data, axis=axis)


dataset = np.random.randint(10, size=(6, 6))
print_array(dataset, "Initial array")

transposed_dataset = to_transpose(dataset)
print_array(transposed_dataset, "Transposed array")
assert len(dataset) == len(transposed_dataset), "Integrity of the array is not maintained"

reshaped_dataset = to_reshape(dataset)
print_array(reshaped_dataset, "Reshaped array (3x12)")
assert len(reshaped_dataset) == 3, "Reshaped array error"

split_dataset = to_split(dataset)
print_array(split_dataset, "Splitted array")
assert len(split_dataset) == 3, "Splitted array error"

combined_dataset = to_combine(split_dataset)
print_array(combined_dataset, "Combined array")
assert np.array_equal(dataset, combined_dataset), "Integrity of the array is not maintained"
