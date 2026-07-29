import re

from config import settings

TARGET_HASHTAGS = [tag.strip() for tag in settings.TARGET_HASHTAGS.split(',')]
MONTHS = r'(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)'

def is_target_hashtag(text: str) -> bool:
    return any(hashtag in text for hashtag in TARGET_HASHTAGS)

def extract_type(text: str) -> str:
    return next((hashtag[1:] for hashtag in TARGET_HASHTAGS if hashtag in text), '')

def extract_name(text: str) -> str:
    if text.split()[0] == 'У' or text.split()[0] == 'у':
        return text.split()[1]
    return text.split()[0]

def extract_dates(text: str) -> str:
    date_single = rf'\d{{1,2}}\s+{MONTHS}'
    date_range_same_month = rf'\d{{1,2}}\s*[–-]\s*\d{{1,2}}\s+{MONTHS}'
    date_range_different_month = rf'\d{{1,2}}\s+{MONTHS}\s*[–-]\s*\d{{1,2}}\s+{MONTHS}'
    pattern = f'{date_range_different_month}|{date_range_same_month}|{date_single}'
    match = re.search(pattern, text)
    return match.group(0).strip()

def format_post(text: str) -> str:
    name = extract_name(text)
    post_type = extract_type(text)
    dates = extract_dates(text)

    return f'{name} {post_type} {dates}'

