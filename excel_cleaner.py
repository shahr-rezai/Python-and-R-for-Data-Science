import pandas as pd


# Function to read an Excel file
def read_excel_file(file_name):
    data = pd.read_excel(file_name)
    return data

#funtion to clean the data
def clean_excel_file(data):

    # Remove duplicate rows  
    data=data.drop_duplicates()

    # Fill missing values
    data = data.fillna("Unknown")

    # Remove rows with negative values in numeric columns
    numeric_columns = data.select_dtypes(inlcude = "number").columns

    for column in numeric_columns:
        data = data[data[column]>=0]
    
    return data


# Function to save the cleaned data

def save_cleaned_file(data, output_file):
    data.to_excel(output_file, index=False)
    print("Cleaned file saved successfully!")

# Main Program
file_name = r"C:\Users\DELL\OneDrive\Desktop\python Lab\data_cleaning\sales_data.xlsx"

#read file
data = read_excel_file(file_name)

#clean file
cleaned_data = clean_excel_file(data)

#print cleaned data
print(cleaned_data)

#save cleaned data
save_cleaned_file(cleaned_data, "cleaned_sales_data.slsx")