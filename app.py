# app.py
import streamlit as st
import pandas as pd
import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

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
st.title("📊 Reddit Sentiment Analysis")

# Sidebar
st.sidebar.header("Navigation")
options = st.sidebar.radio("Go to", [
    "📄 Dataset Preview", 
    "📈 Visualizations", 
    "☁️ Word Cloud", 
    "🔍 Custom Search", 
    "📂 Upload CSV"
], key="nav_radio")

df = load_data()

# 1. Dataset View
if options == "📄 Dataset Preview":
    st.subheader("Top 100 Records with Sentiment on Artificial Intelligence")
    st.dataframe(df[['title', 'text', 'Sentiment']].head(100))

# 2. Visualization View
elif options == "📈 Visualizations":
    st.subheader("Sentiment Distribution")
    st.image("notebooks/visualizations/sentiment_bar_chart.png", caption="Bar Chart")

    st.subheader("Sentiment Pie Chart")
    st.image("notebooks/visualizations/sentiment_pie_chart.png", caption="Pie Chart")

# 3. Word Cloud View
elif options == "☁️ Word Cloud":
    st.subheader("Sentiment Word Cloud")
    st.image("notebooks/visualizations/sentiment_wordcloud.png", caption="Word Cloud")

# 4. Custom Search
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
            analyze_sentiment(pd.read_csv(output_csv), output_path="src/data/output_sentiment.csv")

            # Reload data
            df = load_data()

            st.success(f"✅ Fetched and analyzed {limit} posts!")
            st.dataframe(df[['title', 'text', 'Sentiment']].head(100))

# 5. Upload CSV for Sentiment Analysis
elif options == "📂 Upload CSV":
    st.subheader("Upload Your CSV for Sentiment Analysis")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        user_df = pd.read_csv(uploaded_file)

        # Check for text column
        if 'text' not in user_df.columns:
            st.error("Your CSV must have a column named 'text'.")
        else:
            with st.spinner("Analyzing sentiment..."):
                # Apply your sentiment model
                user_df['Sentiment'] = user_df['text'].apply(get_sentiment)

            st.success("✅ Sentiment analysis complete!")
            st.dataframe(user_df.head(50))

            # Download button
            csv = user_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Predictions as CSV",
                data=csv,
                file_name="sentiment_results.csv",
                mime="text/csv"
            )

            
          
