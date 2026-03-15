import feedparser
import datetime

# News RSS feed
feed = feedparser.parse("https://www.cnbc.com/id/10000664/device/rss/rss.html")

article = feed.entries[0]

title = article.title
summary = article.summary

post = f"""
{title}

1️⃣ Market Situation
{summary}

2️⃣ What The Data Shows
Markets reacting to latest financial developments.

3️⃣ Investor View
Volatility creates opportunities for long-term investors.

Nifty: 23867

Rishabh Kale
"""

print(post)
