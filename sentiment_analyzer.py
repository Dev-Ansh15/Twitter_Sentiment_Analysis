import tweepy
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from config import settings

class SentimentAnalyzer:

    def __init__(self):
        if not settings.BEARER_TOKEN:
            raise ValueError("BEARER_TOKEN not found. Check your .env file.")
        
        self.client = tweepy.Client(bearer_token=settings.BEARER_TOKEN)
        self.analyzer = SentimentIntensityAnalyzer()

    def get_tweets(self, topic, max_results=20):
        query = f"{topic} -is:retweet lang:en"
        
        try:
            response = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=["text", "created_at"]
            )
            return response.data
            
        except tweepy.errors.TooManyRequests as e:
            # CRITICAL FIX: Re-raise this specific error so the App knows to tell the user to wait.
            raise e
            
        except tweepy.errors.TweepyException as e:
            print(f"Error fetching tweets: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def analyze_sentiment(self, tweet_text):
        score = self.analyzer.polarity_scores(tweet_text)
        compound = score['compound']
        
        if compound >= 0.05:
            return 'Positive'
        elif compound <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def run_analysis(self, topic, max_results=20):
        # This might raise TooManyRequests, which is caught in app.py
        tweets = self.get_tweets(topic, max_results)
        
        if not tweets:
            return pd.DataFrame()

        tweet_data = []
        for tweet in tweets:
            text = tweet.text
            sentiment = self.analyze_sentiment(text)
            tweet_data.append({
                'created_at': tweet.created_at,
                'tweet_text': text,
                'sentiment': sentiment
            })
        
        return pd.DataFrame(tweet_data)