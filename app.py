import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output,State
from dash.exceptions import PreventUpdate

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("fossil-fuel-co2-emissions-by-nation.csv")
df = df[['Year', 'Country', 'Total']]

d = list(set(df['Year']))

app.layout = html.Div([

    html.H1("Fossil Fuel Emission Dashboard", style={'text-align': 'center'}),

    dcc.Dropdown(id = "slct_year",
                 options = d,
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='map', figure={})

])


@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    
    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    
    fig = px.choropleth(
        data_frame=dff.where(dff['Year'] == option_slctd),
        locationmode='country names',
        locations='Country',
        scope="world",
        color='Total',
        color_continuous_scale=px.colors.sequential.Blues
    )


    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)
