
# 📊 Reddit Sentiment Analysis Report

## 📌 Project Overview

This project aims to perform **sentiment analysis on Reddit posts related to "Artificial Intelligence"** using NLP techniques. It uses Reddit’s API to scrape data, analyzes the sentiment using TextBlob, and visualizes the insights through Streamlit.

---

## 📥 Data Collection

- **Source**: Reddit (via `praw` API wrapper)
- **Query used**: `"Artificial Intelligence"`
- **Timeframe**: Custom search based on live queries
- **Limit**: Default 50 posts (user-controlled in Streamlit)

---

## 🔍 Preprocessing & Sentiment Analysis

- Titles and texts of Reddit posts were extracted.
- Sentiment was analyzed using **TextBlob**, which calculates the **polarity score** of the text.
- Classification based on polarity:
  - `> 0` → Positive 
  - `= 0` → Neutral 
  - `< 0` → Negative 

---

## 📈 Visualization Summary

The sentiment analysis was visualized using:

1. **Bar Chart**: Displays the count of positive, neutral, and negative posts.
2. **Pie Chart**: Proportional distribution of sentiments.
3. **Word Cloud**: Shows frequent keywords in posts related to AI.

---

## 📌 Custom Query Support

The web application supports a **Custom Search** feature via the Streamlit interface, allowing users to:

- Enter any Reddit query dynamically
- Set number of posts to fetch (10–500)
- Instantly view analyzed sentiment on newly fetched data

---

## 🗂️ Project Structure

```
reddit_sentiment_analysis/
├── app.py
├── README.md (or REPORT.md)
├── src/
│   ├── config.py
│   ├── reddit_scraper.py
│   ├── sentiment_analysis.py
│   └── data/
│       ├── output.csv
│       └── output_sentiment.csv
├── model/
│   └── sentiment.py
└── notebooks/
    └── visualizations/
        ├── sentiment_bar_chart.png
        ├── sentiment_pie_chart.png
        └── sentiment_wordcloud.png
```

---

## ✅ Technologies Used

- Python
- Streamlit (GUI)
- TextBlob (Sentiment analysis)
- PRAW (Reddit API)
- Matplotlib & WordCloud (Visualizations)
- Pandas (Data handling)

---

