import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("telco_churn_clean.csv")

# Overall churn rate
print(f"Overall churn rate: {df['ChurnFlag'].mean():.2%}")

# Churn rate by contract type
churn_by_contract = df.groupby('Contract')['ChurnFlag'].mean().sort_values(ascending=False)
print(churn_by_contract)

sns.barplot(x=churn_by_contract.index, y=churn_by_contract.values)
plt.ylabel("Churn Rate")
plt.title("Churn Rate by Contract Type")
plt.savefig("churn_by_contract.png")
plt.close()

# Churn rate by tenure group
sns.barplot(x='TenureGroup', y='ChurnFlag', data=df)
plt.title("Churn Rate by Tenure")
plt.savefig("churn_by_tenure.png")
plt.close()

# Monthly charges: churned vs retained customers
sns.kdeplot(data=df, x='MonthlyCharges', hue='Churn', fill=True)
plt.title("Monthly Charges: Churned vs Retained")
plt.savefig("monthly_charges_dist.png")