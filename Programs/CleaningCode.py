import pandas as pd

from values import csv_file, cleaned_csv_file

#import csv
df = pd.read_csv(csv_file)
print(df.to_string())  

# Check Info
print(df.info())

# 1. Removing Any Empty Rows Left with Empty Cells
df = df.dropna()
print(df.to_string())

# 2. Removing Rows where 'age' is greater than 120 and lesser than 17
#this data set contains only data from adults 
for i in df.index:  # Outputs the index of each row
    if df.loc[i, "age"] >= 120 and df.loc[i, 'age'] <= 17:  
        df = df.drop(i)
print(df.to_string())

# 3. Replacing values over 200 in 'trestbps' column with estimate of 131 (unrealistically high heart rates)
df.loc[df['trestbps'] > 200, 'trestbps'] = 131
print(df.to_string())

# 4.Replacing Empty Values in 'chol' Column with Mean cholestrol 
x = df['chol'].mean()
df['chol'] = df['chol'].fillna(x)
print(df.to_string())

#5. Removing apostrophes on 'Thalach' and 'Ca' column.
df['thalach'] = df['thalach'].str.strip("'")
df['ca'] = df['ca'].str.strip("'")
print(df.to_string())

# Convert all the columns except 'oldpeak' to integer
for col in df.columns:
    if col != 'oldpeak':
        df[col] = df[col].astype(int)
# Convert 'oldpeak' to float
df['oldpeak'] = df['oldpeak'].astype(float)
print(df.to_string())
 
# Exporting Cleaned Data
df.to_csv(cleaned_csv_file, index=False)  # Don't include index numbers



