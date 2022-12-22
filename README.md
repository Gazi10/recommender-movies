# Movie Recommender System
This project is a movie recommender system that suggests similar movies to a user-selected movie using machine learning techniques. It was developed using Python, Numpy, Pandas, and Streamlit.

## How it works
The recommender system uses a content-based filtering approach, which means that it recommends movies based on their characteristics and features. In this case, the system uses the TMDB 5000 Movie Dataset, which includes information about various movies, such as their title, overview, and genres.

To recommend similar movies, the system first vectorizes the data using a bag-of-words model. This converts the movie data into numerical vectors, which can then be compared using cosine similarity. The system calculates the similarity between each vector (movie) and the user-selected movie, and then recommends the movies with the highest similarity scores.

## Features
* Suggests similar movies to a user-selected movie
* Uses a bag-of-words model to vectorize the movie data
* Evaluates the similarity between each vector (movie) using cosine similarity
* Developed as a web app using Streamlit and deployed to Heroku (recommender-movies.herokuapp.com)
* Displays posters of the recommended movies
## Installation
To run the movie recommender system on your local machine, follow these steps:

* Clone the repository:
`git clone https://github.com/Gazi10/recommender-movies.git`
* Install the required packages:
`pip install numpy pandas streamlit`

## Run the Streamlit app:
`streamlit run app.py`
