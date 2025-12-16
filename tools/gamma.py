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
    CORRECTED: Replaces any existing scrollable archive with an updated one.
    Uses robust pattern matching to avoid duplication and extra lines.
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
    
    # Generate horizontally scrollable archive HTML - with EXACT line endings
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
      <div style="display: inline-flex; gap: 1.5rem; padding: 0 0.5rem;">'''
    
    # Add all posts as inline elements
    for i, post in enumerate(posts):
        if i > 0:
            archive_html += '\n'
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
        </a>'''
    
    archive_html += '''
      </div>
    </div>
    <div style="margin-top: 0.5rem; font-size: 0.8em; color: #666; text-align: center;">
      <small>← Scroll to see all posts →</small>
    </div>
  </div>'''
    
    # Read current blog.html content
    with open(blog_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove ALL existing scrollable archives
    archive_pattern = r'\s*<!-- Horizontally Scrollable Blog Archive for SEO -->.*?</div>\s*</div>\s*</div>'
    content = re.sub(archive_pattern, '', content, flags=re.DOTALL)
    
    # 2. Remove any hidden links
    hidden_pattern = r'\s*<div style="display: none;" aria-hidden="true">.*?</div>'
    content = re.sub(hidden_pattern, '', content, flags=re.DOTALL)
    
    # 3. Find the EXACT insertion point before footer
    # Look for the footer comment with potential whitespace
    lines = content.split('\n')
    insertion_line = -1
    
    for i, line in enumerate(lines):
        # Find the footer comment line
        if '<!-- Footer -->' in line.strip():
            insertion_line = i
            break
    
    if insertion_line >= 0:
        # Insert the archive with proper indentation
        # Get the indentation of the footer line
        footer_line = lines[insertion_line]
        indent_match = re.match(r'(\s*)<!-- Footer -->', footer_line)
        indent = indent_match.group(1) if indent_match else ''
        
        # Split archive_html into lines and apply proper indentation
        archive_lines = archive_html.split('\n')
        indented_archive = '\n'.join([indent + line if line.strip() else line for line in archive_lines])
        
        # Insert the archive before the footer
        lines.insert(insertion_line, indented_archive)
        content = '\n'.join(lines)
        print(f"✅ Inserted scrollable archive with {len(posts)} posts")
    else:
        # Fallback: append before closing body tag
        for i, line in enumerate(lines):
            if '</body>' in line:
                # Get indentation of the </body> tag
                indent_match = re.match(r'(\s*)</body>', line)
                indent = indent_match.group(1) if indent_match else ''
                
                # Split and indent archive
                archive_lines = archive_html.split('\n')
                indented_archive = '\n'.join([indent + line if line.strip() else line for line in archive_lines])
                
                lines.insert(i, indented_archive)
                content = '\n'.join(lines)
                print(f"⚠️  Appended archive before </body> with {len(posts)} posts")
                break
    
    # Write updated content back
    with open(blog_html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"📊 Total posts in archive: {len(posts)}")
    return True

def clean_duplicate_archives():
    """
    Emergency function to clean up multiple archive sections.
    Run this once if your blog.html has duplicates.
    """
    blog_html_path = "blog.html"
    
    with open(blog_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all archive sections
    archive_pattern = r'<!-- Horizontally Scrollable Blog Archive for SEO -->.*?</div>\s*</div>\s*</div>'
    archives = re.findall(archive_pattern, content, re.DOTALL)
    
    if len(archives) <= 1:
        print("✅ No duplicates found")
        return
    
    print(f"⚠️  Found {len(archives)} duplicate archive sections")
    
    # Keep only the FIRST archive
    content = re.sub(archive_pattern, '', content, flags=re.DOTALL)
    
    # Now we need to add one back before the footer
    footer_pattern = '  <!-- Footer -->'
    if footer_pattern in content:
        # We'll need to generate a fresh archive - call the main function
        update_blog_with_scrollable_archive()
    else:
        # Write cleaned content back
        with open(blog_html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"🧹 Removed {len(archives)-1} duplicate archive(s)")

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
        
        # 2. Check if we need to clean duplicates first
        blog_html_path = "blog.html"
        if os.path.exists(blog_html_path):
            with open(blog_html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Count how many archive sections exist
            archive_count = content.count('<!-- Horizontally Scrollable Blog Archive for SEO -->')
            if archive_count > 1:
                print(f"⚠️  Found {archive_count} archive sections (should be 1)")
                clean_duplicate_archives()
        
        # 3. Update with scrollable archive
        success = update_blog_with_scrollable_archive()
        
        # 4. Final report
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