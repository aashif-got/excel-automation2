import pandas as pd

# Load the Excel file
df = pd.read_excel("sales_data1.xlsx")

# Group by Product and sum the Sales
summary = df.groupby("Product")["Sales"].sum().reset_index()

# Save the result to a new Excel file
summary.to_excel("sales_summary.xlsx", index=False)

print("✅ Summary file created successfully.")
