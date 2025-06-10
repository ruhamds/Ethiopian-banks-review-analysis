Ethiopian Banks Reviews Analysis
Project Overview
This project analyzes Google Play Store reviews for three Ethiopian banks: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank (DB). The goal is to extract insights from ~1,200 reviews to identify user sentiment, themes, drivers, pain points, and recommend app improvements. The pipeline includes data collection, preprocessing, sentiment/thematic analysis, Oracle storage, and visualization.
Repository

GitHub: https://github.com/ruhamds/Ethiopian-banks-review-analysis
Branches: task-1, task-2, task-3, task-4, main

Setup Instructions

Clone Repository:git clone https://github.com/ruhamds/Ethiopian-banks-review-analysis.git


Create Virtual Environment:python -m venv venv
.\venv\Scripts\activate


Install Dependencies:pip install -r requirements.txt


Run Notebooks:
Open Jupyter: jupyter notebook
Execute notebooks in order: scrape_reviews.ipynb, preprocess_reviews.ipynb, sentiment_analysis.ipynb, thematic_analysis.ipynb, oracle_database_setup.ipynb, insights_visualizations.ipynb.



Tasks
Task 1: Data Collection and Preprocessing

Objective: Scrape ~400 reviews per bank, clean data.
Methodology: Used scrape_reviews.ipynb for Google Play scraping, preprocess_reviews.ipynb for cleaning (e.g., remove duplicates, handle missing data).
Outputs: cleaned_reviews.csv (~1,200 reviews).

Task 2: Sentiment and Thematic Analysis

Objective: Analyze sentiment and extract themes.
Methodology: Used sentiment_analysis.ipynb with VADER for sentiment scores/labels, thematic_analysis.ipynb with spaCy for themes (e.g., “Account Access Issues”). Fixed CBE-only issue via standardized bank names.
Outputs: reviews_with_sentiment.csv, sentiment_summary.csv, reviews_with_themes.csv, keyword_summary.txt.

Task 3: Store Data in Oracle

Objective: Store reviews in an Oracle xe database.
Methodology: Used oracle_database_setup.ipynb to create bank_reviews schema with Banks and Reviews tables, inserted ~1,200 reviews.
Outputs: Populated Oracle database.


Task 4: Insights and Recommendations

Objective: Derive insights, visualize results, recommend improvements.
Methodology: Used insights_visualizations.ipynb to create 4 visualizations (sentiment, ratings, themes, theme word cloud), identify drivers (e.g., UI), pain points (e.g., login issues), and suggest improvements. Used theme-based word cloud due to keyword mismatch issues.
Outputs: sentiment_distribution.png, rating_distribution.png, theme_frequency.png, theme_cloud_negative and positive.png.

Dependencies

Python 3.8+
Libraries: pandas, matplotlib, seaborn, wordcloud, cx_Oracle, spacy, vaderSentiment
Oracle database access

Notes

Ensure Oracle credentials are configured for Task 3.
Theme-based word cloud used in Task 4 due to keyword mismatch; verify with facilitators if acceptable.

### Insights
- **Scenario 1: Retaining Users**: Slow loading is a major issue for BOA (210 “Technical Issues”, -0.3 sentiment, 2.8 stars) and moderate for CBE (238 “Technical Issues”, 0.16 sentiment). DB’s positive “Transaction Performance” and high sentiment (0.46, 4.0 stars) support retention.
- **Scenario 2: Enhancing Features**:  “App Functionality” (1805 mentions) and “Mobile Banking Services” (606) emphasize transfers. DB leads in satisfaction.
- **Scenario 3: Managing Complaints**: Login errors dominate for CBE (~120 “Account Access Issues”, 238 “Technical Issues”) and BOA (210 “Technical Issues”). DB has minimal complaints.

#### Recommendations
1. **Optimize Transfer Speed**: BOA and CBE to upgrade backend for faster transfers, addressing “Technical Issues” (BOA: 210, CBE: 238).
2. **Deploy AI Chatbot**: BOA and CBE to handle login errors in “Account Access Issues” and “Technical Issues”.
3. **Enhance Transaction Features**: DB to add advanced transfer options to “App Functionality” (391).