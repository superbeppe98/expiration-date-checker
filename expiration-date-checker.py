from tabulate import tabulate
import pandas as pd
import datetime
import sys

# Disable SettingWithCopyWarning
pd.options.mode.chained_assignment = None

# Function to left-align strings


def align_left(s):
    if pd.isna(s):
        return ""
    else:
        return f'{s:<30}'


# Check if the expiration date is provided as a command-line argument
if len(sys.argv) > 1:
    expiration_date_str = sys.argv[1]
else:
    # Prompt user to input the expiration date of the packaging in the format "01-01-2023"
    expiration_date_str = input(
        "Enter the expiration date of the packaging (format: 01-01-2023): ")

# Convert the provided expiration date to a datetime object
expiration_date = datetime.datetime.strptime(expiration_date_str, '%d-%m-%Y')

# Load the Excel file and handle column name formatting
df = pd.read_excel("products.xlsx")

# Rename the "Part Name" column to "Product Name" and move it to position 0, left-aligning the text
df = df.rename(columns={"Part Name": "Product Name"})
product_name = df.pop("Product Name")
df.insert(0, "Product Name", product_name.apply(align_left))

# Rename the "Quantity" column to "Quantity"
df = df.rename(columns={"Quantity": "Quantity"})

# Rename the "purchase_price" column to "Purchase Price"
df = df.rename(columns={"purchase_price": "Purchase Price"})

# Convert the "Packaging" column to a datetime object
df["Packaging"] = pd.to_datetime(df["Packaging"], format="%m/%y")

# Find products with an expiration date up to the end of 2023
mask = (df["Packaging"] <= pd.Timestamp(expiration_date))
expiring_products = df.loc[mask]

# Convert the "Packaging" column to a string in the format "dd-mm-yyyy"
expiring_products["Packaging"] = expiring_products["Packaging"].dt.strftime(
    '%d-%m-%Y')

# Print the expiring products without the row number
print(tabulate(expiring_products, showindex=False, headers=df.columns))
