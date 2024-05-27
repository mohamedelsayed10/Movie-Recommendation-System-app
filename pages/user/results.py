import pandas as pd
import dash
from dash import html, dcc, clientside_callback, Input, Output, State
import dash_bootstrap_components as dbc
from tensorflow.keras.models import load_model
from utils.predict_top_n import predict_top_n_with_loaded_model


dash.register_page(__name__, path="/user/results")

loaded_model = load_model("neural_collaborative_filtering_model.h5")

df_covers = pd.read_csv("ml-latest-small/movie_details.csv")
df_movies = pd.read_csv("./ml-latest-small/movies.csv")
df_ratings = pd.read_csv("ml-latest-small/ratings.csv")
df_tags = pd.read_csv("ml-latest-small/tags.csv")
df_links = pd.read_csv("ml-latest-small/links.csv")

df_merged = pd.merge(df_ratings, df_tags, on=["userId", "movieId"], how="outer")

df_merged["timestamp_x"] = df_merged["timestamp_x"].fillna(df_merged["timestamp_y"])
df_merged["timestamp_y"] = df_merged["timestamp_y"].fillna(df_merged["timestamp_x"])
df_merged = pd.merge(df_merged, df_links, on="movieId", how="outer")
df_merged = df_merged.drop(columns=["timestamp_y"])
df_merged = df_merged.rename(columns={"timestamp_x": "timestamp"})


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
            "alignItems": "center"
        },
    )


def layout(user_id, **other_unknown_query_strings):
    sorted_movies_ids = df_merged[df_merged["userId"] == int(user_id)].sort_values(
        "timestamp"
    )["imdbId"]
    recent_movie_posters = df_covers[df_covers["MovieID"].isin(sorted_movies_ids)][
        "CoverURL"
    ]

    recommended_movies_ids = predict_top_n_with_loaded_model(
        loaded_model=loaded_model,
        ratings=df_ratings,
        movies=df_movies,
        user_id=int(user_id),
        n=20,
    )

    imdb_ids = df_links[df_links["movieId"].isin(recommended_movies_ids)]["imdbId"]
    recommended_movies_posters = df_covers[df_covers["MovieID"].isin(imdb_ids)][
        "CoverURL"
    ]

    return html.Div(
        [
            dbc.Row(
                [
                    html.H2(
                        "Recently Watched",
                        style={"color": "white", "textAlign": "center", "marginTop": "200px", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff", "fontSize": "38px"},
                    ),
                    pagination_component(recent_movie_posters, "recent"),
                ],
                id="recently-watched",
                style={"textAlign": "center"},  # Center text and add margin to separate sections
            ),
            dbc.Row(
                dbc.Button(
                    html.Img(src="/assets/BP.png", style={"width": "50px"}),
                    href="/user",
                    style={
                        "backgroundColor": "transparent",
                        "border": "none",
                        "textAlign": "left",
                        "width": "fit-content",
                    },
                ),
                style={"marginBlock": "80px", "paddingInline": "60px"},
            ),
            dbc.Row(
                [
                    html.H2(
                        "Recommended Movies",
                        # className="neon-effect",
                        style={"color": "inherit", "textAlign": "center", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff", "fontSize": "38px"},
                    ),
                    pagination_component(recommended_movies_posters, "recommended"),
                ],
                id="recommended-movies",
                style={"textAlign": "center","marginBottom": "200px"},  # Center text and add margin to separate sections
            ),
            html.Button(
                "Go to Recommended Movies",
                id="scroll-button-user",
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
                    "padding": "10px 20px",
                    "cursor": "pointer",
                    "zIndex": 2,  # Ensure button is above background image
                },
            ),
        ],
        style={
            "backgroundImage": "url('/assets/pr.jpg')",
            "minHeight": "100vh",
            "width": "100vw",
            "overflowX": "hidden",
            "backgroundSize": "cover",
            "backgroundRepeat": "no-repeat",
            "backgroundAttachment": "fixed",  # Make background image cover full screen
            "backgroundPosition": "center",
            "zIndex": 1,
            "position": "relative",  # Ensure content stays above the background image
            "color": "white",
        },
        
    )

# JavaScript for handling the scroll
clientside_callback(
    """
    function(n_clicks_left, n_clicks_right, prev_left, prev_right) {
        var container = document.getElementById('recent-image-container');
        var scrollAmount = container.clientWidth - 100;
        if (n_clicks_left > prev_left) {
            container.scrollLeft -= scrollAmount;
        }
        if (n_clicks_right > prev_right) {
            container.scrollLeft += scrollAmount;
        }
        return [n_clicks_left, n_clicks_right];
    }
    """,
    [
        Output("recent-store-left-clicks", "data"),
        Output("recent-store-right-clicks", "data"),
    ],
    [Input("recent-left-arrow", "n_clicks"), Input("recent-right-arrow", "n_clicks")],
    [
        State("recent-store-left-clicks", "data"),
        State("recent-store-right-clicks", "data"),
    ],
)

clientside_callback(
    """
    function(n_clicks_left, n_clicks_right, prev_left, prev_right) {
        var container = document.getElementById('recommended-image-container');
        var scrollAmount = container.clientWidth - 100;
        if (n_clicks_left > prev_left) {
            container.scrollLeft -= scrollAmount;
        }
        if (n_clicks_right > prev_right) {
            container.scrollLeft += scrollAmount;
        }
        return [n_clicks_left, n_clicks_right];
    }
    """,
    [
        Output("recommended-store-left-clicks", "data"),
        Output("recommended-store-right-clicks", "data"),
    ],
    [
        Input("recommended-left-arrow", "n_clicks"),
        Input("recommended-right-arrow", "n_clicks"),
    ],
    [
        State("recommended-store-left-clicks", "data"),
        State("recommended-store-right-clicks", "data"),
    ],
)


clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks > 0) {
            const scrollButton = document.getElementById('scroll-button-user');
            const target = document.getElementById(scrollButton.innerText.includes('Recommended Movies') ? 'recommended-movies' : 'recently-watched');
            target.scrollIntoView({ behavior: 'smooth' });
            scrollButton.innerText = scrollButton.innerText.includes('Recommended Movies') ? 'Go to Recently Watched' : 'Go to Recommended Movies';
        }
    }
    """,
    Output("scroll-button-user", "n_clicks"),
    [Input("scroll-button-user", "n_clicks")]
)