import streamlit as st
import requests
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Step 1: Load environment variables (for API keys)
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Set in Streamlit Cloud secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Set in Streamlit Cloud secrets

# Step 2: Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Step 3: Function to fetch news articles using NewsAPI
def fetch_news(category):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={NEWS_API_KEY}&language=en"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        st.error("Error fetching news. Check your NewsAPI key or rate limit.")
        return []

# Step 4: Function to summarize an article using Gemini API
def summarize_article(article_text):
    prompt = f"Summarize this article in 3 sentences:\n\n{article_text}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error summarizing article: {e}")
        return "Summary unavailable."

# Step 5: Function to analyze sentiment using Gemini API
def analyze_sentiment(summary):
    prompt = f"Analyze the sentiment of this text (positive, negative, or neutral):\n\n{summary}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Sentiment analysis unavailable."

# Step 6: Streamlit App Setup
st.title("🗞️ News Explorer Hub")
st.markdown("Discover the latest news with AI-powered summaries! Select a category and explore.")

# Step 7: Category Selection Dropdown
categories = ["technology", "health", "sports", "business", "entertainment"]
selected_category = st.selectbox("Choose a news category:", categories)

# Step 8: Fetch and Display News
if st.button("Fetch News"):
    articles = fetch_news(selected_category)
    if articles:
        st.session_state['articles'] = articles
        st.session_state['summaries'] = []
        st.session_state['sentiments'] = []
        st.session_state['favorites'] = []

        for article in articles[:5]:
            article_text = article.get("content", article.get("description", "No content available"))
            summary = summarize_article(article_text)
            sentiment = analyze_sentiment(summary)
            st.session_state['summaries'].append(summary)
            st.session_state['sentiments'].append(sentiment)

# Step 9: Display Dashboard
if 'articles' in st.session_state and st.session_state['articles']:
    st.subheader(f"Top {selected_category.capitalize()} News Summaries")

    # Sentiment Meter
    sentiments = st.session_state['sentiments']
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
    for sentiment in sentiments:
        if "positive" in sentiment.lower():
            sentiment_counts["positive"] += 1
        elif "negative" in sentiment.lower():
            sentiment_counts["negative"] += 1
        else:
            sentiment_counts["neutral"] += 1
    st.write("**Sentiment Meter:**")
    st.progress(sentiment_counts["positive"] / len(sentiments) if sentiments else 0)
    st.write(f"Positive: {sentiment_counts['positive']}, Negative: {sentiment_counts['negative']}, Neutral: {sentiment_counts['neutral']}")

    # Display Summary Cards
    for i, (article, summary) in enumerate(zip(st.session_state['articles'][:5], st.session_state['summaries'])):
        st.markdown(f"### {article['title']}")
        st.write(f"**Source:** {article['source']['name']}")
        st.write(f"**Summary:** {summary}")
        st.write(f"**Sentiment:** {st.session_state['sentiments'][i]}")
        if st.button(f"Add to Favorites", key=f"fav_{i}"):
            st.session_state['favorites'].append({"title": article['title'], "summary": summary})
            st.success("Added to Favorites!")

# Step 10: Favorites Section
if st.session_state.get('favorites'):
    st.subheader("Your Favorites")
    for fav in st.session_state['favorites']:
        st.write(f"**{fav['title']}**")
        st.write(fav['summary'])
        st.write("---")

# Step 11: Footer
st.write("Built with ❤️ for AI beginners!")