import pandas as pd
import numpy as np

# Read Excel file
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\python Lab\data_cleaning\sales_dirty_dataset.csv")

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

text_columns = ["Name", "Gender", "Department"]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# Standardize gender
df["Gender"] = df["Gender"].replace({
    "Male": "M",
    "Female": "F",
    "X": np.nan,
    "": np.nan,
    "nan": np.nan
})

# Clean department
valid_departments = ["CSE", "EEE", "Math", "BBA"]

df.loc[~df["Department"].isin(valid_departments), "Department"] = np.nan

# Clean names
df["Name"] = df["Name"].replace(["", "nan"], np.nan)

df.loc[
    ~df["Name"].fillna("").str.match(r"^[A-Za-z ]+$"),
    "Name"
] = np.nan

# Convert numeric columns
numeric_columns = [
    "Age",
    "StudyHours",
    "Attendance",
    "Math",
    "Physics",
    "Programming"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove invalid ages
df.loc[(df["Age"] < 16) | (df["Age"] > 35), "Age"] = np.nan

# Remove invalid study hours
df.loc[(df["StudyHours"] < 0) | (df["StudyHours"] > 24), "StudyHours"] = np.nan

# Remove invalid attendance
df.loc[(df["Attendance"] < 0) | (df["Attendance"] > 100), "Attendance"] = np.nan

# Remove invalid marks
subjects = ["Math", "Physics", "Programming"]

for subject in subjects:
    df.loc[(df[subject] < 0) | (df[subject] > 100), subject] = np.nan

# Remove duplicate student IDs
df = df.drop_duplicates(subset="StudentID")

# Fill missing numeric values
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values
categorical_columns = ["Name", "Gender", "Department"]

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Calculate average
df["Average"] = (
    df["Math"] +
    df["Physics"] +
    df["Programming"]
) / 3

df["Average"] = df["Average"].round(2)

# Display cleaned data
print("\nCleaned Data")
print(df)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_excel("students_cleaned_dataset.xlsx", index=False)

print("\nCleaning completed successfully!")
print("File saved as students_cleaned_dataset.xlsx")