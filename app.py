from dash import Dash, dcc, html
from data_analysis import (
    fig_age_suicide,
    fig_country_suicide,
    fig_generation_suicide
)

app = Dash(__name__)

app.layout = html.Div(
    style={'backgroundColor': 'black', 'color': 'white', 'padding': '20px'},
    children=[
        # Header
        html.H1("Suicide Data Analysis Dashboard", style={'textAlign': 'center'}),

        # ----------------------------------------------------- Row 1 ---------------------------------
        html.Div(
            children=[
                dcc.Graph(figure=fig_age_suicide),
                html.P(
                    "Is the suicide rate more prominent in some age categories than others?",
                    style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'}
                )
            ]
        ),

        # ----------------------------------------------------- Row 2 ---------------------------------
        html.Div(
            children=[
                dcc.Graph(figure=fig_country_suicide),
                html.P(
                    "Which countries have the most and the least number of suicides?",
                    style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'}
                )
            ]
        ),

        # ----------------------------------------------------- Row 3 ---------------------------------
        html.Div(
            children=[
                dcc.Graph(figure=fig_generation_suicide),
                html.P(
                    "Show the Number of Suicides by Generation",
                    style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'}
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
