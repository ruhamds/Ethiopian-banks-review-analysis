# 🇪🇹 Ethiopian Banks Reviews Analysis

This repository contains code for **scraping**, **cleaning**, and **analyzing** Google Play Store reviews for three major Ethiopian banks:

- 🏦 **Commercial Bank of Ethiopia (CBE)**
- 🏦 **Bank of Abyssinia (BOA)**
- 🏦 **Dashen Bank**

---

## ✅ Task 1: Data Collection and Preprocessing

### 📌 Methodology

1. **Project Setup**
   - Initialized GitHub repository with `.gitignore` and `requirements.txt`.
   - Created and worked on the `task-1` branch with meaningful commits.
   - Installed required libraries: `google-play-scraper`, `pandas`, etc.

2. **Web Scraping**
   - Scraped **400+ reviews per bank** using `google-play-scraper`.
   - Used multiple sorting strategies (Most Relevant, Newest, Rating).
   - Collected fields:
     - Review Text
     - Rating (1–5)
     - Date (normalized to `YYYY-MM-DD`)
     - Bank/App Name
     - Source (Google Play)
   - Saved raw output to `raw_reviews.csv`.

3. **Preprocessing**
   - Removed duplicates based on `review_id`.
   - Dropped rows with missing reviews or ratings.
   - Cleaned review text and normalized fields.
   - Ensured rating values are valid integers.
   - Final cleaned dataset saved to `cleaned_reviews.csv`.

---

## ✅ Task 2: Sentiment and Thematic Analysis

### 📌 Methodology

#### 🧠 Sentiment Analysis
- Used `VADER` (via `vaderSentiment` library) in `sentiment_analysis.ipynb`.
- Classified reviews into: **Positive**, **Negative**, **Neutral**.
- Calculated sentiment scores per review.
- Aggregated sentiment by **bank** and **rating**.
- Output saved as:
  - `reviews_with_sentiment.csv`
  - `sentiment_summary.csv`

#### 💬 Thematic Analysis
- Used `spaCy` and `TF-IDF` in `thematic_analysis.ipynb`.
- Preprocessed text (tokenization, stopword removal, etc.).
- Extracted top **keywords and bi-grams**.
- Manually clustered into 3–5 themes per bank:
  - e.g., *Account Access Issues*, *Transaction Performance*, *User Interface*
- Output saved as:
  - `reviews_with_themes.csv`
  - `keyword_summary.txt`

---

## 📁 Output Files

| File                         | Description                                  |
|-----------------------------|----------------------------------------------|
| `raw_reviews.csv`           | Raw scraped review data                      |
| `cleaned_reviews.csv`       | Cleaned and preprocessed reviews             |
| `reviews_with_sentiment.csv`| Reviews with sentiment labels and scores     |
| `sentiment_summary.csv`     | Aggregated sentiment breakdown               |
| `reviews_with_themes.csv`   | Reviews annotated with themes                |
| `keyword_summary.txt`       | Top extracted keywords per bank              |

---

## 💻 Project Files

| File Name                   | Purpose                                      |
|----------------------------|----------------------------------------------|
| `scrape_reviews.ipynb`     | Scraping reviews (Task 1)                    |
| `preprocess_reviews.ipynb` | Cleaning and preprocessing (Task 1)          |
| `sentiment_analysis.ipynb` | VADER-based sentiment analysis (Task 2)      |
| `thematic_analysis.ipynb`  | Keyword extraction and thematic grouping     |
| `requirements.txt`         | Python dependencies                         |

> 🗂️ **Note:** CSV data files are not committed to GitHub to avoid size/clutter.

---

## 🛠️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/ruhamds/Ethiopian-banks-review-analysis.git
cd Ethiopian-banks-review-analysis

# 2. Set up virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 4. Launch Jupyter Notebook
jupyter notebook
```

---

## 📬 Contact

- 📧 Email: [ruheezrael@gmail.com](mailto:ruheezrael@gmail.com)  
- 📦 GitHub: [github.com/ruhamds/Ethiopian-banks-review-analysis](https://github.com/ruhamds/Ethiopian-banks-review-analysis)
