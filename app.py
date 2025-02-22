import pickle
import streamlit as st
import requests
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:

        recommended_movies.append(movies.iloc[i[0]].title)


    return recommended_movies

# movies_dict = pickle.load(open('C:/Users/ADMIN/PycharmProjects/Movie-recommender-System/movie_dict.pkl','rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

#similarity = pickle.load(open('C:/Users/ADMIN/PycharmProjects/Movie-recommender-System/similarity.pkl','rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_names = st.selectbox(
    "Type or select a movie from the dropdown",
movies["title"].values)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie_names)
    for i in recommendations:
        st.write(i)




