import numpy as np
from datetime import datetime
from collections import Counter

# transaction_id, user_id, product_id, quantity, price, timestamp
dataset = np.array([[1, 1, 1, 1, 25, datetime.timestamp(datetime(2024, 8, 5))],
                 [2, 2, 1, 10, 25, datetime.timestamp(datetime(2024, 8, 5))],
                 [3, 3, 1, 2, 25, datetime.timestamp(datetime(2024, 8, 5))],
                 [4, 1, 3, 5, 100, datetime.timestamp(datetime(2024, 8, 6))],
                 [5, 2, 4, 1, 10, datetime.timestamp(datetime(2024, 8, 6))],
                 [6, 4, 2, 3, 5, datetime.timestamp(datetime(2024, 8, 7))],
                 [7, 5, 1, 3, 25, datetime.timestamp(datetime(2024, 8, 7))],
                 [8, 2, 3, 1, 100, datetime.timestamp(datetime(2024, 8, 7))],
                 [9, 1, 4, 4, 10, datetime.timestamp(datetime(2024, 8, 8))],
                 [10, 3, 2, 20, 5, datetime.timestamp(datetime(2024, 8, 8))]], dtype=object)


def print_array(array, message="Numpy array"):
    print(message)
    print(f"{array}\n")


def total_revenue(data):
    return np.sum(data[:, 3].astype(int) * data[:, 4].astype(float))


def unique_users(data):
    return len(np.unique(data[:, 1].astype(int)))


def most_purchased_product(data):
    product = data[:, 2].astype(int)
    quantity = data[:, 3].astype(int)
    res = {str(key): 0 for key in np.unique(product)}
    for i in range(len(product)):
        res[str(product[i])] += quantity[i]
    return np.array([max(res, key=res.get), res[max(res, key=res.get)]])


def type_cast(data):
    data[:, 4] = data[:, 4].astype(int)
    return data


def check_type(data):
    for i in range(len(data[0,:])):
        print(data[i, :].dtype)


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


def revenue_comparison(data, start_date_1, end_date_1, start_date_2, end_date_2):
    mask1 = (data[:, 5] >= datetime.timestamp(datetime(*start_date_1))) & (data[:, 5] <= datetime.timestamp(datetime(*end_date_1)))
    mask2 = (data[:, 5] >= datetime.timestamp(datetime(*start_date_2))) & (data[:, 5] <= datetime.timestamp(datetime(*end_date_2)))
    revenue1 = total_revenue(data[mask1])
    revenue2 = total_revenue(data[mask2])
    return revenue1, revenue2


def user_transactions(data, user_id):
    return data[data[:, 1].astype(int) == user_id]


def date_range_slice(data, start_date, end_date):
    return data[(data[:, 5] >= datetime.timestamp(datetime(*start_date))) & (data[:, 5] <= datetime.timestamp(datetime(*end_date)))]


def top_products(data, top_n=5):
    product_revenues = {}
    for product_id, quantity, price in zip(data[:, 2].astype(int), data[:, 3].astype(int), data[:, 4].astype(float)):
        if product_id not in product_revenues:
            product_revenues[product_id] = 0
        product_revenues[product_id] += quantity * price
    sorted_products = sorted(product_revenues.items(), key=lambda x: x[1], reverse=True)
    top_products_ids = [product_id for product_id, _ in sorted_products[:top_n]]
    for product_id in top_products_ids:
        print(f"Product {product_id}, revenue={product_revenues[product_id]}")
        print(data[data[:, 2].astype(int) == product_id])


print_array(dataset, "Initial array")
print(f"Total revenue is {total_revenue(dataset)}")
print(f"Number of unique users is {unique_users(dataset)}")
most_purchased_prod = most_purchased_product(dataset)
print(f"Most purchased product is {most_purchased_prod[0]} with quantity {most_purchased_prod[1]}")
print("Data types of columns")
check_type(type_cast(dataset))

prod_quant = product_quantity_array(dataset)
print_array(prod_quant, "Product quantity array")
user_transact_count = user_transaction_count(dataset)
print_array(user_transact_count, "User transaction count")
mask_array = masked_array(dataset)
print_array(mask_array, "Masked array (quantity>0)")

increased_price = price_increase(dataset)
print_array(increased_price, "Increased price (5%)")
filtered_transactions = filter_transactions(dataset)
print_array(filtered_transactions, "Filtered transactions (quantity>1)")
compared_revenues = revenue_comparison(dataset, (2024, 8, 5), (2024, 8, 6), (2024, 8, 7), (2024, 8, 8))
print(f"Compared revenues: {compared_revenues}")

specific_user_transactions = user_transactions(dataset, 1)
print_array(specific_user_transactions, "User transactions")
date_slice = date_range_slice(dataset, (2024, 8, 5), (2024, 8, 7))
print_array(date_slice, "Sliced transactions")
print("Top products transactions by revenue")
top_products(dataset)
