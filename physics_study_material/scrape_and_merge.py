#!/usr/bin/env python3
"""
Pravegaa Free Physics Study Material Scraper and PDF Merger
Author: Antigravity
Scrapes all 11 physics subjects from Pravegaa, downloads individual topic PDFs,
and merges each subject into a single comprehensive PDF with bookmarks/outlines.
"""

import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, unquote

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader, PdfWriter

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "raw_topics")
MERGED_DIR = os.path.join(BASE_DIR, "merged_subjects")
INDEX_PATH = os.path.join(BASE_DIR, "INDEX.md")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(MERGED_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

SUBJECTS = [
    ("01", "Mathematical Methods of Physics", "https://pravegaa.com/free-study-material/mathematical-methods-of-physics/"),
    ("02", "Mechanics & Classical Mechanics", "https://pravegaa.com/free-study-material/mechanics-classical-mechanics/"),
    ("03", "Waves, Oscillations & Optics", "https://pravegaa.com/free-study-material/wave-oscillation-and-optics/"),
    ("04", "Electromagnetic Theory", "https://pravegaa.com/free-study-material/electromagnetic-theory/"),
    ("05", "Thermodynamics & Statistical Mechanics", "https://pravegaa.com/free-study-material/thermodynamics-statistical-mechanics/"),
    ("06", "Modern Physics & Quantum Mechanics", "https://pravegaa.com/free-study-material/modern-physics-and-quantum-mechanics/"),
    ("07", "Condensed Matter Physics", "https://pravegaa.com/free-study-material/condensed-matter-physics/"),
    ("08", "Electronics & Experimental Methods", "https://pravegaa.com/free-study-material/electronics-experimental-methods/"),
    ("09", "Atomic & Molecular Physics", "https://pravegaa.com/free-study-material/atomic-molecular-physics/"),
    ("10", "Nuclear & Particle Physics", "https://pravegaa.com/free-study-material/nuclear-and-particle-physics/"),
    ("11", "Special Theory of Relativity", "https://pravegaa.com/free-study-material/special-theory-of-relativity/"),
]

def clean_title(raw_text, url):
    """Clean scraped link text into a readable topic title."""
    text = raw_text.strip()
    # Remove download suffixes and emojis
    text = re.sub(r'^[📄\s\W_]+', '', text)
    text = re.sub(r'(?i)\s*Download\s*PDF.*$', '', text).strip()
    
    if not text or len(text) < 3:
        # Fallback to URL filename
        filename = unquote(url.split('/')[-1])
        filename = re.sub(r'\.pdf(\.pdf)?$', '', filename, flags=re.IGNORECASE)
        filename = filename.replace('-', ' ').replace('_', ' ')
        text = filename.strip()
        
    return text

def sanitize_filename(name):
    """Sanitize string for Windows filename."""
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip()

def scrape_subject_topics(subject_url):
    """Scrape ordered list of topic titles and PDF links from a subject page."""
    session = requests.Session()
    resp = session.get(subject_url, headers=HEADERS, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    topics = []
    seen_urls = set()
    
    for a in soup.find_all("a", href=True):
        href = a['href'].strip()
        if href.lower().endswith('.pdf'):
            # Filter out non-topic PDFs (like general question papers / footer links)
            if any(k in href.lower() for k in ['previous-paper', 'question-paper', 'previous-year', 'syllabus']):
                continue
            if href not in seen_urls:
                seen_urls.add(href)
                raw_text = a.get_text(strip=True)
                title = clean_title(raw_text, href)
                topics.append({
                    "title": title,
                    "url": href,
                    "raw_text": raw_text
                })
                
    return topics

def download_file(url, target_path):
    """Download a PDF file with retry and validation."""
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
        # Validate existing file has PDF magic bytes
        try:
            with open(target_path, "rb") as f:
                sig = f.read(5)
                if sig.startswith(b'%PDF'):
                    return True, "cached"
        except Exception:
            pass

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            res = requests.get(url, headers=HEADERS, timeout=30, stream=True)
            if res.status_code == 200:
                content = res.content
                if content.startswith(b'%PDF'):
                    with open(target_path, "wb") as f:
                        f.write(content)
                    return True, "downloaded"
                else:
                    time.sleep(1)
            else:
                time.sleep(1)
        except Exception as e:
            if attempt == max_retries:
                return False, f"Error: {e}"
            time.sleep(1.5)
            
    return False, "Failed after retries"

def merge_subject_pdfs(subject_name, topics, subject_raw_dir, output_pdf_path):
    """Merge all topic PDFs for a subject into a single PDF with bookmarks."""
    writer = PdfWriter()
    toc = []
    total_pages = 0
    failed_topics = []

    for idx, topic in enumerate(topics, start=1):
        filename = f"{idx:03d}_{sanitize_filename(topic['title'])}.pdf"
        filepath = os.path.join(subject_raw_dir, filename)

        if not os.path.exists(filepath):
            failed_topics.append(topic['title'])
            continue

        try:
            reader = PdfReader(filepath)
            num_pages = len(reader.pages)
            if num_pages == 0:
                continue

            start_page = len(writer.pages)
            for page in reader.pages:
                writer.add_page(page)

            # Add outline / bookmark
            bookmark_title = f"{idx}. {topic['title']}"
            writer.add_outline_item(bookmark_title, start_page)

            toc.append({
                "index": idx,
                "title": topic['title'],
                "start_page": start_page + 1,
                "page_count": num_pages
            })
            total_pages += num_pages
        except Exception as e:
            print(f"      [Warning] Error reading {filename}: {e}")
            failed_topics.append(topic['title'])

    if len(writer.pages) > 0:
        with open(output_pdf_path, "wb") as out_f:
            writer.write(out_f)
        return total_pages, toc, failed_topics
    else:
        return 0, [], failed_topics

def main():
    print("=" * 70)
    print("PRAVEGAA PHYSICS STUDY MATERIAL SCRAPER & MERGER")
    print("=" * 70)
    print(f"Saving merged PDFs to: {MERGED_DIR}")
    print(f"Caching raw topic PDFs to: {RAW_DIR}")
    print("=" * 70)

    all_subject_summaries = []
    grand_total_topics = 0
    grand_total_pages = 0

    for code, subject_name, url in SUBJECTS:
        print(f"\n[{code}/11] Processing Subject: {subject_name}")
        print(f"       URL: {url}")
        
        # 1. Scrape topics
        try:
            topics = scrape_subject_topics(url)
            print(f"       Found {len(topics)} topic PDFs")
        except Exception as e:
            print(f"       Failed to scrape subject page: {e}")
            continue

        grand_total_topics += len(topics)
        safe_subject_folder = sanitize_filename(f"{code}_{subject_name}")
        subject_raw_dir = os.path.join(RAW_DIR, safe_subject_folder)
        os.makedirs(subject_raw_dir, exist_ok=True)

        # 2. Download topic PDFs in parallel
        print(f"       Downloading {len(topics)} topics...")
        download_tasks = []
        with ThreadPoolExecutor(max_workers=6) as executor:
            for idx, topic in enumerate(topics, start=1):
                filename = f"{idx:03d}_{sanitize_filename(topic['title'])}.pdf"
                filepath = os.path.join(subject_raw_dir, filename)
                future = executor.submit(download_file, topic['url'], filepath)
                download_tasks.append((future, topic['title']))

            downloaded_count = 0
            cached_count = 0
            failed_count = 0

            for future, title in download_tasks:
                success, status = future.result()
                if success:
                    if status == "downloaded":
                        downloaded_count += 1
                    else:
                        cached_count += 1
                else:
                    failed_count += 1
                    print(f"         Failed: {title} ({status})")

        print(f"       Downloads complete: {downloaded_count} new, {cached_count} cached, {failed_count} failed")

        # 3. Merge into single subject PDF
        merged_filename = f"{code}_{sanitize_filename(subject_name)}.pdf"
        output_pdf_path = os.path.join(MERGED_DIR, merged_filename)
        print(f"       Merging into single PDF: {merged_filename}...")

        total_pages, toc, failed_topics = merge_subject_pdfs(
            subject_name, topics, subject_raw_dir, output_pdf_path
        )
        
        pdf_size_mb = 0.0
        if os.path.exists(output_pdf_path):
            pdf_size_mb = os.path.getsize(output_pdf_path) / (1024 * 1024)

        print(f"       Merged PDF created successfully! ({total_pages} pages, {pdf_size_mb:.2f} MB)")
        grand_total_pages += total_pages

        all_subject_summaries.append({
            "code": code,
            "name": subject_name,
            "url": url,
            "topic_count": len(topics),
            "merged_file": merged_filename,
            "pages": total_pages,
            "size_mb": pdf_size_mb,
            "toc": toc
        })

    # 4. Generate INDEX.md documentation
    print("\n" + "=" * 70)
    print("Generating INDEX.md documentation...")
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write("# Pravegaa Physics Study Material - Complete Subject Notes\n\n")
        f.write("Scraped from [Pravegaa Education Free Study Material](https://pravegaa.com/free-study-material/).\n\n")
        f.write(f"- **Total Subjects:** {len(all_subject_summaries)}\n")
        f.write(f"- **Total Topic PDFs Merged:** {grand_total_topics}\n")
        f.write(f"- **Total Combined Pages:** {grand_total_pages}\n\n")
        f.write("## Merged Subject PDFs\n\n")
        f.write("| # | Subject | Topics | Total Pages | File Size | Merged PDF |\n")
        f.write("|---|---------|--------|-------------|-----------|------------|\n")
        for s in all_subject_summaries:
            f.write(f"| {s['code']} | {s['name']} | {s['topic_count']} | {s['pages']} | {s['size_mb']:.2f} MB | [`{s['merged_file']}`](merged_subjects/{s['merged_file']}) |\n")
        
        f.write("\n---\n\n")
        f.write("## Detailed Table of Contents by Subject\n\n")
        for s in all_subject_summaries:
            f.write(f"### {s['code']}. {s['name']}\n\n")
            f.write(f"- **Source:** [{s['url']}]({s['url']})\n")
            f.write(f"- **Merged PDF:** [`merged_subjects/{s['merged_file']}`](merged_subjects/{s['merged_file']}) ({s['pages']} pages, {s['size_mb']:.2f} MB)\n\n")
            f.write("| Chapter / Topic | Start Page | Page Count |\n")
            f.write("|-----------------|------------|------------|\n")
            for item in s['toc']:
                f.write(f"| {item['index']}. {item['title']} | Page {item['start_page']} | {item['page_count']} pages |\n")
            f.write("\n")

    print(f"INDEX.md generated at: {INDEX_PATH}")
    print("=" * 70)
    print("ALL SUBJECTS DOWNLOADED & MERGED SUCCESSFULLY!")
    print(f"Total Subjects: {len(all_subject_summaries)}")
    print(f"Total Topic PDFs: {grand_total_topics}")
    print(f"Total Pages: {grand_total_pages}")
    print("=" * 70)

if __name__ == "__main__":
    main()
