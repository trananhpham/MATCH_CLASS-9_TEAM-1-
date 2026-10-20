import os
import re
import sys
import time
import requests
from bs4 import BeautifulSoup

TARGET_DIR = r"d:\toan lop 9 lang son"
TARGET_TOTAL = 50

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def count_existing_pdfs():
    files = [f for f in os.listdir(TARGET_DIR) if f.lower().endswith('.pdf')]
    return files

existing_files = count_existing_pdfs()
print(f"Current PDF count: {len(existing_files)}", flush=True)
if len(existing_files) >= TARGET_TOTAL:
    print(f"Already have {len(existing_files)} files (>= {TARGET_TOTAL}). Done!", flush=True)
    sys.exit(0)

# Queries to search on thcs.toanmath.com
queries = [
    'lạng sơn',
    'bắc sơn',
    'hữu lũng',
    'cao lộc',
    'chi lăng',
    'lộc bình',
    'đình lập',
    'văn lãng',
    'tràng định',
    'bình gia',
    'văn quan'
]

post_candidates = []
seen_posts = set()

print("Scanning search results...", flush=True)

for q in queries:
    p = 1
    while p <= 10:
        url = f'https://thcs.toanmath.com/page/{p}/?s={requests.utils.quote(q)}' if p > 1 else f'https://thcs.toanmath.com/?s={requests.utils.quote(q)}'
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code != 200:
                break
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article')
            if not articles:
                titles = soup.find_all(['h2', 'h3'], class_=lambda c: c and ('entry-title' in c or 'post-title' in c))
                items = []
                for t in titles:
                    a = t.find('a')
                    if a and a.get('href'):
                        items.append((a.get_text(strip=True), a['href']))
            else:
                items = []
                for a in articles:
                    title_elem = a.find(['h2', 'h3'])
                    link_elem = a.find('a')
                    title = title_elem.get_text(strip=True) if title_elem else (link_elem.get('title') or link_elem.get_text(strip=True) if link_elem else '')
                    href = link_elem['href'] if link_elem else None
                    if href:
                        items.append((title, href))
            
            if not items:
                break
            
            for title, href in items:
                if href in seen_posts:
                    continue
                seen_posts.add(href)
                
                # Check title / href relevance
                combined = (title + " " + href).lower()
                
                # Must be Lạng Sơn related
                ls_keywords = [
                    'lạng sơn', 'lang son', 'lang-son', 'bắc sơn', 'bac son', 'bac-son',
                    'hữu lũng', 'huu lung', 'huu-lung', 'cao lộc', 'cao loc', 'cao-loc',
                    'chi lăng', 'chi lang', 'chi-lang', 'lộc bình', 'loc binh', 'loc-binh',
                    'văn lãng', 'van lang', 'van-lang', 'tràng định', 'trang dinh', 'trang-dinh',
                    'bình gia', 'binh gia', 'binh-gia', 'văn quan', 'van quan', 'van-quan',
                    'đình lập', 'dinh lap', 'dinh-lap'
                ]
                if not any(k in combined for k in ls_keywords):
                    continue
                
                # Exclude explicitly other grades if no grade 9
                is_g6 = 'toán 6' in combined or 'toan-6' in combined or 'toan 6' in combined
                is_g7 = 'toán 7' in combined or 'toan-7' in combined or 'toan 7' in combined
                is_g8 = 'toán 8' in combined or 'toan-8' in combined or 'toan 8' in combined
                is_g9 = 'toán 9' in combined or 'toan-9' in combined or 'toan 9' in combined or 'lớp 9' in combined or 'lop-9' in combined
                is_ts10 = 'tuyển sinh' in combined or 'tuyen-sinh' in combined or 'vào 10' in combined or 'vao-10' in combined
                
                if (is_g6 or is_g7 or is_g8) and not is_g9:
                    continue
                
                if is_g9 or is_ts10:
                    post_candidates.append((title, href))
            
            if f'/page/{p+1}/' not in r.text and not soup.find('a', class_=lambda c: c and 'next' in c):
                break
            p += 1
        except Exception as e:
            print(f"Error searching {q} page {p}: {e}", flush=True)
            break

print(f"Found {len(post_candidates)} candidate posts for Math 9 / TS 10 Lang Son.", flush=True)

# Now iterate and download
current_pdfs = count_existing_pdfs()
print(f"Current count in directory: {len(current_pdfs)}", flush=True)

for title, post_url in post_candidates:
    if len(current_pdfs) >= TARGET_TOTAL:
        print(f"Reached {TARGET_TOTAL} files! Stopping.", flush=True)
        break
    
    try:
        r = requests.get(post_url, headers=headers, timeout=10)
        if r.status_code != 200:
            continue
        soup = BeautifulSoup(r.text, 'html.parser')
        
        pdf_url = None
        # Check download buttons first
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = a.get_text(strip=True).lower()
            if 'tải xuống pdf' in text or (href.endswith('.pdf') and 'thcs-pdf' in href):
                pdf_url = href
                break
        
        # If not found, any pdf link
        if not pdf_url:
            for a in soup.find_all('a', href=True):
                href = a['href']
                if href.lower().endswith('.pdf'):
                    pdf_url = href
                    break
        
        if not pdf_url:
            continue
        
        # Determine filename
        filename = os.path.basename(pdf_url)
        if not filename.endswith('.pdf'):
            # use slug
            slug = post_url.rstrip('/').split('/')[-1].replace('.html', '')
            filename = f"{slug}.pdf"
        
        target_path = os.path.join(TARGET_DIR, filename)
        if os.path.exists(target_path):
            print(f"[SKIP EXISTS] {filename}", flush=True)
            continue
        
        print(f"[DOWNLOADING] {filename} from {pdf_url}...", flush=True)
        pdf_res = requests.get(pdf_url, headers=headers, timeout=30)
        if pdf_res.status_code == 200 and len(pdf_res.content) > 1000:
            # Check if PDF header
            if pdf_res.content[:5] == b'%PDF-':
                with open(target_path, 'wb') as f:
                    f.write(pdf_res.content)
                current_pdfs = count_existing_pdfs()
                print(f"[SAVED] {filename} ({len(pdf_res.content)} bytes). Total now: {len(current_pdfs)}", flush=True)
            else:
                print(f"[WARN] Not a valid PDF: {filename}", flush=True)
        else:
            print(f"[FAIL] HTTP {pdf_res.status_code} for {pdf_url}", flush=True)
        
        time.sleep(0.5)
    except Exception as e:
        print(f"[ERROR] processing {post_url}: {e}", flush=True)

final_pdfs = count_existing_pdfs()
print(f"\nFinal count in {TARGET_DIR}: {len(final_pdfs)} files.", flush=True)
