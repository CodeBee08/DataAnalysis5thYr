import plotly.graph_objects as go
import pandas as pd

def trestbps_chol_correlation():
    cleaned_csv_file = '/Users/poornima/Desktop/Workspace/DA/Data/heart_cleaned.csv'
    df = pd.read_csv(cleaned_csv_file)
    
    fig = go.Figure() # Creates an 'empty’ canvas for graph
    fig.add_trace(go.Scatter( 
        x=df['trestbps'], # x-axis column data
        y=df['chol'],  # y=axis column data
        mode='markers', # lines on graph and points on lines
        name='Resting Heart Rate vs Cholesterol'
    ))
    # Labels and Theme
    fig.update_layout(
        title="Scatter Plot:  Correlation of Resting Heart Rate to Cholesterol",
        xaxis_title="Resting Heart Rate",
        yaxis_title="Cholesterol",
        template="plotly_dark" # plotly_white
    )
    fig.show() # Show Chart
trestbps_chol_correlation()
