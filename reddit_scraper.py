from src.config import reddit
import pandas as pd

def scrape_reddit(query, limit, output_csv):
    posts = []

    for submission in reddit.subreddit("all").search(query, limit=limit):
        posts.append([
            submission.created_utc,
            submission.title,
            submission.selftext,
            submission.subreddit.display_name,
            submission.url
        ])

    df = pd.DataFrame(posts, columns=["date", "title", "text", "subreddit", "url"])
    df.to_csv(output_csv, index=False)
    print(f"[INFO] Saved {len(df)} posts to {output_csv}")



