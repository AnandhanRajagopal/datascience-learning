import numpy as np
import pandas as pd

ages = [1,2,2,3]

print("Mean: " + str(np.mean(ages)))  # Mean
print("Median: " + str(np.median(ages)))  # Median
print("StandardDeviation: " + str(np.std(ages)))  # Standard Deviation
print("Variance: " + str(np.var(ages)))  # Variance
df  = pd.DataFrame(ages, columns=['ages'])
print("Mode: " + str(df.ages.mode()))  # Mode

q1 = np.percentile(ages, 25)
q3 = np.percentile(ages, 75)

iqr = q3 - q1
print(f"Interquartile Range (IQR): {iqr}")
print("Range: " + str(np.max(ages) - np.min(ages)))  # Range