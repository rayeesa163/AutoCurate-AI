import streamlit as st
from news_fetch import get_news
from summarizer import summarize_text
from forecast import get_forecast

st.set_page_config(page_title="AutoCurate AI", layout="wide")
st.title("🧠 AutoCurate AI Dashboard")
st.subheader("Live News Summarization + Forecasting")

st.header("📰 Top News Summaries")

try:
    st.write("✅ Fetching news...")
    news = get_news()
    st.write("✅ News fetched:", len(news))

    for title, desc in news:
        st.markdown(f"### {title}")
        st.write("🔹 Summary:", summarize_text(desc))
        st.markdown("---")
except Exception as e:
    st.error(f"⚠️ News Fetch Failed: {e}")

st.header("📈 Forecasting Trend")

try:
    st.write("✅ Starting forecast...")
    forecast = get_forecast()
    st.write("✅ Forecast loaded.")
    st.line_chart(forecast.set_index("ds")["yhat"])
except Exception as e:
    st.error(f"⚠️ Forecast Error: {e}")
