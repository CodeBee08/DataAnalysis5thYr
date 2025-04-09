import plotly.graph_objects as go
import pandas as pd
from values import cleaned_csv_file

def age_thalach():
    df = pd.read_csv(cleaned_csv_file)
    df = df.groupby('age')['thalach'].mean().reset_index()

    fig = go.Figure() 
    fig.add_trace(go.Scatter( 
        x=df['age'], 
        y=df['thalach'],  
        mode='lines+markers', 
    ))
    fig.update_layout(
        title="Heart Study Grouped",
        xaxis_title="Age",
        yaxis_title="Max Heart Rate Achieved",
        template="plotly_dark" # plotly_white
    )
    fig.show() 
    
age_thalach()