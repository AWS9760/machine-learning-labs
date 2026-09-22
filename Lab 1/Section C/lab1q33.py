import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dates = pd.date_range("2026-01-01", periods=10).to_list()
np.random.shuffle(dates) 
df = pd.DataFrame({"date": dates, "sales": np.random.randint(100, 500, 10)})
df = df.sort_values("date")
ax = df.plot(x="date", y="sales", kind="line", marker="o", title="Sales Over Time", legend=False)
ax.set_ylabel("Sales")
plt.savefig("q33_sales_over_time.png", dpi=150)
plt.show()
plt.close()