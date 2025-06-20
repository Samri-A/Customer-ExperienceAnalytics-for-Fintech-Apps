# Customer-ExperienceAnalytics-for-Fintech-Apps

This repository contains two main projects:

- **Customer Experience Analytics for Fintech Apps**: A data analytics toolkit for extracting, preprocessing, and analyzing customer reviews from fintech applications.
- **MiniGit**: A minimal version control system implemented in C++ for educational purposes.

---

## 1. Customer Experience Analytics for Fintech Apps

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

## 2. MiniGit

### Overview

MiniGit is a simplified version control system written in C++. It supports basic git-like operations such as `init`, `add`, `commit`, `branch`, and `log`.

### Directory Structure

- `Minigit-project/`: Contains the MiniGit C++ source code (`minigit.cpp`) and its README.

### Building and Running

1. **Compile:**
   ```sh
   g++ -std=c++17 -o minigit Minigit-project/minigit.cpp
   ```

2. **Run:**
   ```sh
   ./minigit
   ```

### Features

- Initialize a repository
- Add files to staging area
- Commit changes
- View commit log
- Create branches

---

