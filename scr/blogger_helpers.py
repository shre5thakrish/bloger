from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

def get_blogger_service():
    return build(
        'blogger', 
        'v3',
        credentials=Credentials(
            token=None,
            refresh_token=os.getenv('BLOGGER_REFRESH_TOKEN'),
            client_id=os.getenv('BLOGGER_CLIENT_ID'),
            client_secret=os.getenv('BLOGGER_CLIENT_SECRET'),
            token_uri="https://oauth2.googleapis.com/token"
        )
    )

def post_article(content: str):
    service = get_blogger_service()
    return service.posts().insert(
        blogId=os.getenv('BLOGGER_BLOG_ID'),
        body={
            "title": f"2025 Money Making Update {get_timestamp()}",
            "content": content,
            "labels": ["Automation", "2025", "AI"]
        }
    ).execute()

def get_timestamp():
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d %H:%M')
