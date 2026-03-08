# 🎬 Movie Recommender System

A content-based movie recommender system built using **Python, Pandas, and Scikit-Learn**.
The system suggests movies similar to the one selected by the user using **cosine similarity on movie features**.

---

## 🚀 Features

* Recommends movies similar to a selected movie
* Uses **content-based filtering**
* Built with **Python and machine learning libraries**
* Precomputed similarity matrix for fast recommendations

---

## 🧠 How It Works

1. Movie metadata is processed and important features are extracted.
2. Features such as **genres, keywords, cast, and crew** are combined.
3. Text data is converted into vectors using **CountVectorizer**.
4. **Cosine similarity** is calculated between movie vectors.
5. The system recommends the **top similar movies**.

---

## 📂 Project Structure

```
movie-recommender-system
│
├── app.py
├── model.ipynb
├── movies.pkl
├── similarity.pkl.gz
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/vishal598/movie-recommender-system.git
cd movie-recommender-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start the application:

```bash
python app.py
```

---

## 📦 Model Files

The similarity matrix is stored in a **compressed format** to reduce file size:

```
similarity.pkl.gz
```

To load it in Python:

```python
import gzip
import pickle

with gzip.open("similarity.pkl.gz", "rb") as f:
    similarity = pickle.load(f)
```

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Pickle

---

## 📊 Dataset

The dataset contains movie metadata including:

* Title
* Genres
* Keywords
* Cast
* Crew

These features are used to compute similarity between movies.

---

## 📌 Future Improvements

* Add **Streamlit UI**
* Use **TMDB API for posters**
* Implement **collaborative filtering**
* Deploy the project online

---

## 👨‍💻 Author

**Vishal Bagga**
