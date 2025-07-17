CREATE TABLE IF NOT EXISTS dim_product (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    brand TEXT
);

CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    region TEXT,
    gender TEXT
);

CREATE TABLE IF NOT EXISTS fact_sales (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    order_date TEXT,
    quantity INTEGER,
    price REAL,
    revenue REAL,
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);
