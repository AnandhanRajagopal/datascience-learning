import pandas as pd
import numpy as np
import math

marks = [98,56, "P" ,78,43, "P", 56,23, "F", 67,87, "P", 99,54, "P", 78,27, "F", 77,45, "P", 56,57, "P",  89,34, "F" ,44,43, "P"]

data = np.array(marks).reshape(10,3)

results_mapping = {
    "P": 1,
    "F": 0
}

df = pd.DataFrame(data, columns=["sub1", "sub2", "result"])
df['sub1'] = pd.to_numeric(df['sub1'])
df['sub2'] = pd.to_numeric(df['sub2'])

df['result'] = df['result'].map(results_mapping)
df['result'] = pd.to_numeric(df['result'])

print("Mean")
print(df[['sub1', 'sub2', 'result']].mean())

print("\nMedian:")
print(df[['sub1', 'sub2', 'result']].median())

print("\nMode:")
print(df[['sub1', 'sub2', 'result']].mode())

print("\nStandard Deviation:")
print(df[['sub1', 'sub2', 'result']].std())

print("\nVariance:")
print(df[['sub1', 'sub2', 'result']].var())

print("\nCorrelation between sub1 and sub2:")
print(df['sub1'].corr(df['sub2']))

print("\nCovariance Matrix:")
print(df[['sub1', 'sub2', 'result']].cov())

print("\nResult Distribution:")
print(df['result'].value_counts())

print("\nOverall Mean")
print(df.mean().mean())

print("\nOverall Median")
print(df.median().median())

print("\nOverall Mode")
print(df.mode().mode())

print("\nOverall Standard Deviation")
print(df.std().std())

print("\nOverall Variance")
print(df.var().var())

  