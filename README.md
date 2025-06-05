# Ethiopian Banks Reviews Analysis

This repository contains code for scraping and preprocessing Google Play Store reviews for three Ethiopian banks: Commercial Bank of Ethiopia, Bank of Abyssinia, and Dashen Bank.

## Task 1: Data Collection and Preprocessing

### Methodology
1. **Setup**:
   - Created a GitHub repository with `.gitignore` and `requirements.txt`.
   - Installed Python libraries: `google-play-scraper` and `pandas`.
   - Worked on the `task-1` branch with frequent commits.

2. **Web Scraping**:
   - Used `google-play-scraper` to scrape reviews for each bank’s app.
   - Targeted 400+ reviews per bank using multiple sort options (Most Relevant, Newest, Rating).
   - Collected: review text, rating, date, bank name, and source (Google Play).
   - Saved raw data to `raw_reviews.csv`.

3. **Preprocessing**:
   - Removed duplicates based on `review_id`.
   - Dropped rows with missing `review` or `rating`.
   - Normalized dates to `YYYY-MM-DD`.
   - Ensured ratings are integers between 1 and 5.
   - Cleaned review text by removing extra whitespace.
   - Saved cleaned data to `cleaned_reviews.csv`.

### Files
- `scrape_reviews.ipynb`: Scrapes reviews from Google Play Store.
- `preprocess_reviews.ipynb`: Cleans and preprocesses the scraped data.
- `raw_reviews.csv`: Raw scraped data (not committed due to `.gitignore`).
- `cleaned_reviews.csv`: Cleaned data (not committed due to `.gitignore`).
- `requirements.txt`: Lists required Python libraries.

### How to Run
1. Clone the repository: `git clone https://github.com/ruhamds/Ethiopian-banks-review-analysis.git
2. Install dependencies: `pip install -r requirements.txt`
3. Run scraping: `python scrape_reviews.py`
4. Run preprocessing: `python preprocess_reviews.py`

### Next Steps
