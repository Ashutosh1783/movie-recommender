
import streamlit as st
import pickle

mv = pickle.load(open('movies.pkl','rb'))


def recommend(movie):
    movie = movie.lower()

    if movie not in mv['title'].str.lower().values:
        return ["Movie not found"]

    index = mv[mv['title'].str.lower() == movie].index[0]
    distances = sim[index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x:x[1])[1:6]

    return [mv.iloc[i[0]].title for i in movies_list]

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Select a movie", mv['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)
