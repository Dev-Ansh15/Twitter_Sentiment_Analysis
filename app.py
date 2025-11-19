import streamlit as st
import pandas as pd
import tweepy
from sentiment_analyzer import SentimentAnalyzer

# Set page configuration
st.set_page_config(page_title="X Sentiment Analyzer", layout="wide")

st.title("📈 X (Twitter) Sentiment Analyzer")
st.write("Enter a topic or keyword to analyze the sentiment of recent tweets.")

# --- Sidebar for Inputs ---
with st.sidebar:
    st.header("Search Parameters")
    topic = st.text_input("Topic or Keyword:", "Tesla")
    max_results = st.number_input("Number of Tweets to Analyze:", min_value=10, max_value=100, value=20)
    analyze_button = st.button("Analyze Sentiment")

# --- Caching Function ---
# FIX: This decorator saves the result. If you search "Tesla" again, 
# it loads from memory instead of hitting the API limit.
@st.cache_data(ttl=900, show_spinner=False) 
def get_analyzed_data(topic, max_results):
    analyzer = SentimentAnalyzer()
    return analyzer.run_analysis(topic, max_results)

# --- Main Content Area ---
if analyze_button:
    if not topic:
        st.warning("Please enter a topic to analyze.")
    else:
        try:
            with st.spinner(f"Fetching and analyzing {max_results} tweets for '{topic}'..."):
                # Call the cached function
                df = get_analyzed_data(topic, max_results)
            
            if df.empty:
                st.info("No tweets found for this topic. Try another keyword.")
            else:
                st.success("Analysis Complete!")
                
                # --- Display Results ---
                st.subheader("Sentiment Summary")
                
                # Data processing for charts
                sentiment_counts = df['sentiment'].value_counts().reset_index()
                sentiment_counts.columns = ["sentiment", "count"]
                
                sentiment_percentage = (df['sentiment'].value_counts(normalize=True) * 100).round(2)
                summary_df = pd.DataFrame({
                    'Count': df['sentiment'].value_counts(),
                    'Percentage': sentiment_percentage.astype(str) + '%'
                }).reindex(['Positive', 'Neutral', 'Negative']).fillna(0)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.dataframe(summary_df, width="stretch")
                with col2:
                    st.bar_chart(
                        sentiment_counts, 
                        x="sentiment", 
                        y="count", 
                        color="sentiment"
                    )

                st.subheader("Raw Tweet Data")
                df_display = df[['created_at', 'sentiment', 'tweet_text']]
                st.dataframe(df_display, width="stretch")

        except tweepy.errors.TooManyRequests:
            # FIX: Specific error message for Rate Limit
            st.error("🚨 **API Rate Limit Exceeded**")
            st.error("Twitter/X limits how many searches you can do in a short time.")
            st.warning("⏳ **Please wait 15 minutes** before trying again.")
            
        except ValueError as e:
            st.error(f"Configuration Error: {e}")
            st.error("Please make sure you have created a .env file with your BEARER_TOKEN.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")