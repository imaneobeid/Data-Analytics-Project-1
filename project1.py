import pandas as pd

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

# ==========================
# Display Dataset Information
# ==========================
print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
df.info()

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# ==========================
# Check Missing Values
# ==========================
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Verify missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ==========================
# Check Duplicate Rows
# ==========================
duplicate_rows = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicate_rows}")

df = df.drop_duplicates()

# ==========================
# Check Duplicate Order IDs
# ==========================
duplicate_ids = df["OrderID"].duplicated().sum()
print(f"Duplicate Order IDs: {duplicate_ids}")

df = df.drop_duplicates(subset="OrderID")

# ==========================
# Convert Date Column
# ==========================
df["Date"] = pd.to_datetime(df["Date"])

# ==========================
# Save Cleaned Dataset
# ==========================
df.to_csv("Cleaned_Dataset.csv", index=False)

print("\n✅ Data cleaning completed successfully!")
print("The cleaned dataset has been saved as 'Cleaned_Dataset.csv'.")