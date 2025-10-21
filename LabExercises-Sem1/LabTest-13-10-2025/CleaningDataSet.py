import numpy as np
import pandas as pd

pd.set_option('future.no_silent_downcasting', True)

data = {
    'Age': [25, '?', 30, 35, '?', 28],
    'Income': ['?', 45000, 55000, '?', 65000, 48000],
    'Education': ['Bachelors', '?', 'Masters', 'PhD', 'Bachelors', '?']
}

df = pd.DataFrame(data)

df = df.replace('?', np.nan)

print("\nDataFrame after replacing '?' with NaN:")
print(df)

print("\nData Info after cleaning:")
print(df.info())

print("\nNumber of NaN values in each column:")
print(df.isna().sum())

#Save the cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)