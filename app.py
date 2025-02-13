from dash import Dash, dcc, html
from data_analysis import (
    fig_age_suicide,
    fig_most_suicides,
    fig_least_suicides,
    fig_pop_vs_suicides,
    fig_gdp_vs_suicides,
    fig_year_trend,
    fig_sex_suicide,
    fig_generation_suicide
)

app = Dash(__name__)

app.layout = html.Div(
    style={'backgroundColor': 'black', 'color': 'white', 'padding': '20px'},
    children=[
        # Header
        html.H1("Suicide Data Analysis Dashboard", style={'textAlign': 'center'}),

        # --------------------------------------------------------- Row 1 ------------------------------------------------------------
        html.Div(
            style={'display': 'flex', 'justifyContent': 'space-between'},
            children=[
                # Column 1: 
                html.Div(
                    style={'width': '48%'},
                    children=[
                        dcc.Graph(figure=fig_age_suicide),
                        html.P("Average Suicide Rate by Age Category", style={'textAlign': 'center'})
                    ]
                ),
                # Column 2: 
                html.Div(
                    style={'width': '48%'},
                    children=[
                        dcc.Graph(figure=fig_most_suicides),
                        html.P("Top 10 Countries with Most Suicides", style={'textAlign': 'center'})
                    ]
                )
            ]
        ),

        # --------------------------------------------------------- Row 2 ------------------------------------------------------------
        html.Div(
            style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '20px'},
            children=[
                # Column 1: 
                html.Div(
                    style={'width': '48%'},
                    children=[
                        dcc.Graph(figure=fig_least_suicides),
                        html.P("Top 10 Countries with Least Suicides", style={'textAlign': 'center'})
                    ]
                ),
                # Column 2: 
                html.Div(
                    style={'width': '48%'},
                    children=[
                        dcc.Graph(figure=fig_pop_vs_suicides),
                        html.P("Effect of Population on Suicide Rates", style={'textAlign': 'center'})
                    ]
                )
            ]
        ),

        
        # --------------------------------------------------------- Row 3 ------------------------------------------------------------
        html.Div(
            style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '20px'},
            children=[
                # Column 1: 
                html.Div(
                    style={'width': '48%'},
                    children=[
                        dcc.Graph(figure=fig_gdp_vs_suicides),
                        html.P("Effect of GDP per Capita on Suicide Rates", style={'textAlign': 'center'})
                    ]
                ),
                # Column 2:
                html.Div(
                    style={'width': '48%'},
                    children=[
                        dcc.Graph(figure=fig_year_trend),
                        html.P("Trend of Suicide Rates Across the Years", style={'textAlign': 'center'})
                    ]
                )
            ]
        ),

        # --------------------------------------------------------- Row 4 ------------------------------------------------------------
        html.Div(
            style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '20px'},
            children=[
                # Column 1:
                html.Div(
                    style={'width': '48%'},
                    children=[
                        dcc.Graph(figure=fig_sex_suicide),
                        html.P("Average Suicide Rate by Sex", style={'textAlign': 'center'})
                    ]
                ),
                # Column 2:
                html.Div(
                    style={'width': '48%'},
                    children=[
                        dcc.Graph(figure=fig_generation_suicide),
                        html.P("Suicides by Generation", style={'textAlign': 'center'})
                    ]
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
