import feedparser, time

# Only fetch news <=6 hours old
FRESHNESS_HOURS = 6

RSS_FEEDS = {
    "tech": [
        "http://feeds.feedburner.com/Techcrunch",
        "https://www.theverge.com/rss/index.xml",
        "http://feeds.arstechnica.com/arstechnica/index"
    ],
    "ai": [
        "https://hnrss.org/frontpage",
        "https://openai.com/blog/rss/",
        "https://github.blog/feed/"
    ],
    "science": [
        "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml",
        "https://www.nature.com/subjects/artificial-intelligence.rss"
    ],
    "business": [
        "https://www.bloomberg.com/feeds/bbiz/technology.rss",
        "https://www.cnbc.com/id/10001147/device/rss/rss.html"
    ]
}

def fetch_latest_news():
    items = []
    now = time.time()
    for category, urls in RSS_FEEDS.items():
        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries[:3]:
                if hasattr(entry, 'published_parsed'):
                    published = time.mktime(entry.published_parsed)
                    hours_old = (now - published) / 3600
                    if hours_old > FRESHNESS_HOURS:
                        continue
                items.append({
                    "title": entry.title,
                    "url": entry.link,
                    "category": category
                })
    return items
