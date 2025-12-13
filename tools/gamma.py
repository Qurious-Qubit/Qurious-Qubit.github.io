import os
from datetime import datetime, timezone
from xml.etree.ElementTree import Element, SubElement, tostring, Comment
from xml.dom import minidom

def generate_sitemap():
    """
    Generates a detailed sitemap.xml with priority and lastmod timestamp
    for all .html files in the repository.
    """
    # --- Configuration ---
    base_url = "https://qurious-qubit.github.io"
    root_dir = "." 
    sitemap_path = os.path.join(root_dir, "sitemap.xml")
    ignore_list = ['.git', 'tools', '.ref', 'googleab578e53430b81a4.html']
    
    # --- Get current time in UTC for the <lastmod> tag ---
    # Format: YYYY-MM-DDTHH:MM:SS+00:00
    now_utc = datetime.now(timezone.utc).isoformat(timespec='seconds')

    # --- XML Root Element with Namespaces ---
    # This setup matches the required format exactly
    urlset_attrs = {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xsi:schemaLocation": "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    }
    urlset = Element("urlset", urlset_attrs)

    # --- Find all HTML files and build the sitemap ---
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in ignore_list]
        
        for filename in filenames:
            if filename in ignore_list or not filename.endswith(".html"):
                continue

            file_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(file_path, root_dir).replace("\\", "/")

            # --- Determine URL and Priority ---
            if relative_path == "index.html":
                page_url = base_url + "/"
                priority = "1.00"
            elif "blog-posts/" in relative_path:
                page_url = f"{base_url}/{relative_path}"
                priority = "0.9" 
            else:
                # Top-level pages like blog.html, contact.html, etc.
                page_url = f"{base_url}/{relative_path}"
                priority = "0.80"

            # --- Create XML elements for this URL ---
            url_element = SubElement(urlset, "url")
            
            loc_element = SubElement(url_element, "loc")
            loc_element.text = page_url
            
            lastmod_element = SubElement(url_element, "lastmod")
            lastmod_element.text = now_utc
            
            priority_element = SubElement(url_element, "priority")
            priority_element.text = priority

    # --- Write the XML to a file with pretty printing ---
    xml_str = tostring(urlset, 'utf-8')
    pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")
    
    # The default pretty print adds an extra <?xml...> line, we remove it
    # if it's not the first line.
    pretty_xml_str = "\n".join(pretty_xml_str.split("\n")[1:]) if pretty_xml_str.startswith("<?xml") else pretty_xml_str


    with open(sitemap_path, "w", encoding='utf-8') as f:
        # We need to manually add the correct XML declaration
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(pretty_xml_str)

    print(f"Detailed sitemap generated successfully at {sitemap_path}")

def update_blog_with_hidden_links():
    """
    Updates blog.html with hidden links to all blog posts for SEO
    """
    blog_html_path = "blog.html"
    
    # Find all blog post directories
    blog_posts = []
    blog_dir = "blog-posts"
    
    if os.path.exists(blog_dir):
        for folder in os.listdir(blog_dir):
            post_path = os.path.join(blog_dir, folder, "post.html")
            if os.path.exists(post_path):
                blog_posts.append(folder)
    
    if not blog_posts:
        print("No blog posts found to link")
        return
    
    # Read current blog.html content
    with open(blog_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate hidden links HTML
    hidden_links_html = '  <div style="display: none;" aria-hidden="true">\n'
    for post_folder in sorted(blog_posts):
        hidden_links_html += f'    <a href="blog-posts/{post_folder}/post.html">{post_folder}</a>\n'
    hidden_links_html += '  </div>'
    
    # Check if hidden links already exist and update them
    if '<div style="display: none;" aria-hidden="true">' in content:
        # Replace existing hidden links
        import re
        pattern = r'<div style="display: none;" aria-hidden="true">.*?</div>'
        new_content = re.sub(pattern, hidden_links_html, content, flags=re.DOTALL)
    else:
        # Insert hidden links before the footer
        footer_pattern = '  <!-- Footer -->'
        new_content = content.replace(footer_pattern, hidden_links_html + '\n\n' + footer_pattern)
    
    # Write updated content back
    with open(blog_html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated blog.html with {len(blog_posts)} hidden blog post links")

def update_blog_with_scrollable_archive():
    """
    Updates blog.html with a horizontally scrollable archive
    """
    blog_html_path = "blog.html"
    
    # Read the JSON to get post titles
    meta_path = "blog-posts/meta.json"
    posts = []
    
    try:
        import json
        with open(meta_path, 'r', encoding='utf-8') as f:
            posts = json.load(f)
    except Exception as e:
        print(f"Could not read {meta_path}: {e}")
        return
    
    if not posts:
        print("No blog posts found to link")
        return
    
    # Generate horizontally scrollable archive HTML
    archive_html = '''
  <!-- Horizontally Scrollable Blog Archive for SEO -->
  <div class="scrollable-archive" style="margin-top: 3rem;">
    <div style="margin-bottom: 0.5rem; font-weight: 500; color: #333;">
      <small>ALL POSTS</small>
    </div>
    <div style="
      overflow-x: auto;
      overflow-y: hidden;
      white-space: nowrap;
      padding: 1rem 0;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: thin;
    ">
      <div style="display: inline-flex; gap: 1.5rem; padding: 0 0.5rem;">
'''
    
    # Add all posts as inline elements
    for post in posts:
        archive_html += f'''        <a href="blog-posts/{post['folder']}/post.html" 
           style="
             display: inline-block;
             padding: 0.75rem 1.25rem;
             background: #f8f9fa;
             border: 1px solid #e9ecef;
             border-radius: 8px;
             color: #0066cc;
             text-decoration: none;
             white-space: nowrap;
             min-width: fit-content;
             font-size: 0.9em;
             transition: all 0.2s ease;
           "
           onmouseover="this.style.background='#e9ecef'; this.style.borderColor='#0066cc';"
           onmouseout="this.style.background='#f8f9fa'; this.style.borderColor='#e9ecef';"
        >
          {post['title']}
        </a>
'''
    
    archive_html += '''      </div>
    </div>
    <div style="margin-top: 0.5rem; font-size: 0.8em; color: #666; text-align: center;">
      <small>← Scroll to see all posts →</small>
    </div>
  </div>
'''
    
    # Insert into blog.html
    with open(blog_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any existing hidden links section first
    if '<div style="display: none;" aria-hidden="true">' in content:
        import re
        pattern = r'<div style="display: none;" aria-hidden="true">.*?</div>'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Insert scrollable archive before footer
    footer_pattern = '  <!-- Footer -->'
    if footer_pattern in content:
        new_content = content.replace(footer_pattern, archive_html + '\n\n' + footer_pattern)
    else:
        # Fallback: append before closing body tag
        body_pattern = '</body>'
        new_content = content.replace(body_pattern, archive_html + '\n' + body_pattern)
    
    with open(blog_html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Updated blog.html with {len(posts)} posts in horizontally scrollable archive")
    print("✓ Removed any existing hidden links")
    print("✓ Archive is mobile-friendly with touch scrolling")

if __name__ == "__main__":
    generate_sitemap()
    #update_blog_with_hidden_links()
    update_blog_with_scrollable_archive()
