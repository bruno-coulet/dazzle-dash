import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

class LifeExpectancyApp:
    def __init__(self, df):
        self.df = df
        self.df_filtered = self.df[['country', 'year', 'life expectancy']]

    def create_figure(self, selected_countries):
        if not selected_countries:
            return go.Figure()  # Retourner un graphique vide si aucun pays n'est sélectionné
        filtered_df = self.df_filtered[self.df_filtered['country'].isin(selected_countries)]
        fig = px.line(filtered_df, x='year', y='life expectancy', color='country', title='Life Expectancy by Country and Year')
        return fig

class AdultMortalityApp:
    def __init__(self, df):
        self.df = df
        self.df_filtered = self.df[['country', 'year', 'adult mortality']]

    def create_figure(self, selected_countries):
        if not selected_countries:
            return go.Figure()  # Retourner un graphique vide si aucun pays n'est sélectionné
        filtered_df = self.df_filtered[self.df_filtered['country'].isin(selected_countries)]
        fig = px.line(filtered_df, x='year', y='adult mortality', color='country', title='Adult Mortality by Country and Year')
        return fig

class Top10App:
    def __init__(self, df):
        self.df = df

    def create_figure(self, selected_column):
        if not selected_column:
            return go.Figure()  # Retourner un graphique vide si aucune colonne n'est sélectionnée
        avg_df = self.df.groupby('country')[selected_column].mean().reset_index()
        top_10 = avg_df.nlargest(10, selected_column)
        fig = px.bar(top_10, x='country', y=selected_column, title=f'Top 10 Countries by {selected_column.capitalize()}')
        return fig

class HealthDataApp:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.life_expectancy_app = LifeExpectancyApp(self.df)
        self.adult_mortality_app = AdultMortalityApp(self.df)
        self.top_10_app = Top10App(self.df)
        self.app = dash.Dash(__name__)
        self.setup_layout()
        self.setup_callbacks()

    def setup_layout(self):
        self.app.layout = html.Div([
            html.H1("Health Data by Country and Year"),
            dcc.Dropdown(
                id='data-type-dropdown',
                options=[
                    {'label': 'Life Expectancy', 'value': 'life_expectancy'},
                    {'label': 'Adult Mortality', 'value': 'adult_mortality'}
                ],
                value='life_expectancy',
                placeholder='Select Data Type'
            ),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in self.df['country'].unique()],
                value=[],  # Aucun pays sélectionné par défaut
                multi=True,
                placeholder='Select Countries'
            ),
            dcc.Graph(id='line-chart'),
            html.H1("Top 10"),
            dcc.Dropdown(
                id='top-10-dropdown',
                options=[{'label': col, 'value': col} for col in self.df.columns if col not in ['country', 'year', 'status']],
                placeholder='Select Column for Top 10'
            ),
            dcc.Graph(id='top-10-chart')
        ])

    def setup_callbacks(self):
        @self.app.callback(
            Output('line-chart', 'figure'),
            [Input('data-type-dropdown', 'value'),
             Input('country-dropdown', 'value')]
        )
        def update_graph(data_type, selected_countries):
            if data_type == 'life_expectancy':
                return self.life_expectancy_app.create_figure(selected_countries)
            else:
                return self.adult_mortality_app.create_figure(selected_countries)

        @self.app.callback(
            Output('top-10-chart', 'figure'),
            [Input('top-10-dropdown', 'value')]
        )
        def update_top_10(selected_column):
            return self.top_10_app.create_figure(selected_column)

    def run(self):
        self.app.run_server(debug=True)

if __name__ == '__main__':
    health_data_app = HealthDataApp('processed_data/LifeExpectancyData.csv')
    health_data_app.run()
