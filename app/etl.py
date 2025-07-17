import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Generate Products
products = [
    {"product_id": i, "name": fake.word(), "category": random.choice(["Electronics", "Fashion", "Home"]), "brand": fake.company()}
    for i in range(1, 21)
]

# Generate Customers
customers = [
    {"customer_id": i, "name": fake.name(), "region": fake.city(), "gender": random.choice(["Male", "Female"])}
    for i in range(1, 51)
]

# Generate Sales
sales = []
for i in range(1, 501):
    product = random.choice(products)
    customer = random.choice(customers)
    quantity = random.randint(1, 5)
    price = round(random.uniform(10.0, 500.0), 2)
    order_date = fake.date_between(start_date='-90d', end_date='today')
    
    sales.append({
        "order_id": i,
        "product_id": product["product_id"],
        "customer_id": customer["customer_id"],
        "order_date": order_date,
        "quantity": quantity,
        "price": price,
        "revenue": round(quantity * price, 2)
    })

# Save data
pd.DataFrame(sales).to_csv("data/fact_sales.csv", index=False)
pd.DataFrame(products).to_csv("data/dim_product.csv", index=False)
pd.DataFrame(customers).to_csv("data/dim_customer.csv", index=False)
import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect("db/sales.db")
cursor = conn.cursor()

# Run schema
with open("sql/create_tables.sql", "r") as f:
    cursor.executescript(f.read())

# Load CSV data
pd.read_csv("data/dim_product.csv").to_sql("dim_product", conn, if_exists="append", index=False)
pd.read_csv("data/dim_customer.csv").to_sql("dim_customer", conn, if_exists="append", index=False)
pd.read_csv("data/fact_sales.csv").to_sql("fact_sales", conn, if_exists="append", index=False)

conn.commit()
conn.close()
