# app.py (Put in root folder)
import streamlit as st
import pandas as pd
import os
from src.config import reddit
from src.sentiment_analysis import analyze_sentiment
from src.reddit_scraper import scrape_reddit 
from model.sentiment import get_sentiment

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("src/data/output_sentiment.csv")
    return df

st.set_page_config(page_title="Reddit Sentiment Analysis", layout="wide")
st.title("📊 Reddit Sentiment Analysis ")

# Sidebar
st.sidebar.header("Navigation")
options = st.sidebar.radio("Go to", ["📄 Dataset Preview", "📈 Visualizations", "☁️ Word Cloud","🔍 Custom Search"])

df = load_data()

# Dataset View
if options == "📄 Dataset Preview":
    st.subheader("Top 100 Records with Sentiment on Artificial Intelligence")
    st.dataframe(df[['title', 'text', 'Sentiment']].head(100))

# Visualization View
elif options == "📈 Visualizations":
    st.subheader("Sentiment Distribution")
    st.image("notebooks/visualizations/sentiment_bar_chart.png", caption="Bar Chart")

    st.subheader("Sentiment Pie Chart")
    st.image("notebooks/visualizations/sentiment_pie_chart.png", caption="Pie Chart")

# Word Cloud View
elif options == "☁️ Word Cloud":
    st.subheader("Sentiment Word Cloud")
    st.image("notebooks/visualizations/sentiment_wordcloud.png", caption="Word Cloud")


# 4. User Input: Custom Query
elif options == "🔍 Custom Search":
    st.subheader("Search Reddit by Query")

    with st.form("reddit_form"):
        query = st.text_input("Enter your Reddit search query:", placeholder="e.g., Artificial Intelligence in education")
        limit = st.number_input("Number of posts to fetch", min_value=10, max_value=500, value=50, step=10)
        submitted = st.form_submit_button("Scrape and Analyze")

    if submitted and query:
        with st.spinner("Scraping and analyzing Reddit posts..."):
            # Scrape data
            output_csv = "src/data/output.csv"
            scrape_reddit(query, limit, output_csv)

            # Analyze sentiment
            analyze_sentiment(df, output_path="src/data/output_sentiment.csv")
           
            # Reload data
            df = load_data()

            st.success(f"✅ Fetched and analyzed {limit} posts!")
            st.dataframe(df[['title', 'text', 'Sentiment']].head(100))

            
          
