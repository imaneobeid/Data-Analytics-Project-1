import pandas as pd

df = pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
df.info()

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

duplicate_rows = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicate_rows}")

df = df.drop_duplicates()

duplicate_ids = df["OrderID"].duplicated().sum()
print(f"Duplicate Order IDs: {duplicate_ids}")

df = df.drop_duplicates(subset="OrderID")

df["Date"] = pd.to_datetime(df["Date"])

df.to_csv("Cleaned_Dataset.csv", index=False)

print("\n✅ Data cleaning completed successfully!")
print("The cleaned dataset has been saved as 'Cleaned_Dataset.csv'.")