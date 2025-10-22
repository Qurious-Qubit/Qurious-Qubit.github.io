import os
import json
import re
from bs4 import BeautifulSoup

ROOT_DIR = 'blog-posts'
OUTPUT_FILE = os.path.join(ROOT_DIR, 'meta.json')

def extract_post_data(folder):
    folder_path = os.path.join(ROOT_DIR, folder)
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

    # Extract summary: first <p> inside .post-content-text
    para_tag = soup.select_one('.post-content-text p')
    if para_tag:
        text = para_tag.get_text(strip=True)
        words = text.split()
        summary = ' '.join(words[:30]) + ('...' if len(words) > 30 else '')
    else:
        summary = 'No summary available.'

    # Find thumbnail (default fallback is optional)
    thumb_file = next((f for f in os.listdir(folder_path)
                      if f.lower().startswith('thumbnail') and f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp'))), None)
    
    '''
    if not thumb_file:
        thumb_file = 'image1.jpg'  # Optional fallback
    '''
    if not thumb_file:
        thumb_file = next((f for f in os.listdir(folder_path)
                        if f.lower().startswith('image1.') and f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp'))), None)
    '''
    return {
        'title': title,
        'summary': summary,
        'folder': folder,
        'thumbnail': f'{folder}/{thumb_file}' if thumb_file else ''
    }
    '''
    return {
    'title': title,
    'summary': summary,
    'folder': folder,
    'thumbnail': f'{folder}/{thumb_file}' if thumb_file else '',
    'category': category
}
# Collect and sort posts
all_posts = []
folders = [f for f in os.listdir(ROOT_DIR) if os.path.isdir(os.path.join(ROOT_DIR, f))]

# Sort folders numerically for post1, post2, etc., others alphabetically
def sort_key(folder):
    if folder.startswith('post'):
        match = re.match(r'post(\d+)', folder)
        if match:
            return (0, int(match.group(1)))  # Sort post1, post2 numerically
    return (1, folder)  # Sort other folders alphabetically

folders.sort(key=sort_key, reverse=True)

for folder in folders:
    post_data = extract_post_data(folder)
    if post_data:
        all_posts.append(post_data)

# Write to meta.json
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(all_posts, f, indent=2)

print(f"✅ Generated metadata for {len(all_posts)} posts into {OUTPUT_FILE}")