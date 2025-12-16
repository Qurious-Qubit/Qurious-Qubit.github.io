import os
import re
import json
from datetime import datetime, timezone
from xml.etree.ElementTree import Element, SubElement, tostring
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
    now_utc = datetime.now(timezone.utc).isoformat(timespec='seconds')

    # --- XML Root Element with Namespaces ---
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
    pretty_xml_str = "\n".join(pretty_xml_str.split("\n")[1:]) if pretty_xml_str.startswith("<?xml") else pretty_xml_str

    with open(sitemap_path, "w", encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(pretty_xml_str)

    print(f"✅ Sitemap generated successfully at {sitemap_path}")
    return len(urlset)

def update_blog_with_scrollable_archive():
    """
    FIXED: Properly removes ALL duplicate archives before inserting a new one.
    """
    blog_html_path = "blog.html"
    
    # Read the JSON to get post titles
    meta_path = "blog-posts/meta.json"
    
    try:
        with open(meta_path, 'r', encoding='utf-8') as f:
            posts = json.load(f)
    except Exception as e:
        print(f"❌ Could not read {meta_path}: {e}")
        return False
    
    if not posts:
        print("❌ No blog posts found to link")
        return False
    
    # Generate horizontally scrollable archive HTML
    archive_html = '''  <!-- Horizontally Scrollable Blog Archive for SEO -->
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
    
    # Read current blog.html content
    with open(blog_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # CRITICAL FIX: Better regex pattern that matches the entire archive block
    # This pattern captures from the comment through all three closing </div> tags
    archive_pattern = r'  <!-- Horizontally Scrollable Blog Archive for SEO -->.*?</div>\s*\n\s*</div>\s*\n\s*</div>'
    
    # Count duplicates before removal
    archive_count = len(re.findall(archive_pattern, content, flags=re.DOTALL))
    print(f"🔍 Found {archive_count} archive section(s)")
    
    # Remove ALL instances of the archive (using re.DOTALL to match across newlines)
    content = re.sub(archive_pattern, '', content, flags=re.DOTALL)
    
    if archive_count > 0:
        print(f"🧹 Removed all {archive_count} archive section(s)")
    
    # SECOND: Remove any remaining whitespace artifacts
    # Clean up multiple blank lines left behind
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # THIRD: Insert the NEW archive before the footer
    footer_pattern = '  <!-- Footer -->'
    
    if footer_pattern in content:
        # Insert the archive right before the footer
        new_content = content.replace(footer_pattern, archive_html + '\n\n' + footer_pattern)
        print(f"✅ Inserted NEW scrollable archive with {len(posts)} posts")
    else:
        # Fallback: try to find any footer div
        footer_div_pattern = r'(\s*<div class="footer">)'
        match = re.search(footer_div_pattern, content)
        if match:
            new_content = content[:match.start()] + archive_html + '\n\n' + content[match.start():]
            print(f"⚠️  Found alternative footer, inserted archive with {len(posts)} posts")
        else:
            # Last resort: append before closing body tag
            body_pattern = '</body>'
            if body_pattern in content:
                new_content = content.replace(body_pattern, archive_html + '\n' + body_pattern)
                print(f"⚠️  Appended archive before </body> with {len(posts)} posts")
            else:
                print("❌ Could not find insertion point for archive")
                return False
    
    # Write updated content back
    with open(blog_html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"📊 Total posts in archive: {len(posts)}")
    print("📱 Archive is mobile-friendly with touch scrolling")
    return True

def clean_duplicate_archives():
    """
    Emergency function to clean up multiple archive sections.
    Run this independently if needed.
    """
    blog_html_path = "blog.html"
    
    with open(blog_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all archive sections
    archive_pattern = r'  <!-- Horizontally Scrollable Blog Archive for SEO -->.*?</div>\s*\n\s*</div>\s*\n\s*</div>'
    archive_count = len(re.findall(archive_pattern, content, flags=re.DOTALL))
    
    if archive_count == 0:
        print("✅ No archive sections found")
        return
    elif archive_count == 1:
        print("✅ Only one archive section found (correct state)")
        return
    
    print(f"⚠️  Found {archive_count} duplicate archive sections")
    
    # Remove ALL archives
    content = re.sub(archive_pattern, '', content, flags=re.DOTALL)
    
    # Clean up whitespace
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # Write cleaned content back
    with open(blog_html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"🧹 Removed all {archive_count} archive section(s)")
    print("⚠️  Run update_blog_with_scrollable_archive() to add a fresh archive")

def main():
    """
    Main execution function with error handling
    """
    print("=" * 50)
    print("Qurious-Qubit SEO Script")
    print("=" * 50)
    
    try:
        # 1. Generate sitemap
        url_count = generate_sitemap()
        
        # 2. Update blog with scrollable archive (this now handles duplicate removal)
        success = update_blog_with_scrollable_archive()
        
        # 3. Final report
        print("\n" + "=" * 50)
        print("SCRIPT EXECUTION COMPLETE")
        print("=" * 50)
        print(f"• Sitemap URLs: {url_count}")
        print(f"• Archive updated: {'✅' if success else '❌'}")
        print("\nNext steps:")
        print("1. Commit and push changes to GitHub")
        print("2. Submit sitemap in Google Search Console")
        print("3. Wait 24-48 hours for Google to crawl")
        
    except Exception as e:
        print(f"❌ Script failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()