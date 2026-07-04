import os
from datetime import datetime, timezone
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# -- IRONCLAD PATHS --
# 1. Find exactly where this script lives (the tools folder)
TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
# 2. Go up exactly one level to the main project folder
PROJECT_ROOT = os.path.dirname(TOOLS_DIR)

def generate_sitemap():
    base_url = "https://qurious-qubit.github.io"
    # 3. Force the sitemap to save in the main project folder
    sitemap_path = os.path.join(PROJECT_ROOT, "sitemap.xml")
    
    ignore_list = ['.git', 'tools', '.ref', 'googleab578e53430b81a4.html', '_layouts', '_data']
    
    now_utc = datetime.now(timezone.utc).isoformat(timespec='seconds')

    urlset_attrs = {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xsi:schemaLocation": "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    }
    urlset = Element("urlset", urlset_attrs)

    # 4. Walk through the main project folder
    for dirpath, dirnames, filenames in os.walk(PROJECT_ROOT):
        # Ignore hidden folders and specific lists
        dirnames[:] = [d for d in dirnames if d not in ignore_list and not d.startswith('_')]
        
        for filename in filenames:
            if filename in ignore_list or not filename.endswith(".html"):
                continue

            file_path = os.path.join(dirpath, filename)
            # Create the relative path for the URL
            relative_path = os.path.relpath(file_path, PROJECT_ROOT).replace("\\", "/")

            if relative_path == "index.html":
                page_url = base_url + "/"
                priority = "1.00"
            elif "blog-posts/" in relative_path:
                page_url = f"{base_url}/{relative_path}"
                priority = "0.9" 
            else:
                page_url = f"{base_url}/{relative_path}"
                priority = "0.80"

            url_element = SubElement(urlset, "url")
            loc_element = SubElement(url_element, "loc")
            loc_element.text = page_url
            lastmod_element = SubElement(url_element, "lastmod")
            lastmod_element.text = now_utc
            priority_element = SubElement(url_element, "priority")
            priority_element.text = priority

    xml_str = tostring(urlset, 'utf-8')
    pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")
    pretty_xml_str = "\n".join(pretty_xml_str.split("\n")[1:]) if pretty_xml_str.startswith("<?xml") else pretty_xml_str

    with open(sitemap_path, "w", encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(pretty_xml_str)

    print(f"✅ Sitemap generated successfully at {sitemap_path}")
    return len(urlset)

def main():
    print("=" * 50)
    print("Qurious-Qubit SEO Script - Sitemap Generator")
    print("=" * 50)
    
    try:
        url_count = generate_sitemap()
        print("\n" + "=" * 50)
        print("SCRIPT EXECUTION COMPLETE")
        print("=" * 50)
        print(f"• Sitemap URLs generated: {url_count}")
        
    except Exception as e:
        print(f"❌ Script failed with error: {e}")

if __name__ == "__main__":
    main()