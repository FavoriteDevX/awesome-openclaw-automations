import requests
import json
import os

# Configuration
KEYWORDS = ["openclaw", "llm", "ai agent", "autonomous", "ollama"]
TOP_STORIES_URL = "https://firebaseio.com"
ITEM_URL_TEMPLATE = "https://firebaseio.com{}.json"

def fetch_hn_updates():
    print("[OpenClaw Worker] Fetching Hacker News Top Stories...")
    try:
        response = requests.get(TOP_STORIES_URL, timeout=10)
        story_ids = response.json()[:30] # Check top 30 stories
        
        matched_stories = []
        for s_id in story_ids:
            story_data = requests.get(ITEM_URL_TEMPLATE.format(s_id), timeout=5).json()
            if not story_data or 'title' not in story_data:
                continue
                
            title_lower = story_data['title'].lower()
            if any(kw in title_lower for kw in KEYWORDS):
                matched_stories.append({
                    "title": story_data['title'],
                    "url": story_data.get('url', f"https://ycombinator.com{s_id}")
                })
        
        # Save output for OpenClaw Agent digestion
        output_file = "hn_digest_input.json"
        with open(output_file, "w") as f:
            json.dump(matched_stories, f, indent=4)
        print(f"[OpenClaw Worker] Found {len(matched_stories)} matching articles. Saved to {output_file}.")
        
    except Exception as e:
        print(f"Error executing HN Scraper: {e}")

if __name__ == "__main__":
    fetch_hn_updates()
