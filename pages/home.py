import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = html.Div(
    style={
        "backgroundColor": "black",
        "height": "100vh",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "backgroundImage": "url('/assets/pr.jpg')",
        "backgroundSize": "cover",  # Ensure full coverage of background image
        "backgroundRepeat": "no-repeat",  # Ensure the image is not repeated
        "backgroundPosition": "center",  # Center the background image
    },
    children=[
        dbc.Container(
            [
                dbc.Row(
                    dbc.Col(
                        html.H1(
                            "Welcome To CineMate",
                            style={
                                "fontSize": "64px",
                                "textAlign": "center",
                                "marginBottom": "150px",  # Increased bottom margin to move text down
                                "textTransform": "uppercase",
                                "color": "white",
                                "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",  # Neon effect
                                "fontFamily": "Arial, sans-serif",  # Changed font family for better styling
                            }
                        ),
                        width=12,
                    )
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Button(
                                    html.Img(
                                        src="/assets/u1.gif",
                                        style={
                                            "width": "300px",
                                            "height": "300px",
                                            "borderRadius": "50%",
                                            "boxShadow": "0 0 40px #bb00ff",
                                        },
                                    ),
                                    href="/user",
                                    style={
                                        "border": "none",
                                        "backgroundColor": "transparent",
                                    },
                                ),
                                html.H2(
                                    "User",
                                    style={
                                        "color": "white",
                                        "fontSize": "36px",  # Increased font size
                                        "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",  # Neon effect
                                        "fontFamily": "Arial, sans-serif",  # Changed font family for better styling
                                    },
                                ),
                            ],
                            width=6,
                        ),
                        dbc.Col(
                            [
                                dbc.Button(
                                    html.Img(
                                        src="/assets/movie.gif",
                                        style={
                                            "width": "300px",
                                            "height": "300px",
                                            "borderRadius": "50%",
                                            "boxShadow": "0 0 40px #bb00ff",
                                        },
                                    ),
                                    href="/movie",
                                    style={
                                        "border": "none",
                                        "backgroundColor": "transparent",
                                    },
                                ),
                                html.H2(
                                    "Movie",
                                    style={
                                        "color": "white",
                                        "fontSize": "36px",  # Increased font size
                                        "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff",  # Neon effect
                                        "fontFamily": "Arial, sans-serif",  # Changed font family for better styling
                                    },
                                ),
                            ],
                            width=6,
                        ),
                    ],
                    style={"textAlign": "center"},
                ),
            ],
        )
    ],
)
