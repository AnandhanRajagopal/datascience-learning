import pandas as pd
import numpy as np
import os


# base_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(base_dir, "..", "dataset", "cancer.csv")

# df = py.read_csv(file_path)

# print(df.head())
# file_path1 = os.path.join(base_dir, "..", "dataset", "cancerrrrrrr.csv")
# df.to_csv(file_path1)

y = [33, 44, 29, 16, 25, 45, 33, 19, 54, 22, 21, 49, 11, 24, 56]

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

shops = ["Shop1", "Shop2", "Shop3"]

data = np.array(y).reshape(5,3)

df = pd.DataFrame(data, columns=shops, index=days)

print(df)

print(df.describe(include='all').T)

print (df.T.describe())