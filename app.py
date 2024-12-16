import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

# Création de l'application Dash
app = dash.Dash()
# Charger les données
df = pd.read_csv('DATA\LifeExpectancyData.csv')

developing_country = df[df['status']=='developing']

avg_developing = developing_country.groupby('year')[['adult mortality','percentage expenditure']].mean().reset_index()

y_max = df['bmi'].max()

# Définir la disposition de l'application Dash
app.layout = html.Div([
    html.H1("Dashboard"),
    html.Div([

    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='united states of america',  
        clearable=False
    ),
    dcc.Graph(id='BMI'),
    ]),
    html.Img(src='assets\bmi_indicator.jpg')
    ])

@app.callback(
    Output('BMI', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    bmi_per_country = px.line(
        filtered_df,
        x='year',
        y='bmi',
        title=f'BMI de {selected_country} par an ',
        markers=True
    )
    bmi_per_country.update_layout(yaxis=dict(range=[0, y_max], title="BMI"), xaxis_title="année")
    return bmi_per_country

# Lancer l'application Dash
if __name__ == '__main__':
    app.run_server()
