import os, json, datetime

CACHE_FILE = "posted.json"

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return []
    with open(CACHE_FILE, "r") as f:
        return json.load(f)

def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)

def was_posted(url):
    return url in load_cache()

def mark_posted(url):
    cache = load_cache()
    cache.append(url)
    save_cache(cache)
    increment_monthly_count()

def get_monthly_count():
    month_file = "tweet_count.json"
    month = datetime.datetime.utcnow().strftime("%Y-%m")
    if not os.path.exists(month_file):
        return 0
    with open(month_file, "r") as f:
        counts = json.load(f)
    return counts.get(month, 0)

def increment_monthly_count():
    month_file = "tweet_count.json"
    month = datetime.datetime.utcnow().strftime("%Y-%m")
    counts = {}
    if os.path.exists(month_file):
        with open(month_file, "r") as f:
            counts = json.load(f)
    counts[month] = counts.get(month, 0) + 1
    with open(month_file, "w") as f:
        json.dump(counts, f)
