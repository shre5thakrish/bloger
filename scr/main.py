import os
import requests
from blogger_helpers import post_article, get_timestamp

def generate_content():
    prompt = f"""Generate a detailed 1500-word article about making money in 2025. Include:
    - 5 emerging AI technologies
    - 3 blockchain opportunities
    - Practical implementation steps
    - Real-world examples
    Current timestamp: {get_timestamp()}"""
    
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"},
        json={
            "messages": [{"role": "user", "content": prompt}],
            "model": "deepseek-chat",
            "max_tokens": 3000
        }
    )
    return response.json()['choices'][0]['message']['content']

if __name__ == "__main__":
    content = generate_content()
    result = post_article(content)
    print(f"Published post at: {result['url']}")
