import pandas as pd

df = pd.read_csv("telco_churn.csv")
print(df.shape)                       # (rows, columns)
print(df.dtypes)                      # what type each column is
print(df.isnull().sum())              # how many missing values per column
print(df['Churn'].value_counts(normalize=True))   # % churned vs not