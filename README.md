# Customer-ExperienceAnalytics-for-Fintech-Apps


### Overview

This project provides scripts and notebooks to scrape, preprocess, and analyze customer reviews from fintech apps (e.g., Google Play Store). It includes sentiment analysis, thematic analysis, and text classification.

### Directory Structure

- `notebooks/`: Jupyter notebooks for data exploration, scraping, and analysis.
- `scripts/`: Python scripts for scraping, preprocessing, and analysis.
- `src/data/`: Contains raw review data (e.g., `raw_review.csv`).

### Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Run Notebooks:**
   Open any notebook in the `notebooks/` directory with Jupyter and execute the cells.

3. **Run Scripts:**
   Example:
   ```sh
   python scripts/scrap.py
   ```

### Main Features

- Scrape reviews from Google Play Store using `google_play_scraper`.
- Preprocess and clean review data.
- Perform sentiment and thematic analysis.
- Classify text and extract top keywords.

---

