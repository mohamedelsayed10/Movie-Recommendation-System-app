import pandas as pd

def get_movie_details(movie_id, movies, ratings, links, movie_details):
    total_movie_details = pd.merge(movies, ratings, on="movieId", how="outer")
    total_movie_details = pd.merge(total_movie_details, links, on="movieId", how="outer")
    total_movie_details = pd.merge(total_movie_details, movie_details, left_on="imdbId", right_on="MovieID", how="outer")

    movie =  total_movie_details[total_movie_details["movieId"] == movie_id]
    # average rating
    avg_rating = movie["rating"].mean()
    # number of ratings
    num_ratings = movie["rating"].count()

    directors = movie["Directors"].unique()
    actors = movie["Actors"].unique()
    writers = movie["Writers"].unique()

    genres = movie["genres"].unique()

    return {
        "avg_rating": avg_rating,
        "num_ratings": num_ratings,
        "directors": directors,
        "actors": actors,
        "writers": writers,
        "genres": genres
    }