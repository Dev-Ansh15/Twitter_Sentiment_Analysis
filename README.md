# 📈 Social Media Sentiment Analysis Tool

A Python-based web application that fetches real-time tweets about a specific topic using the X (Twitter) API v2 and analyzes their sentiment using VADER (Valence Aware Dictionary and sEntiment Reasoner). The results are visualized in an interactive dashboard built with Streamlit.

---

## 🚀 Features

* **Real-time Data Fetching:** Connects directly to X/Twitter to get the latest tweets on any topic.
* **Sentiment Classification:** Categorizes tweets as Positive, Negative, or Neutral.
* **Interactive Dashboard:** User-friendly interface to search topics and view results instantly.
* **Data Visualization:** Displays sentiment distribution using dynamic bar charts and data tables.
* **Rate Limit Protection:** Includes smart caching to prevent hitting Twitter's API limits (`429 Too Many Requests`) when searching the same topic repeatedly.
* **Raw Data Inspection:** View the actual text and timestamps of analyzed tweets.

---

## 🛠️ Tech Stack

* **Language:** Python 3.7+
* **API:** Tweepy (Twitter API v2 Client)
* **NLP:** VaderSentiment
* **UI Framework:** Streamlit
* **Data Manipulation:** Pandas

---

## 📂 Project Structure
```
sentiment_analysis_project/
├── .env                      # Stores your API Bearer Token (Not uploaded to Git)
├── .gitignore                # Ignores unnecessary files
├── requirements.txt          # List of dependencies
├── config.py                 # Loads environment variables safely
├── sentiment_analyzer.py     # Core logic for fetching and analyzing tweets
├── app.py                    # Main Streamlit UI application
└── README.md                 # Project documentation
```

---

## ⚙️ Prerequisites

1. **Python Installed:** Make sure you have Python installed (`python --version`).
2. **X Developer Account:**
   * Go to the [X Developer Portal](https://developer.twitter.com/).
   * Create a Project/App.
   * **Important:** You need at least the "Basic" tier (paid) to use the Search Tweet endpoint. The "Free" tier only supports posting tweets, not searching.
   * Copy your Bearer Token.

---

## 📦 Installation

### 1. Clone or Download the project:
```bash
# If using git
git clone <repository-url>
cd sentiment_analysis_project
```

### 2. Create a Virtual Environment (Recommended):

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

1. Create a file named `.env` in the root directory.
2. Open it and paste your X API Bearer Token:
```env
BEARER_TOKEN="YOUR_ACTUAL_LONG_STRING_TOKEN_HERE"
```

**Note:** Do not use quotes around the token if your OS/editor adds them automatically, but standard `.env` syntax usually handles quotes fine.

---

## ▶️ How to Run

1. Ensure your virtual environment is active.
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. The application will open automatically in your default web browser (usually at `http://localhost:8501`).

---

## ⚠️ Troubleshooting & Common Errors

### 1. `429 Too Many Requests`
* **Cause:** You have exceeded the X API rate limit (approx. 15 requests per 15 minutes for Basic tier).
* **Solution:** The app will display a warning. You must wait 15 minutes before searching for a new topic. Searching for a topic you just searched for is fine (it uses cached data).

### 2. `403 Forbidden`
* **Cause:** Your API Access Level is too low.
* **Solution:** Ensure you have the Basic tier subscription on the X Developer Portal. The "Free" tier does not support `search_recent_tweets`.

### 3. `401 Unauthorized` or `ValueError: BEARER_TOKEN not found`
* **Cause:** The `.env` file is missing, the token is incorrect, or the file wasn't saved.
* **Solution:** Double-check that `.env` exists in the same folder as `app.py` and contains the correct `BEARER_TOKEN`.

### 4. `DeprecationWarning: use_container_width`
* **Cause:** Older versions of the code used a Streamlit parameter that is expiring.
* **Solution:** Ensure you are using the latest version of `app.py` provided in this project, which uses `width="stretch"`.

---

## 📊 Usage Example

1. Launch the app using `streamlit run app.py`
2. Enter a topic in the search box (e.g., "Python programming", "climate change")
3. Click "Analyze Sentiment"
4. View the sentiment distribution chart and detailed tweet analysis
5. Explore raw tweet data in the expandable section

---

## 📝 Future Enhancements

* Add support for filtering tweets by date range
* Implement more advanced NLP models (e.g., BERT, RoBERTa)
* Export analysis results to CSV/PDF
* Add historical sentiment tracking over time
* Support for multiple social media platforms

---

## 📜 License

This project is open-source. Feel free to modify and distribute.

**Disclaimer:** This tool is for educational purposes. Ensure you comply with the X (Twitter) Developer Agreement and Policy when using their data.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/sentiment-analysis/issues).

---
