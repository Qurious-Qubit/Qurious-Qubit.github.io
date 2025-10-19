# tools/gamma.py

import os
from datetime import date
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def generate_sitemap():
    """
    Generates a sitemap.xml for all .html files in the repository.
    """
    base_url = "https://qurious-qubit.github.io"
    root_dir = "." 
    sitemap_path = os.path.join(root_dir, "sitemap.xml")
    
    # Files or directories to ignore
    ignore_list = ['.git', 'tools', '.ref', 'googleab578e53430b81a4.html']

    urlset = Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    today = date.today().isoformat()

    # --- Find all HTML files and build the sitemap ---
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Remove ignored directories from the search
        dirnames[:] = [d for d in dirnames if d not in ignore_list]
        
        for filename in filenames:
            # Check if the current file should be ignored
            if filename in ignore_list:
                continue
            
            if filename.endswith(".html"):
                file_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(file_path, root_dir).replace("\\", "/")
                
                if relative_path == "index.html":
                    page_url = base_url + "/"
                else:
                    page_url = f"{base_url}/{relative_path}"

                url_element = SubElement(urlset, "url")
                loc_element = SubElement(url_element, "loc")
                loc_element.text = page_url
                lastmod_element = SubElement(url_element, "lastmod")
                lastmod_element.text = today

    xml_str = tostring(urlset, 'utf-8')
    pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")

    with open(sitemap_path, "w") as f:
        f.write(pretty_xml_str)

    print(f"Sitemap generated successfully at {sitemap_path}")


if __name__ == "__main__":
    generate_sitemap()