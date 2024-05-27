import numpy as np
import dash
from dash import html, Input, Output, callback, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/user")

users = np.arange(1, 611)

user_dropdown = dcc.Dropdown(
    id="user-dropdown",
    options=[{"label": f"User {user}", "value": user} for user in users],
    placeholder="Select User",
    value=1,
    style={"width": "200px", "height": "fit-content", "color": "black"},
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
            dbc.Row(
                [
                    dbc.Col(
            html.Img(src="/assets/u_page.gif", style={"maxWidth": "100%", "height": "auto"}),
            width=5,
            style={"display": "flex", "alignItems": "center", "justifyContent": "right"}
        ),
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H3("Select User", style={"color": "white", "textShadow": "0 0 20px #bb00ff, 0 0 30px #bb00ff, 0 0 40px #bb00ff", "fontSize": "24px"}),
                                user_dropdown,
                                dbc.Button(
                                    "Submit",
                                    href="",
                                    id="user-submit-button",
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
                ]
            ),
            align="center",
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

@callback(Output("user-submit-button", "href"), Input("user-dropdown", "value"))
def update_href(user):
    return f"/user/results?user_id={user}"
