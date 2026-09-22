import matplotlib
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2 * np.pi, 200)
plt.figure(figsize=(8, 4))
plt.plot(x, np.sin(x), label="sin(x)", color="tab:orange")
plt.plot(x, np.cos(x), label="cos(x)", color="tab:green")
plt.title("sin(x) and cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("q27_sin_cos.png", dpi=150)
plt.show()
plt.close()
