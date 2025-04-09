# 8.2.1	Counting Values 
import plotly.express as px
import pandas as pd

mapping = {
    0: 'No Heart Disease',
    1: 'Heart Disease'
}

cleaned_csv_file = '/Users/poornima/Desktop/Workspace/DA/Data/heart_cleaned.csv'
df = pd.read_csv(cleaned_csv_file)

# Function to count occurrences
def count_hd_values():
    fieldCounts = df['target'].value_counts().reset_index()
    fieldCounts.columns = ['Presence of Heart Disease', 'Count']  # Try this if graph fails to show
    fieldCounts['Presence of Heart Disease'] = fieldCounts['Presence of Heart Disease'].map(mapping)
    return fieldCounts  # value_counts() groups the values before counting
                                          # value_counts() creates a new column called 'count'

a = count_hd_values()
print(a)

#8.2.2	Plotting a Pie Chart {Using Counted Values} 

def plot_count_hd_values():
    fieldCounts = count_hd_values()  # Get the counts DataFrame

    fig = px.pie(
        fieldCounts, 
        names='Presence of Heart Disease',  
        values='Count',  
        title="Distribution of Presence of Heart Disease",
        template="plotly_dark"
    )
    fig.show()
plot_count_hd_values()