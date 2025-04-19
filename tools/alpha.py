import os
import json

ROOT_DIR = '../blog-posts'

# Loop through all folders in blog-posts/
for folder in os.listdir(ROOT_DIR):
    post_path = os.path.join(ROOT_DIR, folder)
    if os.path.isdir(post_path):
        images = [f for f in os.listdir(post_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]
        json_path = os.path.join(post_path, 'images.json')
        with open(json_path, 'w') as f:
            json.dump(images, f, indent=2)
        print(f'Written {len(images)} images to {json_path}')
