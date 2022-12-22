import streamlit as st
import pickle
import pandas as pd
import requests

def fetchPoster(id, data):
    path = 'http://image.tmdb.org/t/p/w500/' + data['poster_path']
    return path


def recommend(movie):
    movieIndex = movies[movies['title'] == movie].index[0]
    distances = similarity[movieIndex]
    moviesList = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:30]
    
    recommended = []
    posters = []
    for i in moviesList:
        data = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9318cfc1fd2c5e2c6c0b4ad6c0bd0c4'.format(movies.iloc[i[0]].movie_id)).json()
        if 'poster_path' in data and data['poster_path']:
            recommended.append((movies.iloc[i[0]].title))
            posters.append(fetchPoster(movies.iloc[i[0]].movie_id, data))
        else:
            continue
    return recommended, posters

moviesDict = pickle.load(open('models/movies_dict.pkl','rb'))
similarity = pickle.load(open('models/similarity.pkl','rb'))
movies = pd.DataFrame(moviesDict)

st.set_page_config(layout="wide")
st.title('Movie Recommender')
st.header(' ')

selectedMovie = st.selectbox("Enter a movie", movies['title'].values)
if st.button('Recommend'):
    names, posters = recommend(selectedMovie)

    st.header(' ')
    st.subheader('20 results')
    st.subheader(' ')
    count = 0
    for i in range(0, 4):
        cols = st.columns(5)
        cols[0].text(names[count])
        cols[0].image(posters[count])
        count += 1
        
        cols[1].text(names[count])
        cols[1].image(posters[count])
        count += 1

        cols[2].text(names[count])
        cols[2].image(posters[count])
        count += 1

        cols[3].text(names[count])
        cols[3].image(posters[count])
        count += 1

        cols[4].text(names[count])
        cols[4].image(posters[count])
        count += 1
        st.header(' ')
