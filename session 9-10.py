import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=[11,2,5,4,6,7])
print(s)
print("\n\n")

print(s[4])
print(s[7])
print(s.index)
print(s.values)
print(s.values[4], s[6])

dates = pd.date_range("20260427", periods=100, freq="D")
print(dates)
print(type(dates))

df = pd.DataFrame(np.random.randn(100 , 4), index=dates, columns=list("ABCD"))
# df = pd.DataFrame(np.random.randint(1, 100, (6, 4)), index=dates, columns=list("ABCD"))

df

# df.index

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "gym"]),
        "F": "foo"
    }
)
df2

print(df.index)
print("-----")
df.describe()

print(df.T)

print(df.sort_values(by="B", ascending=True))
print(df)

print(df)
print("----")
print(df["A"]) # df.A dot notation
print("----")
print(df.B[0:3]) # Selection of a few cells of column using dot notation
print("----")
print(type(df.A))
print(df.A.values)

print(type(df.A.values))

import pandas as pd
import numpy as np

# --- create sample dataframe (replace with your CSV if needed) ---
data = {
    "A": [3, 1, 2, 5],
    "B": [9, 7, 8, 6],
    "C": pd.date_range("2024-01-01", periods=4)
}

df = pd.DataFrame(data)

# --- sorting ---
print(df.sort_values(by="B", ascending=True))
print(df)

# --- column access ---
print(df)
print("----")
print(df["A"])          # bracket notation
print("----")
print(df.A[0:3])        # dot notation slice
print("----")
print(type(df.A))
print(df.A.values)
print(type(df.A.values))

print(df)
print("\n\n\n")

# --- working with column C ---
print(df["C"])
print(type(df["C"]))


print(df["C"].iloc[1])

# --- working with column C ---
print(df["C"])
print(type(df["C"]))

# correct way to access second element
print(df["C"].iloc[1])

print(df)
print("-----")

# row selection
print(df.iloc[1])   # second row (safe)
# print(df.loc[1])  # only works if index actually has label 1

print("-----")

# ❌ OLD (caused error)
# print(df.iloc[3, 3])

# ✅ FIXED (last valid row instead)
print(df.iloc[2, 3])   # row 2, column 3

print("-----")

# slicing (this one was already fine)
print(df.iloc[1:3, 2:4])

print("-----")
print(df.iloc[[0, 1, 2], [1, 2]])



