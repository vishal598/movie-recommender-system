import streamlit as st
import pickle
import pandas as pd

# load movie dictionary
movies_dict = pickle.load(open('movie_dict.pkl','rb'))

# convert dictionary to dataframe
movies = pd.DataFrame(movies_dict)

# load similarity matrix
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x:x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


st.title("Movie Recommender System")

# dropdown list
movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

# button
if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)