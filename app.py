import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Dictionnaire des descriptions des colonnes
COLUMN_DESCRIPTIONS = {
    'life expectancy': 'L\'espérance de vie à la naissance (en années).',
    'adult mortality': 'Le taux de mortalité des adultes exprimé pour 1000 adultes âgés de 15 à 60 ans.',
    'infant deaths': 'Le nombre absolu de décès infantiles (moins d\'un an).',
    'alcohol': 'La consommation d\'alcool par habitant (litres par an).',
    'percentage expenditure': 'Le pourcentage des dépenses de santé par rapport au produit intérieur brut (PIB).',
    'hepatitis b': 'La couverture vaccinale contre l\'hépatite B (% de la population).',
    'measles': 'Le nombre de cas de rougeole.',
    'bmi': 'L\'indice de masse corporelle moyen de la population.',
    'under-five deaths': 'Le nombre absolu de décès d\'enfants de moins de 5 ans.',
    'polio': 'La couverture vaccinale contre la poliomyélite (% de la population).',
    'total expenditure': 'Les dépenses totales de santé par habitant (% du PIB).',
    'diphtheria': 'La couverture vaccinale contre la diphtérie (% de la population).',
    'hiv/aids': 'Le taux de prévalence du VIH/sida (% de la population).',
    'gdp': 'Le produit intérieur brut (PIB) par habitant (en dollars américains).',
    'population': 'La population totale.',
    'thinness 1-19 years': 'Le pourcentage de maigreur chez les personnes âgées de 1 à 19 ans.',
    'thinness 5-9 years': 'Le pourcentage de maigreur chez les enfants âgés de 5 à 9 ans.',
    'income composition of resources': 'L\'indice de développement humain basé sur les ressources (échelle de 0 à 1).',
    'schooling': 'Le nombre moyen d\'années de scolarité.'
}


class ColumnByCountryYearApp:
    def __init__(self, df, column, title):
        self.df = df
        self.df_filtered = self.df[['country', 'year', column]]
        self.column = column
        self.title = title

    def create_figure(self, selected_countries):
        if not selected_countries:
            return go.Figure()  # Retourner un graphique vide si aucun pays n'est sélectionné
        filtered_df = self.df_filtered[self.df_filtered['country'].isin(selected_countries)]
        fig = px.line(filtered_df, x='year', y=self.column, color='country', title=self.title)
        return fig

class Top10App:
    def __init__(self, df):
        self.df = df

    def create_figure(self, selected_column, start_year, end_year):
        if not selected_column:
            return go.Figure()  # Retourner un graphique vide si aucune colonne n'est sélectionnée
        filtered_df = self.df[(self.df['year'] >= start_year) & (self.df['year'] <= end_year)]
        avg_df = filtered_df.groupby('country')[selected_column].mean().reset_index()
        top_10 = avg_df.nlargest(10, selected_column)
        fig = px.bar(top_10, x='country', y=selected_column, title=f'Top 10 Countries by {selected_column.capitalize()} ({start_year}-{end_year})')
        fig.update_yaxes(type='log')  # Mettre à jour l'échelle de l'axe des y en logarithmique
        return fig

class CorrelationApp:
    def __init__(self, df):
        self.df = df

    def create_figure(self, selected_columns):
        if not selected_columns:
            return go.Figure()  # Retourner un graphique vide si aucune colonne n'est sélectionnée
        corr_df = self.df[selected_columns].corr()
        fig = px.imshow(corr_df, text_auto=True, title='Correlation Matrix')
        return fig
    

class DataApp:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.app = dash.Dash(__name__)
        self.setup_layout()
        self.setup_callbacks()

    def setup_layout(self):
        self.app.layout = html.Div([
            html.H1("Data by Country and Year"),
            dcc.Dropdown(
                id='data-type-dropdown',
                options=[{'label': col, 'value': col} for col in COLUMN_DESCRIPTIONS.keys()],
                value='life expectancy',
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
            html.Div(id='description', style={'marginTop': 20}),
            html.H1("Top 10"),
            dcc.Dropdown(
                id='top-10-dropdown',
                options=[{'label': col, 'value': col} for col in self.df.columns if col not in ['country', 'year', 'status']],
                placeholder='Select Column for Top 10'
            ),
            dcc.RangeSlider(
                id='year-range-slider',
                min=self.df['year'].min(),
                max=self.df['year'].max(),
                value=[self.df['year'].min(), self.df['year'].max()],
                marks={str(year): str(year) for year in range(self.df['year'].min(), self.df['year'].max() + 1)}
            ),
            dcc.Graph(id='top-10-chart'),
            html.H1("Correlation Matrix"),
            dcc.Dropdown(
                id='correlation-columns-dropdown',
                options=[{'label': col, 'value': col} for col in self.df.columns if col not in ['country', 'year', 'status']],
                value=[],  # Aucune colonne sélectionnée par défaut
                multi=True,
                placeholder='Select Columns for Correlation'
            ),
            dcc.Graph(id='correlation-chart')
        ])

    def setup_callbacks(self):
        @self.app.callback(
            Output('line-chart', 'figure'),
            [Input('data-type-dropdown', 'value'),
             Input('country-dropdown', 'value')]
        )
        def update_graph(data_type, selected_countries):
            app = ColumnByCountryYearApp(self.df, data_type, f'{data_type.capitalize()} by Country and Year')
            return app.create_figure(selected_countries)

        @self.app.callback(
            Output('top-10-chart', 'figure'),
            [Input('top-10-dropdown', 'value'),
             Input('year-range-slider', 'value')]
        )
        def update_top_10(selected_column, year_range):
            start_year, end_year = year_range
            app = Top10App(self.df)
            return app.create_figure(selected_column, start_year, end_year)

        @self.app.callback(
            Output('correlation-chart', 'figure'),
            [Input('correlation-columns-dropdown', 'value')]
        )
        def update_correlation(selected_columns):
            app = CorrelationApp(self.df)
            return app.create_figure(selected_columns)

        @self.app.callback(
            Output('description', 'children'),
            [Input('data-type-dropdown', 'value')]
        )
        def update_description(selected_column):
            return html.P(COLUMN_DESCRIPTIONS.get(selected_column, ''))

    def run(self):
        self.app.run_server(debug=True)

if __name__ == '__main__':
    data_app = DataApp('processed_data/LifeExpectancyData.csv')
    data_app.run()
