import pandas as pd
data = {
    "Name": ["Anu", "Ravi", "Sai"],
    "Marks": [90, 85, 95]
}
df = pd.DataFrame(data)
print(df.head())