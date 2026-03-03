# ==========================================================
# 📊 Lab 12 – Getting Started with Pandas DataFrames
# ==========================================================

import pandas as pd
import numpy as np
import os

print("=" * 70)
print("LAB 12 – PANDAS DATAFRAMES")
print("=" * 70)

# ==========================================================
# TASK 1: VERIFY ENVIRONMENT
# ==========================================================

print("\nPython and Pandas Environment Check")
print("Pandas version:", pd.__version__)

# ==========================================================
# TASK 2: LOAD STUDENTS DATASET
# ==========================================================

print("\nLoading students.csv...")

df = pd.read_csv("students.csv")

print("\nDataFrame Loaded Successfully!")
print(df)

print("\nDataFrame Type:", type(df))
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index)

# ==========================================================
# TASK 3: INSPECTING DATA
# ==========================================================

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 3 rows:")
print(df.tail(3))

print("\nDataFrame Info:")
df.info()

print("\nStatistical Summary (Numeric Columns):")
print(df.describe())

print("\nFull Summary:")
print(df.describe(include="all"))

# ==========================================================
# TASK 4: ACCESSING DATA
# ==========================================================

print("\nAccess column 'name':")
print(df["name"])

print("\nMultiple Columns:")
print(df[["name", "age", "score"]])

print("\nUsing loc – Rows 0 to 2:")
print(df.loc[0:2])

print("\nUsing loc – Specific columns:")
print(df.loc[0:2, ["name", "score"]])

print("\nUsing iloc – First row:")
print(df.iloc[0])

print("\nUsing iloc – Rows 0-2, Columns 1-3:")
print(df.iloc[0:3, 1:4])

print("\nStudents with score > 90:")
print(df.loc[df["score"] > 90])

print("\nStudents aged 20 with grade A:")
print(df.loc[(df["age"] == 20) & (df["grade"] == "A")])

# ==========================================================
# TASK 5: LOAD SALES DATASET
# ==========================================================

print("\nLoading sales_data.csv...")

sales_df = pd.read_csv("sales_data.csv")

print("\nSales Dataset Overview:")
print("Shape:", sales_df.shape)
print(sales_df.head())

print("\nDataset Info:")
sales_df.info()

print("\nStatistical Summary:")
print(sales_df.describe())

# ==========================================================
# ADVANCED DATA ANALYSIS
# ==========================================================

print("\nTop 5 Products by Quantity Sold:")
top_products = sales_df.sort_values("quantity_sold", ascending=False)
print(top_products[["product_name", "quantity_sold"]].head())

print("\nElectronics Products:")
electronics = sales_df[sales_df["category"] == "Electronics"]
print(electronics[["product_name", "price", "quantity_sold"]])

print("\nNorth Region Sales:")
north_sales = sales_df[sales_df["region"] == "North"]
print(north_sales[["product_name", "price", "quantity_sold"]])

print("\nHigh Value Products (price > 200):")
expensive = sales_df[sales_df["price"] > 200]
print(expensive[["product_name", "price", "category"]])

# ==========================================================
# CALCULATE REVENUE
# ==========================================================

sales_df["revenue"] = sales_df["price"] * sales_df["quantity_sold"]

print("\nProducts with Revenue:")
print(sales_df[["product_name", "price", "quantity_sold", "revenue"]].head())

print("\nTop 5 Products by Revenue:")
top_revenue = sales_df.sort_values("revenue", ascending=False)
print(top_revenue[["product_name", "revenue"]].head())

electronics_revenue = sales_df.loc[sales_df["category"] == "Electronics", "revenue"].sum()
furniture_revenue = sales_df.loc[sales_df["category"] == "Furniture", "revenue"].sum()

print("\nRevenue by Category:")
print(f"Electronics Revenue: ${electronics_revenue:,.2f}")
print(f"Furniture Revenue: ${furniture_revenue:,.2f}")

# ==========================================================
# SORTING & FILTERING
# ==========================================================

print("\nSorted by Price (Ascending):")
print(sales_df.sort_values("price")[["product_name", "price"]].head())

print("\nSorted by Category then Price:")
print(sales_df.sort_values(["category", "price"])[["product_name", "category", "price"]].head())

print("\nProducts priced between 100 and 300:")
mid_range = sales_df[(sales_df["price"] >= 100) & (sales_df["price"] <= 300)]
print(mid_range[["product_name", "price"]])

print("\nProducts from East or West Regions:")
print(sales_df[sales_df["region"].isin(["East", "West"])][["product_name", "region"]])

# ==========================================================
# DATA VALIDATION
# ==========================================================

print("\nMissing Values:")
print(sales_df.isnull().sum())

print("\nDuplicate Rows:")
print(sales_df.duplicated().sum())

print("\nMemory Usage:")
print(sales_df.memory_usage(deep=True))

print("\nLAB 12 COMPLETED SUCCESSFULLY!")
print("=" * 70)
