import streamlit as st
from recommender import *

df = load_data()
matrix = create_user_item_matrix(df)
similarity = compute_similarity(matrix, kind='user')

st.title("🎬 Movie Recommendation System")
user_id = st.number_input("Enter User ID", min_value=1, max_value=int(df['userId'].max()))

if st.button("Get Recommendations"):
    recs = recommend_user_based(user_id, matrix, similarity)
    st.write("Recommended Movies:")
    st.write(recs)
