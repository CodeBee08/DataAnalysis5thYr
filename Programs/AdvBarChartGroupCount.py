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
    df_bar.columns = ['No Heart Disease Count', 'Heart Disease Count']
    df_bar.index.name = 'Chest Pain Type'
    df_bar.reset_index(inplace=True)
    print(df_bar.to_string())
    df_bar['Chest Pain Type'] = df_bar['Chest Pain Type'].map(mapping)
    fig = px.bar(df_bar,
                 x='Chest Pain Type',
                 y=['No Heart Disease Count', 'Heart Disease Count'],
                 title='Heart Disease Count by Chest Pain Type',
                 labels={'value': 'Count', 'variable': 'Heart Disease'},
                 barmode='group')
    fig.update_layout(xaxis_title='Chest Pain Type',
                      yaxis_title='Count',
                      legend_title_text='Heart Disease')
    fig.show()  
count_hd_by_cp()