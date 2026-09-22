import matplotlib
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

days = np.arange(1, 31)
temps = np.random.randint(20, 40, 30)
plt.figure(figsize=(8, 4))
plt.plot(days, temps, color="tab:blue", marker="o")
plt.title("Daily Temperature Readings (30 Days)")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.savefig("q26_line_chart.png", dpi=150)
plt.show()
plt.close()
