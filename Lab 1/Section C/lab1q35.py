import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

csv_path = ("Lab 1/monthly_expenses.csv")

pd.DataFrame({
    "category": ["Rent", "Food", "Transport", "Food", "Utilities", "Rent", "Entertainment"],
    "amount": [800, 150, 60, 90, 120, 800, 75],
}).to_csv(csv_path, index=False)

df = pd.read_csv(csv_path)
totals = df.groupby("category")["amount"].sum()
plt.figure(figsize=(6, 6))
plt.pie(totals.values, labels=totals.index, autopct="%1.1f%%")
plt.title("Monthly Expenses by Category")
plt.savefig("q35_expenses_pie.png", dpi=150)
plt.show()
plt.close()