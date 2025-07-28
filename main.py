import os
from src.reddit_scraper import scrape_reddit
from src.sentiment_analysis import analyze_sentiment

def main():
    query = input("Enter the Reddit search query: ")
    limit = int(input("Enter the number of posts to scrape (max=1000/search): "))
    
    os.makedirs("data", exist_ok=True)

    output_csv = "data/raw_reddit_data.csv"
    output_sentiment_csv = "data/output_sentiment.csv"

    scrape_reddit(query=query, limit=limit, output_csv=output_csv)
    analyze_sentiment(csv_path=output_csv, output_path=output_sentiment_csv)

if __name__ == "__main__":
    main()

