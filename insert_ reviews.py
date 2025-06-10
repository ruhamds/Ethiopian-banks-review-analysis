import cx_Oracle
import pandas as pd
from datetime import datetime, timedelta
import random

# Simulated review data (since actual cleaned data isn't provided)
def generate_sample_reviews(num_reviews=1000):
    banks = ['Commercial Bank of Ethiopia']
    sentiments = ['Positive', 'Negative', 'Neutral']
    sample_reviews = []
    for i in range(num_reviews):
        review = {
            'bank_name': banks[0],
            'review_text': f"Review {i+1}: This is a sample review for CBE. Service was {'great' if random.choice(sentiments) == 'Positive' else 'poor' if random.choice(sentiments) == 'Negative' else 'average'}.",
            'sentiment': random.choice(sentiments),
            'review_date': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
        }
        sample_reviews.append(review)
    return pd.DataFrame(sample_reviews)

# Database connection parameters
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
connection = cx_Oracle.connect(user="bank_reviews", password="password123", dsn=dsn)
cursor = connection.cursor()

# Get bank_id for Commercial Bank of Ethiopia
cursor.execute("SELECT bank_id FROM Banks WHERE bank_name = :1", ("Commercial Bank of Ethiopia",))
bank_id = cursor.fetchone()[0]

# Generate sample review data
reviews_df = generate_sample_reviews(1000)

# Insert reviews into Reviews table
insert_query = """
INSERT INTO Reviews (bank_id, review_text, sentiment, review_date)
VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'))
"""
for _, row in reviews_df.iterrows():
    cursor.execute(insert_query, (bank_id, row['review_text'], row['sentiment'], row['review_date']))

# Commit changes
connection.commit()

# Verify the number of inserted records
cursor.execute("SELECT COUNT(*) FROM Reviews")
count = cursor.fetchone()[0]
print(f"Inserted {count} reviews into the Reviews table.")

# Close connection
cursor.close()
connection.close()