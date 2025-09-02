import pandas as pd

def load_data(path='data/ratings.csv'):
    df = pd.read_csv(path)
    return df
def create_user_item_matrix(df):
    return df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(matrix, kind='user'):
    if kind == 'user':
        similarity = cosine_similarity(matrix)
    else:
        similarity = cosine_similarity(matrix.T)
    return pd.DataFrame(similarity, index=matrix.index if kind=='user' else matrix.columns,
                        columns=matrix.index if kind=='user' else matrix.columns)
def recommend_user_based(user_id, matrix, similarity_df, top_n=5):
    if user_id not in similarity_df.columns:
        return "User ID not found in similarity matrix."

    # Get similarity scores for the user
    similar_users = similarity_df[user_id].drop(user_id)  # exclude self

    # Align similar_users with matrix columns
    similar_users = similar_users[matrix.index.intersection(similar_users.index)]

    # Compute weighted ratings
    weighted_ratings = matrix.loc[similar_users.index].T.dot(similar_users)
    weighted_ratings = weighted_ratings / similar_users.sum()

    # Filter out movies already rated
    user_rated = matrix.loc[user_id][matrix.loc[user_id] > 0].index
    recommendations = weighted_ratings.drop(user_rated).sort_values(ascending=False).head(top_n)

    return recommendations
def recommend_item_based(user_id, matrix, similarity_df, top_n=5):
    user_ratings = matrix.loc[user_id]
    scores = similarity_df.dot(user_ratings)
    scores = scores / similarity_df.sum(axis=1)
    user_rated = user_ratings[user_ratings > 0].index
    recommendations = scores.drop(user_rated).sort_values(ascending=False).head(top_n)
    return recommendations
# --- All your function definitions above ---
# load_data(), create_user_item_matrix(), compute_similarity(), recommend_user_based(), etc.

if __name__ == "__main__":
    df = load_data()
    matrix = create_user_item_matrix(df)
    similarity = compute_similarity(matrix, kind='user')
    print(recommend_user_based(11, matrix, similarity))
