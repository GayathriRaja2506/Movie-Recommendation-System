# 🎬 Movie Recommendation System

A Netflix-style movie recommender built using collaborative filtering. This project demonstrates how platforms can personalize content to boost user engagement.

---

## 🚀 Objective

Recommend movies to users based on their preferences using **user-based** or **item-based collaborative filtering**.

---

## 📦 Features

- User-item matrix generation
- Cosine similarity-based filtering
- User-based and item-based recommendation logic
- Optional Streamlit UI for interactive suggestions

---

## 📁 Project Structure

```
movie_recommender/
│
├── data/
│   └── ratings.csv              # Synthetic or real user ratings
│
├── recommender.py               # Core recommendation logic
├── app.py                       # Streamlit UI (optional)
├── README.md                    # Project documentation
└── requirements.txt             # Dependencies
```

---

## 📊 Dataset

Uses a simplified version of the [MovieLens dataset](https://www.kaggle.com/datasets/sherinclaudia/movielens) or synthetic data with the format:

```
userId,movieId,rating
1,101,4.0
1,102,3.5
2,101,5.0
...
```

You can generate synthetic data using:

```python
import pandas as pd, random

df = pd.DataFrame({
    "userId": [random.randint(1, 20) for _ in range(100)],
    "movieId": [random.randint(101, 130) for _ in range(100)],
    "rating": [round(random.uniform(1.0, 5.0), 1) for _ in range(100)]
})
df.drop_duplicates(subset=["userId", "movieId"]).to_csv("data/ratings.csv", index=False)
```

---

## 🧠 Recommendation Logic

### User-Based Collaborative Filtering
- Computes similarity between users using cosine similarity
- Predicts ratings based on similar users' preferences

### Item-Based Collaborative Filtering
- Computes similarity between movies
- Recommends items similar to those the user liked

---

## 🖥️ Streamlit App (Optional)

Launch the interactive UI:

```bash
streamlit run app.py
```

Enter a user ID to get personalized movie suggestions.

---

## 🛠️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/movie_recommender.git
   cd movie_recommender
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the recommender:
   ```bash
   python recommender.py
   ```

---

## 📌 Requirements

```txt
pandas
numpy
scikit-learn
streamlit
```
