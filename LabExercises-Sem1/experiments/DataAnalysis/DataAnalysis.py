import pandas as pd
import numpy as np
from scipy import special, linalg, optimize
import os
import math
import matplotlib.pyplot as plt


## 1. Reading the dataset from excel format
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, '..','..', 'dataset', 'smartphones.csv')
df = pd.read_csv(file_path)

##print("SmartPhone Specs Details Collection")
#print(df.head())

## 2. Display DataType of resolution_width colum
#print("Datatype of resolution_width column: ", df['resolution_width'].dtype)


## 3. Renaming the column  names
df.rename(columns = {'avg_rating' : 'Average_Rating', 'battery_capacity' : 'Battery_Capacity'}, inplace=True)
#print("Columns Renamed:\n", df.columns)

## 4. Add additional column
df['Available_On_Flipkart'] = df['5G_or_not']
#print(df.head())

## 5. Find Correlation
#print("Correlation Matrix: ", df.corr(numeric_only=True))

## 6. Reading to 10 and bottom 10 records
#print("Top 10 records: \n", df.head(10))
#print("Bottom 10 records: \n", df.tail(10))

## 7. Reading the header
#print("Header Columns: ", df.columns.to_list())


## 8. Reading data on column basis
#print("Available_On_Flipkart Column Data: \n ", df['Available_On_Flipkart'].head(6))

## 9. Reading Specific data
#print("Specific Data [Row 2, Column 'Available_On_Flipkart']", df.loc[2, 'Available_On_Flipkart'])

## 10. Reading data of a specific tuple
# (a) index ranges (b) specific index
#print("Index Range 0-5: \n", df.iloc[0:5])
#print("Specific Index (3): \n" , df.loc[3])

## 11. Rows with indexes 3 to 7
#print(df.loc[3:7])

## 12. Display rows with indexes 5 to 0 (Reverse Order)
print(df.loc[5::-1])

## 13 Display rows with odd indexes from 1 to 7
print(df.loc[1:7:2])

## 14 Display all the rows where "any condition"
print(df[df['brand_name']=="jio"])

## 15 Reading data in a tuple-wise order
print("Tuple-Wise Data: ")
#for row in df.itertuples():
   # print(row)

## 16 Reading data in a column wise order
# for col in df.columns:
#     print(col, ":\n", df[col].head())

## 17 Display shape attribute
print("Shape of Dataset:", df.shape)

# 18 Filtering on multiple attributes (e.g., Apple brand AND ram > 4)
print("\n--- Filtering: Apple phones with more than 6GB RAM ---")
condition1 = df['brand_name'] == 'apple'
condition2 = df['ram_capacity'] > 6
print(df[condition1 & condition2])

# 19 Filtering data on the basis of a particular pattern (string contains)
print("\n--- Filtering: Models containing 'Pro' ---")
print(df[df['model'].str.contains('Pro', case=False, na=False)])

# 20 Filtering data on basis of particular regex (e.g., processor is 'bionic' OR 'tensor')
print("\n--- Filtering (Regex): Processor is 'bionic' or 'tensor' ---")
print(df[df['processor_brand'].str.contains(r'bionic|tensor', na=False)])

