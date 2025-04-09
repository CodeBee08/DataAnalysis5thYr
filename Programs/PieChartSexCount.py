# 8.2.1	Counting Values 
import plotly.express as px
import pandas as pd

mapping = {
    0: 'Female',
    1: 'Male'
}

cleaned_csv_file = '/Users/poornima/Desktop/Workspace/DA/Data/heart_cleaned.csv'
df = pd.read_csv(cleaned_csv_file)

# Function to count occurrences
def count_sex_values():
    hd_present_df = df[df['target'] == 1] #this filters only data with heart disease
    fieldCounts = hd_present_df['sex'].value_counts().reset_index()
    fieldCounts.columns = ['Sex', 'Count']  # Try this if graph fails to show
    fieldCounts['Sex'] = fieldCounts['Sex'].map(mapping)
    return fieldCounts  # value_counts() groups the values before counting
                                          # value_counts() creates a new column called 'count'

a = count_sex_values()
print(a)

#8.2.2	Plotting a Pie Chart {Using Counted Values} 

def plot_count_sex_values():
    fieldCounts = count_sex_values()  # Get the counts DataFrame

    fig = px.pie(
        fieldCounts, 
        names='Sex',  
        values='Count',  
        title="Distribution of Sex",
        template="plotly_dark"
    )
    fig.show()
plot_count_sex_values()