import dash
from dash import html, dcc, clientside_callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from utils.get_top_similar import get_top_similar
from utils.get_movie_details import get_movie_details

dash.register_page(__name__, path="/movie/results")

df_ratings = pd.read_csv("ml-latest-small/ratings.csv")
df_movies = pd.read_csv("ml-latest-small/movies.csv")
df_movie_details = pd.read_csv("ml-latest-small/movie_details.csv")
df_links = pd.read_csv("ml-latest-small/links.csv")

def pagination_component(images, id_name):
    image_elements = [
        dbc.Card(
            dbc.CardImg(src=img, top=True, className="zoom-image", style={"height": "100%"}),
            style={"marginRight": "20px", "minWidth": "200px", "minHeight": "300px", "transform": "scaleY(1.0)"},  # Adjusted image size here
        )
        for img in images
    ]
    return html.Div(
        [
            dcc.Store(id=f"{id_name}-store-left-clicks", data=0),
            dcc.Store(id=f"{id_name}-store-right-clicks", data=0),
            html.Div(
                [
                    html.Button(
                        html.I(
                            className="fa-solid fa-arrow-left",
                            style={"color": "#bb00ff"},
                        ),
                        id=f"{id_name}-left-arrow",
                        n_clicks=0,
                        className="arrow",
                        style={
                            "height": "40px",
                            "width": "40px",
                            "backgroundColor": "transparent",
                            "border": "none",
                        },
                    ),
                    html.Div(
                        image_elements,
                        id=f"{id_name}-image-container",
                        style={
                            "display": "flex",
                            "flexDirection": "row",
                            "justifyContent": "space-between",
                            "overflow": "hidden",  # Hide the scrollbar
                            "whiteSpace": "nowrap",
                            "width": "calc(100vw - 200px)",
                            "scrollBehavior": "smooth",
                        },
                    ),
                    html.Button(
                        html.I(
                            className="fa-solid fa-arrow-right",
                            style={"color": "#bb00ff"},
                        ),
                        id=f"{id_name}-right-arrow",
                        n_clicks=0,
                        className="arrow",
                        style={
                            "height": "40px",
                            "width": "40px",
                            "backgroundColor": "transparent",
                            "border": "none",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                },
            ),
        ],
        style={
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
        },
    )

def layout(title=None, **other_unknown_query_strings):
    movie_id = df_movies[df_movies["title"] == title]["movieId"].values[0]
    movie_imdb_id = df_links[df_links["movieId"] == movie_id]["imdbId"].values[0]
    movie_poster = df_movie_details[df_movie_details["MovieID"] == movie_imdb_id]["CoverURL"].values[0]

    sim_df = get_top_similar(df_ratings, df_movies, movieid=movie_id, topn=20)
    sim_df = sim_df.merge(df_links, on='movieId')
    sim_df = sim_df.merge(df_movie_details, right_on='MovieID', left_on='imdbId')
    similar_movie_posters = sim_df["CoverURL"].values

    movie_details = get_movie_details(movie_id, df_movies, df_ratings, df_links, df_movie_details)
    
    return html.Div(
        [
            html.Div(
                "",  # Empty Div for background image
                style={
                    "position": "absolute",
                    "top": 0,
                    "left": 0,
                    "width": "100%",
                    "height": "100%",
                    "backgroundImage": "url('/assets/pr.jpg')",
                    "backgroundSize": "cover",
                    "backgroundAttachment": "fixed",
                    "backgroundRepeat": "no-repeat",  # Ensure the image is not repeated
                    "backgroundPosition": "center",  # Center the background image
                    "zIndex": -1,  # Send the background image to the back
                },
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.H1(
                                    title,
                                    style={"color": "inherit", "textAlign": "center", "zIndex": 1, "fontSize": "50px", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff"},  # Ensure text is above background image
                                ),
                                dbc.Card(
                                    dbc.CardImg(src=movie_poster, top=True),
                                    style={
                                        "width": "300px",
                                        # "height": "395px",
                                        "textAlign": "center",
                                        "margin": "0 auto",  # Center the poster horizontally
                                        # "boxShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",
                                    },
                                ),
                            ],
                            style={"textAlign": "center", "zIndex": 1},  # Center content vertically
                        ), width=3
                    ),
                    dbc.Col(
                        html.Div(
                            [ 
                                html.P(
                                    [html.Span("Genres: ", style={"fontWeight": "bold", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff"}) , movie_details["genres"][0]],
                                    style={"color": "inherit", "textAlign": "left", "zIndex": 1, "fontSize":"25px"},  # Ensure text is above background image
                                ),
                                html.P(
                                    [html.Span("Average Rating: ", style={"fontWeight": "bold", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff"}), str(movie_details["avg_rating"])],
                                    style={"color": "inherit", "textAlign": "left", "zIndex": 1, "fontSize":"25px"},  # Ensure text is above background image
                                ),
                                html.P(
                                    [html.Span("Number of Ratings: ", style={"fontWeight": "bold", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff"}), str(movie_details["num_ratings"])],
                                    style={"color": "inherit", "textAlign": "left", "zIndex": 1, "fontSize":"25px"},  # Ensure text is above background image
                                ),
                                html.P(
                                    [html.Span("Directors: ", style={"fontWeight": "bold", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff"}) , movie_details["directors"][0]],
                                    style={"color": "inherit", "textAlign": "left", "zIndex": 1, "fontSize":"25px"},  # Ensure text is above background image
                                ),
                                html.P(
                                    [html.Span("Actors: ", style={"fontWeight": "bold", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff"}) , movie_details["actors"][0]],
                                    style={"color": "inherit", "textAlign": "left", "zIndex": 1, "fontSize":"25px"},  # Ensure text is above background image
                                )
                            ],
                            style={"textAlign": "left", "zIndex": 1},  # Center content vertically
                        ),
                        width=4,
                        style = {"display": "flex", "alignItems": "center"}
                    )
                ],
                id="top",
                style={"marginTop": "50px", "position": "relative","justifyContent": "center"},  # Ensure text is positioned correctly
            ),
            dbc.Row(
                dbc.Button(
                    html.Img(src="/assets/BP.png", style={"width": "50px"}),
                    href="/movie",
                    style={
                        "backgroundColor": "transparent",
                        "border": "none",
                        "textAlign": "left",
                        "width": "fit-content",
                        "position": "relative",  # Ensure button is positioned correctly
                        "zIndex": 1,  # Ensure button is above background image
                    },
                ),
                style={"marginBlock": "20px", "paddingInline": "60px"},
            ),
            dbc.Row(
                [
                    html.H2(
                        "Similar Movies",
                        id="similar-movies-section",  # Add an ID for smooth scrolling
                        style={"color": "inherit", "textAlign": "center", "marginTop": "200px", "zIndex": 1, "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff", "fontSize": "38px"},  # Ensure text is above background image
                    ),
                    pagination_component(similar_movie_posters, "similar"),
                ],
                style={"marginBottom": "200px", "textAlign": "center","textsize": "50px"},
            ),
            html.Button(
                "Go to Similar Movies",
                id="scroll-button",
                style={
                    "backgroundColor": "transparent",
                                        "border": "2px solid #bb00ff",
                                        "color": "white",
                                        "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",
                                        "boxShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",
                                        "marginTop": "10px",
                    "position": "fixed",
                    "bottom": "20px",
                    "left": "20px",
                    # "backgroundColor": "#bb00ff",
                    # "color": "white",
                    # "border": "none",
                    "padding": "10px 20px",
                    "cursor": "pointer",
                    "zIndex": 2,  # Ensure button is above background image
                },
            ),
        ],
        style={
            "backgroundColor": "black",
            "minHeight": "100vh",
            "maxWidth": "100vw",
            "overflowX": "hidden",
            "position": "relative",  # Ensure content stays above the background image
            "zIndex": 1,  # Ensure content is above background image
            "color": "white",
        },
    )

clientside_callback(
    """
    function(n_clicks_left, n_clicks_right, prev_left, prev_right) {
        var container = document.getElementById('similar-image-container');
        if (n_clicks_left > prev_left) {
            container.scrollLeft -= 1000;
        }
        if (n_clicks_right > prev_right) {
            container.scrollLeft += 1000;
        }
        return [n_clicks_left, n_clicks_right];
    }
    """,
    [
        Output("similar-store-left-clicks", "data"),
        Output("similar-store-right-clicks", "data"),
    ],
    [
        Input("similar-left-arrow", "n_clicks"),
        Input("similar-right-arrow", "n_clicks"),
    ],
    [
        State("similar-store-left-clicks", "data"),
        State("similar-store-right-clicks", "data"),
    ],
)

clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks > 0) {
            const scrollButton = document.getElementById('scroll-button');
            const target = document.getElementById(scrollButton.innerText.includes('Similar Movies') ? 'similar-movies-section' : 'top');
            target.scrollIntoView({ behavior: 'smooth' });
            scrollButton.innerText = scrollButton.innerText.includes('Similar Movies') ? 'Go to Poster' : 'Go to Similar Movies';
        }
    }
    """,
    Output("scroll-button", "n_clicks"),
    [Input("scroll-button", "n_clicks")]
)
