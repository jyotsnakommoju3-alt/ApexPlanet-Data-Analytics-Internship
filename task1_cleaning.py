import pandas as pd
import numpy as np

INPUT_FILE = "ApexPlanet_DataAnalytics_Dataset.xlsx"
OUTPUT_FILE = "ApexPlanet_Task1_Cleaned_Data.xlsx"

df = pd.read_excel(INPUT_FILE)

# 1. Standardize date
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# 2. Remove leading/trailing spaces from text columns
text_cols = ["Order_ID", "Customer_ID", "Customer_Name",
             "Gender", "City", "Product", "Category"]
for col in text_cols:
    df[col] = df[col].astype("string").str.strip()

# 3. Handle missing values
age_median = df["Age"].median()
city_mode = df["City"].mode(dropna=True).iloc[0]

df["Age"] = df["Age"].fillna(age_median)
df["City"] = df["City"].fillna(city_mode)

# 4. Flag repeated Order_ID values instead of deleting valid-looking transactions
df["Duplicate_Order_ID_Flag"] = df["Order_ID"].duplicated(keep=False)

# 5. Validate Total_Sales
df["Total_Sales_Check"] = np.isclose(
    df["Quantity"] * df["Unit_Price"],
    df["Total_Sales"],
    rtol=1e-9,
    atol=1e-6
)

# 6. Detect Total_Sales outliers using the IQR rule
q1 = df["Total_Sales"].quantile(0.25)
q3 = df["Total_Sales"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

df["Total_Sales_Outlier_Flag"] = (
    (df["Total_Sales"] < lower) | (df["Total_Sales"] > upper)
)

# 7. Export analysis-ready data
df.to_excel(OUTPUT_FILE, index=False)

print("Cleaning completed.")
print("Output:", OUTPUT_FILE)
