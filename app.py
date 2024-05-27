import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
        'https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap'  # Adding the custom font
    ],
    use_pages=True,
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"name": "description", "content": "CineMate - Your Movie Recommender System"},
    ]
)

app.title = "CineMate"

app.layout = html.Div(
    [
        html.Link(
            rel='stylesheet',
            href='/assets/custom.css'  # Link to your custom CSS file
        ),
        dcc.Loading(
            id="loading-icon",
            type="circle",
            color="#bb00ff",
            children=dash.page_container,
        ),
    ],
    style={"backgroundColor": "#000", "fontFamily": "'Bebas Neue', sans-serif"}  # Applying the custom font
)


if __name__ == "__main__":
    app.run(debug=False)
