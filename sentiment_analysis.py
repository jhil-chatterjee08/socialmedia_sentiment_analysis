import pandas as pd
from textblob import TextBlob

def analyze_sentiment(data, output_path="output_sentiment.csv"):
    if isinstance(data, str):  
        df = pd.read_csv(data)
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise ValueError("Input must be a file path or a pandas DataFrame")

    def get_sentiment(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'

    df['Sentiment'] = df['title'].apply(get_sentiment)
    df.to_csv(output_path, index=False)
    print(f"Sentiment analysis complete. Output saved to {output_path}")
    return df  

 
