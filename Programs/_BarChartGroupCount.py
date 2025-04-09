import plotly.express as px
import pandas as pd
from values import cleaned_csv_file

mapping = {
    0: 'Typical angina',
    1: 'Atypical angina',
    2: 'Non-anginal pain',
    3: 'Asymptomatic'
}  

def count_hd_by_cp():
    df = pd.read_csv(cleaned_csv_file)
    df_bar = df.groupby('cp')['target'].value_counts().unstack().fillna(0)
    df_bar.columns = ['Chest Pain Type', 'No Heart Disease Count', 'Heart Disease Count']
    print(df_bar.to_string())
    df_bar['Chest Pain Type'] = df_bar['Chest Pain Type'].map(mapping)
    fig = px.bar(
        df_bar, 
        x='Chest Pain Type', 
        y='Heart Disease Count',  
        title="Heart disease count by Chest Pain Type",
        template="plotly_dark",
        color='Chest Pain Type'  
    )
    fig.show()  
count_hd_by_cp()