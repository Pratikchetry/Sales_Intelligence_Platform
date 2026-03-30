# 📊 Smart Sales Intelligence Dashboard

This is an interactive, end-to-end **Sales Intelligence Platform** built using Python, Streamlit, SQLite, and Pandas. It allows users to explore synthetic sales data through a visually engaging dashboards, apply filters, search queries, and download custom reports — all in real time.

---

## 🔗 Live App URL

**Streamlit App**:
[https://salesintelligenceplatform-ztvbawwvr74weynohuzuhl.streamlit.app/](https://salesintelligenceplatform-ztvbawwvr74weynohuzuhl.streamlit.app/)

---

## 💡 Project Overview

This platform simulates how businesses can monitor and analyze sales performance. From high-level KPIs to customer-level drill-downs, this project demonstrates key business intelligence capabilities, including:

* Revenue insights
* Product and customer analytics
* Region-wise performance
* Real-time data exploration
* Downloadable custom datasets

---

## 📦 Features

* 🔍 **Search + Filters**: Filter by customer, product, region, brand, or date range
* 📈 **Revenue Trends**: Line chart of monthly revenue
* 🏆 **Top Products & Customers**: Bar charts of top 5 products and customers
* 🌍 **Region Analysis**: Revenue distribution by region
* 👥 **Gender Distribution**: Pie chart visualization
* 📋 **Live Data Table**: Filtered data preview
* ⬇️ **Download CSV**: Export filtered data in one click

---

## 🧰 Tech Stack

* **Python**
* **Streamlit**
* **SQLite**
* **Pandas**
* **Matplotlib / Seaborn**
* **Faker (for synthetic data)**

---

## 🗂️ Folder Structure

```
Sales_Intelligence_Platform/
├── app/
│   ├── dashboard.py         
│   └── etl.py               
│
├── data/
│   ├── dim_customer.csv    
│   ├── dim_product.csv     
│   └── fact_sales.csv       
│
├── db/
│   └── sales.db            
│
├── notebooks/
│   └── eda.ipynb            
│
├── sql/
│   └── create_tables.sql    
│
├── .streamlit/
│   └── config.toml          
│
├── requirements.txt         
└── README.md               
```

---

## ⚙️ How to Run Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/Pratikchetry/Sales_Intelligence_Platform.git
cd Sales_Intelligence_Platform
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Generate dummy data and SQLite database

```bash
python3 app/etl.py
```

### Step 4: Run the Streamlit dashboard

```bash
streamlit run app/dashboard.py
```

---

## 📈 Dashboard Snapshots

* **Monthly Revenue Trend** (Line chart)
* **Top 5 Products & Customers** (Bar charts)
* **Sales by Region** (Bar chart)
* **Customer Gender Split** (Pie chart)
* **Interactive Data Table with Download Option**

---

## 📌 Future Enhancements

* Connect to real-time API or cloud database
* Add forecast/prediction using ML
* Add login/authentication features
* Improve UI responsiveness for mobile

---

## 👤 About the Author

**Name**: Pratik Chetry
**GitHub**: https://github.com/Pratikchetry
**LinkedIn**: https://www.linkedin.com/in/pratik-chetry/
**Email**: chetrypratik2002@gmail.com

---

## 📜 License

This project is open-source and free for personal or academic use.
