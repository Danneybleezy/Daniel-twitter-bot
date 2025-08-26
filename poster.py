import os, requests, tweepy, logging, time

def safe_call(func, retries=1):
    for attempt in range(retries+1):
        try:
            return func()
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            time.sleep(2)
    return None

def post_to_twitter(text):
    def action():
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_SECRET")
        )
        api = tweepy.API(auth)
        api.update_status(text)
        logging.info("Posted to Twitter")
    return safe_call(action)

def post_to_facebook(text):
    def action():
        token = os.getenv("FACEBOOK_PAGE_TOKEN")
        page_id = "me"
        url = f"https://graph.facebook.com/{page_id}/feed"
        requests.post(url, data={"message": text, "access_token": token})
        logging.info("Posted to Facebook")
    return safe_call(action)

def post_to_telegram(text, category):
    def action():
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        channel_id = os.getenv("TELEGRAM_CHANNEL_ID")
        prefix = f"[{category.upper()}] "
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": channel_id, "text": prefix + text})
        logging.info("Posted to Telegram")
    return safe_call(action)

def post_to_all(post, category):
    text = post['text']
    if os.getenv("TEST_MODE") == "true":
        print("TEST MODE:", text)
        return
    post_to_twitter(text)
    post_to_facebook(text)
    post_to_telegram(text, category)
