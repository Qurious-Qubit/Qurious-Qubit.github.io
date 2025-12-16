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
    SUPER ROBUST: Removes ALL archive sections regardless of formatting.
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
    
    # NUCLEAR OPTION: Multiple passes with different patterns to catch all variations
    
    # Pattern 1: Standard formatting (2-space indent)
    pattern1 = r'  <!-- Horizontally Scrollable Blog Archive for SEO -->.*?</div>\s*\n\s*</div>\s*\n\s*</div>'
    
    # Pattern 2: 4-space indent variation
    pattern2 = r'    <!-- Horizontally Scrollable Blog Archive for SEO -->.*?</div>\s*\n\s*</div>\s*\n\s*</div>'
    
    # Pattern 3: No indent
    pattern3 = r'<!-- Horizontally Scrollable Blog Archive for SEO -->.*?</div>\s*\n\s*</div>\s*\n\s*</div>'
    
    # Pattern 4: Ultra flexible - matches any whitespace
    pattern4 = r'\s*<!-- Horizontally Scrollable Blog Archive for SEO -->.*?<small>← Scroll to see all posts →</small>\s*\n\s*</div>\s*\n\s*</div>'
    
    # Count before removal
    initial_count = content.count('<!-- Horizontally Scrollable Blog Archive for SEO -->')
    print(f"🔍 Found {initial_count} archive section(s) to remove")
    
    # Apply all patterns multiple times to ensure everything is caught
    for i in range(3):  # Run 3 passes to catch nested issues
        content = re.sub(pattern1, '', content, flags=re.DOTALL)
        content = re.sub(pattern2, '', content, flags=re.DOTALL)
        content = re.sub(pattern3, '', content, flags=re.DOTALL)
        content = re.sub(pattern4, '', content, flags=re.DOTALL)
    
    # Verify removal
    remaining = content.count('<!-- Horizontally Scrollable Blog Archive for SEO -->')
    if remaining > 0:
        print(f"⚠️  WARNING: {remaining} archive section(s) still remain!")
    else:
        print(f"🧹 Successfully removed all {initial_count} archive section(s)")
    
    # Clean up excessive whitespace
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # Find footer and insert NEW archive
    footer_pattern = '  <!-- Footer -->'
    
    if footer_pattern in content:
        # Insert the archive right before the footer
        new_content = content.replace(footer_pattern, archive_html + footer_pattern, 1)  # Only replace first occurrence
        print(f"✅ Inserted NEW scrollable archive with {len(posts)} posts before footer")
    else:
        # Fallback: try to find footer div
        footer_div_pattern = r'<div class="footer">'
        if footer_div_pattern in content:
            new_content = content.replace(footer_div_pattern, archive_html + '\n  <div class="footer">', 1)
            print(f"⚠️  Inserted archive before footer div with {len(posts)} posts")
        else:
            print("❌ Could not find insertion point for archive")
            return False
    
    # Write updated content back
    with open(blog_html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # Final verification
    with open(blog_html_path, 'r', encoding='utf-8') as f:
        final_content = f.read()
    
    final_count = final_content.count('<!-- Horizontally Scrollable Blog Archive for SEO -->')
    if final_count == 1:
        print(f"✅ SUCCESS! Exactly 1 archive section in final file")
    else:
        print(f"⚠️  WARNING: Final file has {final_count} archive sections (should be 1)")
    
    print(f"📊 Total posts in archive: {len(posts)}")
    print("📱 Archive is mobile-friendly with touch scrolling")
    return True

def main():
    """
    Main execution function with error handling
    """
    print("=" * 50)
    print("Qurious-Qubit SEO Script - SUPER ROBUST VERSION")
    print("=" * 50)
    
    try:
        # 1. Generate sitemap
        url_count = generate_sitemap()
        
        # 2. Update blog with scrollable archive
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