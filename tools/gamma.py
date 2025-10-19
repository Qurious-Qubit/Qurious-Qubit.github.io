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


if __name__ == "__main__":
    generate_sitemap()
