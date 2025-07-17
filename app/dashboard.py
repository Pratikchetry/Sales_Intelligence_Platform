import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect("db/sales.db")

# Load data
df_sales = pd.read_sql("SELECT * FROM fact_sales", conn)
df_customers = pd.read_sql("SELECT * FROM dim_customer", conn)
df_products = pd.read_sql("SELECT * FROM dim_product", conn)

# Merge data
df_sales['order_date'] = pd.to_datetime(df_sales['order_date'])
df = df_sales.merge(df_products, on='product_id').merge(df_customers, on='customer_id')

# Rename for clarity
df = df.rename(columns={
    "name_x": "product_name",
    "name_y": "customer_name"
})

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter or Search")

# Search Box (works on customer, product, brand, region)
search_query = st.sidebar.text_input("Search (Customer, Product, Brand, Region)", "")

region_filter = st.sidebar.multiselect(
    "Select Region(s)", options=df['region'].unique(), default=df['region'].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category", options=df['category'].unique(), default=df['category'].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range", [df['order_date'].min(), df['order_date'].max()]
)

# --- Filter based on sidebar inputs and search ---
filtered_df = df[
    (df['region'].isin(region_filter)) &
    (df['category'].isin(category_filter)) &
    (df['order_date'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))
]

if search_query:
    search_query = search_query.lower()
    filtered_df = filtered_df[
        df['customer_name'].str.lower().str.contains(search_query) |
        df['product_name'].str.lower().str.contains(search_query) |
        df['brand'].str.lower().str.contains(search_query) |
        df['region'].str.lower().str.contains(search_query)
    ]

# --- Dashboard ---
st.title("📊 Smart Sales Intelligence Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${filtered_df['revenue'].sum():,.2f}")
col2.metric("Total Orders", f"{filtered_df.shape[0]}")
col3.metric("Unique Customers", f"{filtered_df['customer_id'].nunique()}")

# --- Revenue Over Time ---
st.subheader("📈 Revenue Over Time")
monthly_revenue = (
    filtered_df.groupby(filtered_df['order_date'].dt.to_period("M"))
    .sum(numeric_only=True)['revenue']
)
monthly_revenue.index = monthly_revenue.index.astype(str)
st.line_chart(monthly_revenue)

# --- Top 5 Products ---
st.subheader("🏆 Top 5 Products by Revenue")
top_products = (
    filtered_df.groupby("product_name")
    .sum(numeric_only=True)
    .sort_values(by="revenue", ascending=False)
    .head(5)
)
st.bar_chart(top_products['revenue'])

# --- Revenue by Region ---
st.subheader("🌍 Revenue by Region")
region_sales = (
    filtered_df.groupby("region")
    .sum(numeric_only=True)
    .sort_values(by="revenue", ascending=False)
)
st.bar_chart(region_sales['revenue'])

# --- Customer Gender Distribution ---
st.subheader("👥 Customer Gender Distribution")
gender_counts = filtered_df['gender'].value_counts()
st.pyplot(
    gender_counts.plot.pie(
        autopct='%1.1f%%',
        figsize=(5, 5),
        title="Customer Gender Split",
        ylabel=''
    ).get_figure()
)

# --- Top 5 Customers ---
st.subheader("💰 Top 5 Customers by Revenue")
top_customers = (
    filtered_df.groupby("customer_name")
    .sum(numeric_only=True)
    .sort_values(by="revenue", ascending=False)
    .head(5)
)
st.bar_chart(top_customers['revenue'])

# --- Data Table with Download Option ---
st.subheader("📋 Filtered Data Preview")
st.dataframe(filtered_df)

st.download_button(
    label="⬇️ Download CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_sales_data.csv',
    mime='text/csv'
)



