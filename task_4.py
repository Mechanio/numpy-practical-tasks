import numpy as np
import csv


def print_array(array, message="Numpy array"):
    print(message)
    print(f"{array}\n")


def to_save(data, filename="task_4_array"):
    np.savetxt(f"{filename}.txt", data, fmt='%d')
    with open(f"{filename}.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    np.save(f"{filename}.npy", data)


def to_read(filename="task_4_array.npy"):
    if filename.endswith('.npy'):
        return np.load(filename)
    elif filename.endswith('.csv'):
        return np.genfromtxt(filename, delimiter=',', dtype=int)
    elif filename.endswith('.txt'):
        return np.loadtxt(filename, dtype=int)
    else:
        raise ValueError("No file found")


def to_sum(data, axis=None):
    return np.sum(data, axis=axis)


def to_mean(data, axis=None):
    return np.mean(data, axis=axis)


def to_median(data, axis=None):
    return np.median(data, axis=axis)


def to_std(data, axis=None):
    return np.std(data, axis=axis)


# axis=0 - column, axis=1 - row
def axis_aggregation(data, axis=0):
    return {
        "sum_of_dataset": to_sum(data, axis=axis),
        "mean_of_dataset": to_mean(data, axis=axis),
        "median_of_dataset": to_median(data, axis=axis),
        "std_of_dataset": to_std(data, axis=axis),
    }


dataset = np.random.randint(10, size=(10, 10))
print_array(dataset, "Initial array")

to_save(dataset)
read_dataset = to_read()
print_array(read_dataset, "Loaded array")
assert np.array_equal(dataset, read_dataset), "Integrity of the array is not maintained after the read"

sum_of_dataset = to_sum(read_dataset)
print_array(sum_of_dataset, "Sum of array")

mean_of_dataset = to_mean(read_dataset)
print_array(mean_of_dataset, "Mean of array")

median_of_dataset = to_median(read_dataset)
print_array(median_of_dataset, "Median of array")

std_of_dataset = to_std(read_dataset)
print_array(std_of_dataset, "Standard deviation of array")

row_res = axis_aggregation(read_dataset, axis=1)
print_array(row_res["sum_of_dataset"], "Row-wise sum of array")
print_array(row_res["mean_of_dataset"], "Row-wise mean of array")
print_array(row_res["median_of_dataset"], "Row-wise median of array")
print_array(row_res["std_of_dataset"], "Row-wise standard deviation of array")
assert len(dataset) == len(row_res["sum_of_dataset"]), "Integrity of the array is not maintained after the axis aggregation"
assert len(dataset) == len(row_res["mean_of_dataset"]), "Integrity of the array is not maintained after the axis aggregation"
assert len(dataset) == len(row_res["median_of_dataset"]), "Integrity of the array is not maintained after the axis aggregation"
assert len(dataset) == len(row_res["std_of_dataset"]), "Integrity of the array is not maintained after the axis aggregation"


col_res = axis_aggregation(read_dataset)
print_array(col_res["sum_of_dataset"], "Column-wise sum of array")
print_array(col_res["mean_of_dataset"], "Column-wise mean of array")
print_array(col_res["median_of_dataset"], "Column-wise median of array")
print_array(col_res["std_of_dataset"], "Column-wise standard deviation of array")
assert len(dataset[0,:]) == len(col_res["sum_of_dataset"]), "Integrity of the array is not maintained after the axis aggregation"
assert len(dataset[0,:]) == len(col_res["mean_of_dataset"]), "Integrity of the array is not maintained after the axis aggregation"
assert len(dataset[0,:]) == len(col_res["median_of_dataset"]), "Integrity of the array is not maintained after the axis aggregation"
assert len(dataset[0,:]) == len(col_res["std_of_dataset"]), "Integrity of the array is not maintained after the axis aggregation"
