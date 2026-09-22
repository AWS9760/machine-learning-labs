import pandas as pd
import numpy as np

np.random.seed(1)
df = pd.DataFrame({
    "student": [f"S{i}" for i in range(1, 11)],
    "Math": np.random.randint(60, 100, 10),
    "Science": np.random.randint(60, 100, 10),
    "English": np.random.randint(60, 100, 10),
})
df["average"] = df[["Math", "Science", "English"]].mean(axis=1)
top = df.loc[df["average"].idxmax()]
print(f"{df}\n\nTop performer:\n{top}")