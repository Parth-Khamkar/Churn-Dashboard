import pandas as pd
df = pd.read_csv("telco_churn.csv")

# Fix TotalCharges: convert text to numbers, blanks become NaN, then fill with 0
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# Create a simple 0/1 version of the churn label (easier for math/charts)
df['ChurnFlag'] = (df['Churn'] == 'Yes').astype(int)

# Group customers into tenure buckets, for easier filtering later
df['TenureGroup'] = pd.cut(
    df['tenure'],
    bins=[0, 12, 24, 48, 60, 100],
    labels=['0-12 mo', '13-24 mo', '25-48 mo', '49-60 mo', '60+ mo']
)

# Drop the customer ID column — it's a unique code, not useful for analysis
df = df.drop(columns=['customerID'], errors='ignore')

df.to_csv("telco_churn_clean.csv", index=False)
print("Cleaned file saved. New shape:", df.shape)