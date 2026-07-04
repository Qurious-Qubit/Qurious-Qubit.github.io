import os
import json
import re
from bs4 import BeautifulSoup

# -- BULLETPROOF PATHS --
# Automatically find the project root by going up one level from the tools folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

BLOG_DIR = os.path.join(PROJECT_ROOT, 'blog-posts')
OUTPUT_FILE = os.path.join(BLOG_DIR, 'meta.json')

DATA_DIR = os.path.join(PROJECT_ROOT, '_data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
DATA_OUTPUT_FILE = os.path.join(DATA_DIR, 'meta.json')

def extract_post_data(folder_name):
    folder_path = os.path.join(BLOG_DIR, folder_name)
    if not os.path.isdir(folder_path):
        return None

    html_file = next((f for f in os.listdir(folder_path) if f.endswith('.html')), None)
    if not html_file:
        return None

    html_path = os.path.join(folder_path, html_file)
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Extract title
    title_tag = soup.select_one('.post-title h1')
    title = title_tag.get_text(strip=True) if title_tag else 'Untitled'

    # Extract category
    category_tag = soup.select_one('.post-category')
    category = category_tag.get_text(strip=True).lower() if category_tag else 'explore'

    # Extract summary
    para_tag = soup.select_one('.post-content-text p')
    if para_tag:
        text = para_tag.get_text(strip=True)
        words = text.split()
        summary = ' '.join(words[:30]) + ('...' if len(words) > 30 else '')
    else:
        summary = 'No summary available.'

    # Find thumbnail
    thumb_file = next((f for f in os.listdir(folder_path)
                      if f.lower().startswith('thumbnail') and f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp'))), None)
    
    if not thumb_file:
        thumb_file = next((f for f in os.listdir(folder_path)
                        if f.lower().startswith('image1.') and f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp'))), None)

    return {
        'title': title,
        'summary': summary,
        'folder': folder_name,
        'thumbnail': f'{folder_name}/{thumb_file}' if thumb_file else '',
        'category': category
    }

# Collect and sort posts
all_posts = []
folders = [f for f in os.listdir(BLOG_DIR) if os.path.isdir(os.path.join(BLOG_DIR, f))]

def sort_key(folder_name):
    if folder_name.startswith('post'):
        match = re.match(r'post(\d+)', folder_name)
        if match:
            return (0, int(match.group(1))) 
    return (1, folder_name)

folders.sort(key=sort_key, reverse=True)

for folder in folders:
    post_data = extract_post_data(folder)
    if post_data:
        all_posts.append(post_data)

# Write to frontend location
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(all_posts, f, indent=2)

# Write to Jekyll _data location
with open(DATA_OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(all_posts, f, indent=2)

print(f"✅ Generated metadata for {len(all_posts)} posts!")
print(f"📂 Saved to: {OUTPUT_FILE}")
print(f"📂 Saved to: {DATA_OUTPUT_FILE}")