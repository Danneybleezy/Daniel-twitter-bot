import time, logging, os
from feeds import fetch_latest_news
from formatter import format_post
from poster import post_to_all
from storage import was_posted, mark_posted, get_monthly_count

logging.basicConfig(filename="bot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def run_job():
    logging.info("Job started")
    # Quota check for Twitter (500 per month limit, stop at 480)
    if get_monthly_count() >= 480:
        logging.warning("Twitter quota reached for this month, skipping posting.")
        return

    news_items = fetch_latest_news()
    for item in news_items:
        if was_posted(item['url']):
            continue
        post = format_post(item)
        if post:
            try:
                post_to_all(post, item['category'])
                mark_posted(item['url'])
                break  # only 1 post per run
            except Exception as e:
                logging.error(f"Error posting: {e}")
    logging.info("Job finished")

if __name__ == "__main__":
    run_job()
