import pandas as pd
import os


# ImportDataFiles
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, '..', 'dataset', 'cancer.csv')

df = pd.read_csv(file_path)
print(df.head())

# ExportDataFiles
with open("output/output.txt", "w") as f:
    f.write("Hello World\n")
    f.write(df.head().to_string())

