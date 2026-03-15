import feedparser
import google.generativeai as genai

# Gemini API key
genai.configure(api_key="YOUR_API_KEY")

# Read finance news
feed = feedparser.parse("https://www.cnbc.com/id/10000664/device/rss/rss.html")

article = feed.entries[0]

title = article.title
summary = article.summary

prompt = f"""
Write a LinkedIn finance post.

Headline: {title}

1️⃣ Situation
2️⃣ Data insight
3️⃣ Investor view

Nifty: 23867

Rishabh Kale
"""

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content(prompt)

post = response.text

print(post)
