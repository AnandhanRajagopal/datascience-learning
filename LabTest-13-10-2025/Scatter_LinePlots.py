import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Semester" : [1,2,3,4,5,6,7,8],
    "Grades" : ["A+", "D", "A", "B+", "A+", "A", "D", "B+"]
}
df = pd.DataFrame(data)

print(df)

grade_mapping = {
    'A+' : 10, 
    'A': 9,
    'B+' : 8,
    'B': 7,
    'D' : 4
}

#Converting grades to numeric values
df['Numeric_Grades'] = df['Grades'].map(grade_mapping)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(df['Semester'], df['Numeric_Grades'], color='blue', marker='o')
plt.title("Semester Grades - Scatter Plot")
plt.xlabel("Semester")
plt.ylabel("Grades")
plt.grid(True, linestyle="--", alpha= 0.7)
plt.yticks(list(grade_mapping.values()), list(grade_mapping.keys()))

plt.subplot(1,2,2)
plt.plot(df['Semester'], df['Numeric_Grades'], 'r-o',color='blue', linewidth=2, markersize  = 8)
plt.title("Semester Grades - Line Plot")
plt.xlabel("Semester")
plt.ylabel("Grades")
plt.yticks(list(grade_mapping.values()), list(grade_mapping.keys()))
plt.grid(True, linestyle="-", alpha= 0.7)
plt.tight_layout()

plt.show()