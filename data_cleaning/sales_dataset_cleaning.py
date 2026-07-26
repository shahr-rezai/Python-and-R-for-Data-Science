import pandas as pd
import numpy as np

# Read Excel file
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\python Lab\data_cleaning\sales_dataset_cleaning.py")

print("Original Data")
print(df.head())

# Check dataset
print("\nData Info")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nSummary")
print(df.describe(include="all"))

# Remove duplicate rows
df = df.drop_duplicates()

# Remove extra spaces
df.columns = df.columns.str.strip()

text_columns = ["Month", "Region", "Product"]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# Convert numeric columns
numeric_columns = [
    "Quantity",
    "UnitPrice",
    "TotalSales"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Clean Month
valid_months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

df.loc[~df["Month"].isin(valid_months), "Month"] = np.nan

# Clean Region
valid_regions = ["North", "South", "East", "West"]

df.loc[~df["Region"].isin(valid_regions), "Region"] = np.nan

# Clean Product
valid_products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

df.loc[~df["Product"].isin(valid_products), "Product"] = np.nan

# Remove invalid quantity
df.loc[df["Quantity"] <= 0, "Quantity"] = np.nan

# Remove invalid unit price
df.loc[df["UnitPrice"] <= 0, "UnitPrice"] = np.nan

# Remove duplicate Order IDs
df = df.drop_duplicates(subset="OrderID")

# Fill missing numeric values
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values
categorical_columns = ["Month", "Region", "Product"]

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Calculate total sales
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

df["TotalSales"] = df["TotalSales"].round(2)

# Display cleaned data
print("\nCleaned Data")
print(df)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_excel("sales_cleaned_dataset.xlsx", index=False)

print("\nCleaning completed successfully!")
print("File saved as sales_cleaned_dataset.xlsx")