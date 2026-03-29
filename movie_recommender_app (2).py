
import streamlit as st
import pickle

mv = pickle.load(open('movies.pkl','rb'))
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=3000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)


def recommend(movie):
    movie = movie.lower()

    if movie not in mv['title'].str.lower().values:
        return ["Movie not found"]

    index = mv[mv['title'].str.lower() == movie].index[0]
    distances = similarity[index]

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
