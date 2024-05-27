

# Movie Recommendation System app


https://github.com/mohamedelsayed10/Movie-Recommendation-System-app/assets/87568101/94afba34-955c-4a6c-9b40-0a973cf4ee7e


## Overview

This project aims to create an interactive movie recommendation system app using the MovieLens dataset (ml-latest-small) and potentially integrating another dataset for additional context and challenges. The dashboard leverages advanced recommender models like Neural Collaborative Filtering to provide personalized movie recommendations and Item Similarity:Computes similarities dynamically when a movie is selected on the Item Page.

## Recommender Models

### User Recommender

- **Advanced Model:** Utilizes Neural Collaborative Filtering (NCF) for personalized movie recommendations.
- **Inference Model:** Trained and saved for efficient real-time predictions.
- **Integration:** Integrated into the dashboard to provide recommendations based on the selected user.

### Item Similarity

- **Methodology:** Employs appropriate techniques to calculate similarities between movies.
- **On-Demand Calculation:** Computes similarities dynamically when a movie is selected on the Item Page.


## Technology Stack
- Dashboard Framework: Built using Dash for creating interactive web applications.

- Recommendation Model: Developed using TensorFlow, implementing Neural Collaborative Filtering (NCF) for personalized movie recommendations.

- Item-Item Similarity: Calculated using scikit-learn, employing methods such as cosine similarity for measuring item similarity dynamically.



## User Interface Components

### User Page

- **User Selection:** Allows users to choose from a list of unique users in the dataset.
- **User History View:** Displays the user's interaction history with detailed item information.
- **Parameter Input (N):** Enables users to specify the number of recommended items per page.
- **Top-N Recommendations:** Shows a list of top-N recommended movies for the selected user.
- **Navigation:** Allows users to navigate through recommendation lists (next/previous/page navigation).

### Item Page

- **Item Selection:** Allows users to select from a list of unique items in the dataset.
- **Item Profile:** Displays metadata and details about the selected movie.
- **Top-N Similar Items:** Lists movies that are most similar to the selected item.
- **Navigation:** Allows users to navigate through lists of similar items (next/previous/page navigation).



## Dataset

- **MovieLens (small):** Includes 100,836 ratings across 9,742 movies by 610 users.
- **Additional Dataset:** Considering integration of another dataset with additional challenges and contextual information to enhance recommendation insights. Details pending confirmation.



