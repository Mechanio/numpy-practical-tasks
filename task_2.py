# NOT FULLY DONE TASK
# NOT FULLY DONE TASK
# NOT FULLY DONE TASK

import numpy as np
from datetime import datetime
from collections import Counter

# transaction_id, user_id, product_id, quantity, price, timestamp
dataset = np.array([[1, 1, 1, 1, 25, datetime.timestamp(datetime(2024,8, 5))],
                 [2, 2, 1, 10, 25, datetime.timestamp(datetime(2024,8, 5))],
                 [3, 3, 1, 2, 25, datetime.timestamp(datetime(2024,8, 5))],
                 [4, 1, 3, 5, 100, datetime.timestamp(datetime(2024,8, 6))],
                 [5, 2, 4, 1, 10, datetime.timestamp(datetime(2024,8, 6))],
                 [6, 4, 2, 3, 5, datetime.timestamp(datetime(2024,8, 6))],
                 [7, 5, 1, 3, 25, datetime.timestamp(datetime(2024,8, 7))],
                 [8, 2, 3, 1, 100, datetime.timestamp(datetime(2024,8, 7))],
                 [9, 1, 4, 4, 10, datetime.timestamp(datetime(2024,8, 7))],
                 [10, 3, 2, 20, 5, datetime.timestamp(datetime(2024,8, 7))]])


def print_array(array, message="Numpy array"):
    print(message)
    print(f"{array}\n")


def total_revenue(data):
    return np.sum(data[:, 3].astype(int) * data[:, 4].astype(float))


def unique_users(data):
    return len(np.unique(data[:, 1].astype(int)))


# def most_purchased_product(data):
#     product = data[:, 2].astype(int)
#     quantity = data[:, 3].astype(int)
#     # unique_product = np.unique(product)
#     res = {}
#     for i in range(len(product)):
#         res[str(product[i])] += quantity[i]
#     return res


# def type_cast(data):
#     data[:, 4] = data[:, 4].astype(int)
#
#
# def check_type(data):
#     for i in range(len(data[0,:])):
#         print(data[i, :].dtype)
#     print(data.dtype)


def product_quantity_array(data):
    return data[:, [2, 3]]


def user_transaction_count(data):
    users_transactions = data[:, 1].astype(int)
    res = Counter(users_transactions)
    return res
    # or
    # return np.array([list(res.keys()), list(res.values())])


def masked_array(data):
    return data[data[:, 3] > 0]


def price_increase(data, percentage=5):
    data[:, 4] = data[:, 4] * (1 + percentage / 100)
    return data


def filter_transactions(data):
    return data[data[:, 3] > 1]


# def revenue_comparison(data):
#     pass


def user_transactions(data, user_id):
    return data[data[:, 1].astype(int) == user_id]


# def date_range_slice(data):
#     pass


# def top_products(data):
#     pass


print_array(dataset, "Initial array")
print(f"Total revenue is {total_revenue(dataset)}")
print(f"Number of unique users is {unique_users(dataset)}")
# print(most_purchased_product(dataset))
# print(check_type(dataset))

prod_quant = product_quantity_array(dataset)
print_array(prod_quant, "Product quantity array")
user_transact_count = user_transaction_count(dataset)
print_array(user_transact_count, "User transaction count")
mask_array = masked_array(dataset)
print_array(mask_array, "Masked array (quantity>0)")

increased_price = price_increase(dataset)
print_array(increased_price, "Increased price (5%)")
# print(filter_transactions(dataset))
filtered_transactions = filter_transactions(dataset)
print_array(filtered_transactions, "Filtered transactions (quantity>1)")
# print(revenue_comparison(dataset))

specific_user_transactions = user_transactions(dataset, 1)
print_array(specific_user_transactions, "User transactions")
# print(date_range_slice(dataset))
# print(top_products(dataset))
