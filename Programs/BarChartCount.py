import plotly.express as px
import pandas as pd
from values import cleaned_csv_file

df = pd.read_csv(cleaned_csv_file)
mapping = {
    0: 'Typical angina',
    1: 'Atypical angina',
    2: 'Non-anginal pain',
    3: 'Asymptomatic'
}    
def count_cp_values():
    fieldCounts = df['cp'].value_counts().reset_index()
    fieldCounts.columns = ['Chest Pain Type', 'Count']  # Try this if graph fails to show
    fieldCounts['Chest Pain Type'] = fieldCounts['Chest Pain Type'].map(mapping)
    return fieldCounts # Two columns are returned:
         # 'EducationField' and a new column called 'count'
a = count_cp_values()
print(a)

# Function to create the Plotly bar chart
def plot_cp_values():
    fieldCount = count_cp_values()  # Get the counts DataFrame
    fig = px.bar(
        fieldCount, 
        x='Chest Pain Type',  # First column (Education Fields)
        y='Count',  # Second column (Counts)
        title="Count of Values for Each Chest Pain Type",
        labels={'EducationField': 'Number of Chest Pain Types'},
        template="plotly_dark",
    )
    fig.show()
plot_cp_values()  