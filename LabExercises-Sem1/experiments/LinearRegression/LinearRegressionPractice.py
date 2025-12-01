import pandas as pd
import numpy as np
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "Algerian_forest.csv")
data = pd.read_csv(file_path)
df = pd.DataFrame(data)

print(df.head())

updated_data = df.dropna()

print(updated_data)

df["Classes_num"] = df["Classes  "].map({'not fire   ': 0, 'fire   ': 1 })
print(df.head(10))

print(df.columns)

feature_cols = ['Temperature', 'RH', 'Ws', 'Rain ']

x = df[['Rain ']]
y = df['FWI']

print(x)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_Scaled = scaler.fit_transform(X_train)
X_test_Scaled = scaler.fit_transform(X_test)

model = LinearRegression()
model.fit(X_test_Scaled, y_train)

y_predict = model.predict(X_test_Scaled)