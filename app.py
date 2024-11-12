# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
dataset = pd.read_csv('raw_data/LifeExpectancyData.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    # div title
    html.Div(children="Jeu de donnnée sur l'espérance de vie, avec histogramme et controles"),
    # # Radio button
    # html.Hr(),
    # dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='Life expectancy', id='controls-and-radio-item'),
    # Radio button
    html.Hr(),
    dcc.RadioItems(
        options=[
            {'label': 'Population', 'value': 'Population'},
            {'label': 'Life Expectancy', 'value': 'Life expectancy '},
            {'label': 'GDP per Capita', 'value': 'GDP'}
        ],
        value='Life expectancy ',
        id='controls-and-radio-item'
    ),
    # dataframe Pandas
    dash_table.DataTable(data=dataset.to_dict('records'), page_size=10),

    # histogram chart
    dcc.Graph(figure=px.histogram(dataset, x='Country', y='Life expectancy ', histfunc='avg')),
    # dcc.Graph(figure={}, id='controls-and-graph')
    # Histogram chart with callback
    dcc.Graph(id='controls-and-graph')

]


# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(dataset, x='Country', y=col_chosen, histfunc='avg')
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)




