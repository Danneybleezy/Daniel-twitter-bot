# Tech News Bot (Final DBOS Version)

Automated bot that fetches tech/AI/science/business news and posts to Twitter, Facebook, Telegram.

## Features
- Multi-RSS feed aggregation
- Freshness filter (<=6h old)
- AI-generated remarks + hashtags (Groq API)
- Deduplication (no reposts)
- Quota aware (Twitter free tier: 500/month, stops at 480)
- Error logging & retry
- Test mode (set TEST_MODE=true)
- Runs on DBOS Cron (default: every 3 hours)

## Setup
1. Push to GitHub.
2. Connect repo in DBOS Console.
3. Set secrets in DBOS UI:
   - TWITTER_API_KEY
   - TWITTER_API_SECRET
   - TWITTER_ACCESS_TOKEN
   - TWITTER_ACCESS_SECRET
   - FACEBOOK_PAGE_TOKEN
   - TELEGRAM_BOT_TOKEN
   - TELEGRAM_CHANNEL_ID
   - GROQ_API_KEY
   - (Optional) TEST_MODE

## Run locally
```bash
pip install -r requirements.txt
TEST_MODE=true python main.py
```
