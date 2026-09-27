import sqlite3
import pandas as pd

df = pd.read_csv("telco_churn_clean.csv")
conn = sqlite3.connect("churn.db")
df.to_sql("customers", conn, if_exists="replace", index=False)
conn.close()
print("Loaded into churn.db")