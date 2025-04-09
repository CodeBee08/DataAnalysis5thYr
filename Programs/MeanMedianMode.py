import pandas as pd
from values import cleaned_csv_file

df = pd.read_csv(cleaned_csv_file)
#print(df.to_string())
chest_pain_types = ('Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic')

def mean():
    mean_age = df['age'].mean()
    return f'The mean of Age is {round(mean_age, 2)}'
a = mean()
print(a)

def median():
    median_chol = df['chol'].median()
    return f'The median of Cholesterol is {median_chol}'
a = median()
print(a)

def mode():
    mode_cp = df['cp'].mode()[0]
    return f'The mode of Chest Pain (cp)  is {chest_pain_types[mode_cp]}'
a = mode()
print(a)