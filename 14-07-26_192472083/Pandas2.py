import pandas as pd
data = {
    "Name": ["Anu", "Ravi", "Sai"],
    "Age": [20, 21, 19]
}
df = pd.DataFrame(data)
print(df["Name"])