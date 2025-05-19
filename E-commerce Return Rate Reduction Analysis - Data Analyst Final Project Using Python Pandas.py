import pandas as pd

# Data (as a list of dictionaries for simplicity)
data = [
    {"name": "William", "order_id": 1123581321, "product_id": 32, "customer_id": 1, "return_id": 123, "rates": 500, "Probability of Return": "13%"},
    {"name": "Joseph", "order_id": 1123581322, "product_id": 33, "customer_id": 2, "return_id": 124, "rates": 1000, "Probability of Return": "15%"},
    {"name": "John", "order_id": 1123581323, "product_id": 34, "customer_id": 3, "return_id": 125, "rates": 1500, "Probability of Return": "5%"},
    {"name": "Thomas", "order_id": 1123581324, "product_id": 35, "customer_id": 4, "return_id": 126, "rates": 2000, "Probability of Return": "2%"},
    {"name": "James", "order_id": 1123581325, "product_id": 36, "customer_id": 5, "return_id": 127, "rates": 2500, "Probability of Return": "19%"},
    {"name": "Anthony", "order_id": 1123581326, "product_id": 37, "customer_id": 6, "return_id": 128, "rates": 3000, "Probability of Return": "20%"},
    {"name": "George", "order_id": 1123581327, "product_id": 38, "customer_id": 7, "return_id": 129, "rates": 3500, "Probability of Return": "22%"},
    {"name": "Robert", "order_id": 1123581328, "product_id": 39, "customer_id": 8, "return_id": 130, "rates": 4000, "Probability of Return": "18%"},
    {"name": "Donald", "order_id": 1123581329, "product_id": 40, "customer_id": 9, "return_id": 131, "rates": 4500, "Probability of Return": "5%"},
    {"name": "David", "order_id": 1123581330, "product_id": 41, "customer_id": 10, "return_id": 132, "rates": 5000, "Probability of Return": "19%"},
    {"name": "Kenneth", "order_id": 1123581331, "product_id": 42, "customer_id": 11, "return_id": 133, "rates": 5500, "Probability of Return": "20%"},
    {"name": "Adam", "order_id": 1123581332, "product_id": 43, "customer_id": 12, "return_id": 134, "rates": 6000, "Probability of Return": "21%"},
    {"name": "Dolph", "order_id": 1123581333, "product_id": 44, "customer_id": 13, "return_id": 135, "rates": 6500, "Probability of Return": "13%"},
    {"name": "Susan", "order_id": 1123581334, "product_id": 45, "customer_id": 14, "return_id": 136, "rates": 7000, "Probability of Return": "14%"},
    {"name": "Jennifer", "order_id": 1123581335, "product_id": 46, "customer_id": 15, "return_id": 137, "rates": 7500, "Probability of Return": "16%"},
    {"name": "Harold", "order_id": 1123581336, "product_id": 47, "customer_id": 16, "return_id": 138, "rates": 8000, "Probability of Return": "10%"},
    {"name": "Jordan", "order_id": 1123581337, "product_id": 48, "customer_id": 17, "return_id": 139, "rates": 8500, "Probability of Return": "7%"},
    {"name": "Albert", "order_id": 1123581338, "product_id": 49, "customer_id": 18, "return_id": 140, "rates": 9000, "Probability of Return": "15%"},
    {"name": "Jenneth", "order_id": 1123581339, "product_id": 50, "customer_id": 19, "return_id": 141, "rates": 9500, "Probability of Return": "17%"},
]

# Create DataFrame
df = pd.DataFrame(data)

# Convert "Probability of Return" from percentage string to float
df['Probability_numeric'] = df['Probability of Return'].str.rstrip('%').astype(float) / 100

# Display the DataFrame
print(df[['name', 'Probability of Return', 'Probability_numeric']])
