# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px


dataset = pd.read_csv('processed_data/LifeExpectancyData.csv')


style = ['style.css']
app = Dash()


app.layout = [
    
    # INUTILE : html.Tbody(style={'background-color':'black'}),

    html.H1("Analyse sur l'espérance de vie mondiale",
            style={'textAlign': 'center',
                   'color': 'darkgrey',
                   'fontSize': 30}
             ),

    # Horizontal line separator
    html.Hr(style={'color':'darkgrey'}),
    
    html.H2("Jeu de donnée étudiée, fournie par l'OMS",
            style={'textAlign': 'center', 'color': 'brown', 'fontSize': 20}
             ),

    # dash_table.DataTable(data=dataset.to_dict('records'), page_size=10),
    html.Div(className='row', children=[
        html.Div(
                children=[
                    dash_table.DataTable(
                        data=dataset.to_dict('records'),
                        page_size=11,
                        style_table={'overflowX': 'auto'}
                    )
                ]
        ),


    html.H2("Pas encore défini",
        style={'textAlign': 'center', 'color': 'brown', 'fontSize': 20}
            ),
    html.Div(
        children=[
            dcc.Graph(
                figure={},
                id='histo-chart'
            )
        ]
    )

    ]),


    html.Div(className='row', children=[
        dcc.RadioItems(
            options=[
            {'label': 'Population', 'value': 'population'},
            {'label': 'Espérance de vie''Espérance de vie', 'value': 'life expectancy'},
            {'label': 'Dépense de santé/PIB', 'value': 'percentage expenditure'}
            ],
            value='population',
            inline=True,
            id='radio-buttons')
    ]),


    html.Div(className='row', children=[
        dcc.Dropdown(
            options=[
            {'label': 'Population', 'value': 'population'},
            {'label': 'Espérance de vie''Espérance de vie', 'value': 'life expectancy'},
            {'label': 'Dépense de santé/PIB', 'value': 'percentage expenditure'}
            ],
            value = 'population',
            id='dropdown'
        ),
        html.Div(id='dd-output-container')
    ]),


    # # Initial histogram chart
    # dcc.Graph(figure=px.histogram(dataset, x='country', y='life expectancy', histfunc='avg')),

    # # Histogram chart with callback
    # dcc.Graph(id='controls')

]







# Controls to build the interaction
# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='radio-buttons', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(dataset, x='year', y=col_chosen, histfunc='avg')
#     return fig

@callback(
    Output(component_id='histo-chart', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(dataset, x='year', y=col_chosen, histfunc='avg')
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug='True')




