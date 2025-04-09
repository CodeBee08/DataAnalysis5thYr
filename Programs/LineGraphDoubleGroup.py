import plotly.graph_objects as go
import pandas as pd

def thalach_and_chol_for_age():
    cleaned_csv_file = '/Users/poornima/Desktop/Workspace/DA/Data/heart_cleaned.csv'
    df = pd.read_csv(cleaned_csv_file)
    
    df_thalch = df.groupby('age')['thalach'].mean().reset_index()
    df_chol = df.groupby('age')['chol'].mean().reset_index()

    fig = go.Figure() 
    fig.add_trace(go.Scatter( 
        x=df_thalch['age'], 
        y=df_thalch['thalach'],  
        mode='lines+markers',
        name='Max Heart Rate Info'
    ))
    fig.add_trace(go.Scatter( 
        x=df_chol['age'], 
        y=df_chol['chol'],  
        mode='lines+markers',
        name='Cholesterol Info'
    ))
    fig.update_layout(
        title="Heart Rate and Cholesterol levels by Age",
        xaxis_title="Age",
        yaxis_title="Heart Rate and Cholesterol",
        template="plotly_dark"
    )
    fig.show()
thalach_and_chol_for_age()