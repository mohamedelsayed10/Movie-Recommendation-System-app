import pandas as pd
import dash
from dash import html, Input, Output, callback, dcc
import dash_bootstrap_components as dbc

movies = pd.read_csv("ml-latest-small/movies.csv")

dash.register_page(__name__, path="/movie")

movie_titles = movies["title"].unique()

movie_dropdown = dcc.Dropdown(
    id="movie-dropdown",
    options=[{"label": movie, "value": movie} for movie in movie_titles],
    placeholder="Select Movie",
    value=movie_titles[0],
    style={"width": "230px", "height": "fit-content", "color": "black"},
)

layout = dbc.Row(
    [
        dbc.Col(
            dbc.Button(
                html.Img(src="/assets/BP.png", style={"width": "50px"}),
                href="/",
                style={"backgroundColor": "transparent", "border": "none"},
            ),
            width=1,
        ),
        dbc.Col(
            html.Img(src="/assets/skelton.gif", style={"maxWidth": "100%", "height": "auto"}),
            width=5,
            style={"display": "flex", "alignItems": "center", "justifyContent": "right"},
        ),
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H3(
                                    "Select Movie",
                                    style={
                                        "color": "white",
                                        "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",
                                        "fontSize": "24px",
                                    },
                                ),
                                movie_dropdown,
                                dbc.Button(
                                    "Submit",
                                    href="",
                                    id="movie-submit-button",
                                    style={
                                        "backgroundColor": "transparent",
                                        "border": "2px solid #bb00ff",
                                        "color": "white",
                                        "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",
                                        "boxShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",
                                        "marginTop": "10px",
                                        "fontSize": "24px",
                                    },
                                ),
                            ],
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "center",
                                "justifyContent": "center",
                                "gap": "10px",
                            },
                        ),
                    ],
                    style={
                        "paddingInline": "100px",
                        "marginBlock": "auto",
                    },
                )
            ],
            width=4,
            style={"display": "flex", "flexDirection": "column", "height": "100vh", "justifyContent": "center"},
        ),
    ],
    style={
        "backgroundImage": "url('/assets/pr.jpg')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",  
        "minHeight": "100vh",
        "maxWidth": "100vw",
        "overflowX": "hidden",
        "paddingInline": "50px",
    },
    align="center",
)

@callback(
    Output("movie-submit-button", "href"),
    Input("movie-dropdown", "value"),
)
def submit(movie):
    return f"/movie/results?title={movie}"
