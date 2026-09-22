import pandas as pd


df = pd.DataFrame({
    "name": ["Pen", "Notebook", "Bag", "Bottle", "Charger", "Headphones"],
    "price": [1.5, 3.0, 25.0, 5.0, 12.0, 40.0],
    "quantity": [10, 8, 2, 6, 4, 3],
})
df["total"] = df["price"] * df["quantity"]
print(df)