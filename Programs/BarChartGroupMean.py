import plotly.express as px
import pandas as pd

mapping = {
    0: 'Female',
    1: 'Male'
}

def mean_chol_by_sex():
    cleaned_csv_file = '/Users/poornima/Desktop/Workspace/DA/Data/heart_cleaned.csv'
    df = pd.read_csv(cleaned_csv_file)
    sex_chol_mean_df = df.groupby('sex')['chol'].mean().reset_index()
    sex_chol_mean_df['sex'] = sex_chol_mean_df['sex'].map(mapping)
    fig = px.bar(
        sex_chol_mean_df, 
        x='sex', 
        y='chol',  
        title="Average Cholesterol by Sex",
        labels={'sex': 'Sex'},
        template="plotly_dark",
        color='sex'  
    )
    fig.show()  
mean_chol_by_sex()