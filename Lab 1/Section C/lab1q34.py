import pandas as pd
import numpy as np


df = pd.DataFrame({"name": ["A", "B", "C", "D", "E"], "score": [80, np.nan, 90, np.nan, 70]})
df["score"] = df["score"].fillna(df["score"].mean())
remaining_nans = df["score"].isna().sum()
print(f"{df}\n\nRemaining NaNs in score: {remaining_nans}")