import os, requests, logging

def get_groq_text(title):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "", ""
    try:
        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": "You are a social media assistant. Given a news headline, generate a short catchy remark (max 20 words) and 3-4 relevant trending hashtags."},
                    {"role": "user", "content": title}
                ],
                "max_tokens": 60
            },
            timeout=20
        )
        data = r.json()
        text = data['choices'][0]['message']['content'].strip()
        parts = text.split("\n")
        remark, hashtags = "", ""
        if len(parts) >= 2:
            remark, hashtags = parts[0], parts[1]
        else:
            remark = text
        return remark, hashtags
    except Exception as e:
        logging.error(f"Groq API error: {e}")
        return "", ""

def format_post(item):
    remark, hashtags = get_groq_text(item['title'])
    text = f"{item['title']}\n{remark}\n{item['url']}\n{hashtags}"
    if len(text) > 280:
        text = text[:276] + "..."
    return {"text": text}
