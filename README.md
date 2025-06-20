### Customer Experience Analytics for Fintech Apps

### Overview

This project provides scripts and notebooks to scrape, preprocess, and analyze customer reviews from fintech apps (e.g., Google Play Store). It includes sentiment analysis, thematic analysis, and text classification.

### Directory Structure

- `notebooks/`: Jupyter notebooks for data exploration, scraping, and analysis.
- `scripts/`: Python scripts for scraping, preprocessing, and analysis.
- `src/data/`: Contains raw and processed review data (e.g., `raw_review.csv`, `Analysed_review.csv`).
- `tests/`: Unit tests for scripts and modules.

### Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Customer-ExperienceAnalytics-for-Fintech-Apps.git
   cd Customer-ExperienceAnalytics-for-Fintech-Apps'
2. Install dependencies:
   pip install -r requirements.txt

3. Database Setup (Optional):

Ensure PostgreSQL is running.
Use the provided SQL dump or the notebook notebooks/test_oracl.ipynb to create and populate the database.
Usage
Run Notebooks
Open any notebook in the notebooks/ directory with Jupyter and execute the cells. Example notebooks:

sentiment-and-thematic-analysis.ipynb: Sentiment and theme extraction.
web-scrap.ipynb: Scraping reviews from Google Play Store.
test_oracl.ipynb: Example of loading and querying reviews in PostgreSQL.
Run Scripts
Example:
python [scrap.py](http://_vscodecontentref_/0)
python [preprocess.py](http://_vscodecontentref_/1)

### Main Features
Scrape reviews from Google Play Store using google_play_scraper.
Preprocess and clean review data.
Perform sentiment and thematic analysis.
Classify text and extract top keywords.
Store and query reviews in a PostgreSQL database.
Example: Querying Reviews by Bank'
import psycopg2

conn = psycopg2.connect(user="postgres", password="your_password", host="localhost", port="5432", dbname="bank_reviews")
cur = conn.cursor()
cur.execute("SELECT bank, COUNT(*) FROM reviews GROUP BY bank")
print(cur.fetchall())
cur.close()
conn.close()
