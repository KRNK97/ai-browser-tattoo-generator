# summarize_history.py
import json
from urllib.parse import urlparse
from collections import Counter, defaultdict
import re
from nltk.util import ngrams
from nltk.corpus import stopwords
import nltk

# Download required NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def clean_text(text):
    """Clean and normalize text for better phrase extraction"""
    # Convert to lowercase
    text = text.lower()
    # Remove special characters but keep spaces and hyphens
    text = re.sub(r'[^\w\s\-]', ' ', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_domain_from_url(url):
    """Extract domain name from URL"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        # Remove www. prefix if present
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain
    except:
        return ""

def group_titles_by_domain(entries):
    """Group unique titles by their domain names"""
    domain_titles = defaultdict(set)
    
    for entry in entries:
        url = entry.get("url", "")
        title = entry.get("title", "")
        
        if url and title:
            domain = extract_domain_from_url(url)
            if domain:
                # Clean the title
                cleaned_title = clean_text(title)
                if cleaned_title and len(cleaned_title) > 5:  # Filter out very short titles
                    domain_titles[domain].add(cleaned_title)
    
    return domain_titles

def get_top_domains_with_titles(domain_titles, top_n=25):
    """Get top domains with their most frequent titles"""
    # Count total entries per domain (proxy for frequency)
    domain_counts = {domain: len(titles) for domain, titles in domain_titles.items()}
    
    # Sort by count and get top domains
    top_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    # For each top domain, get up to 5 most representative titles
    result = []
    for domain, count in top_domains:
        titles = list(domain_titles[domain])
        # Sort titles by length (longer titles often have more context)
        titles.sort(key=len, reverse=True)
        top_titles = titles[:5]  # Take top 5 titles
        
        result.append({
            "domain": domain,
            "visit_count": count,
            "top_titles": top_titles
        })
    
    return result

def build_summary(entries):
    """Build comprehensive summary with domain-grouped data"""
    print("📊 Processing browsing history...")
    
    # Group titles by domain
    domain_titles = group_titles_by_domain(entries)
    print(f"✅ Found {len(domain_titles)} unique domains")
    
    # Get top domains with their titles
    top_domains_with_titles = get_top_domains_with_titles(domain_titles, top_n=25)
    
    # Create summary
    summary = {
        "total_pages": len(entries),
        "unique_domains": len(domain_titles),
        "top_domains_with_titles": top_domains_with_titles,
        "sample_titles": [e.get("title", "") for e in entries[:10] if e.get("title")]
    }
    
    return summary

if __name__ == "__main__":
    print("🔍 Loading browsing history data...")
    with open("takeout_history_parsed.json", "r", encoding="utf-8") as f:
        entries = json.load(f)
    
    print(f"📚 Loaded {len(entries)} browsing history entries")
    
    summary = build_summary(entries)
    
    with open("history_summary.json", "w", encoding="utf-8") as out:
        json.dump(summary, out, ensure_ascii=False, indent=2)
    
    print("✅ Saved history_summary.json")
    
    # Print summary of what we found
    print(f"\n📊 Summary:")
    print(f"   Total pages: {summary['total_pages']}")
    print(f"   Unique domains: {summary['unique_domains']}")
    print(f"   Top domains analyzed: {len(summary['top_domains_with_titles'])}")
    
    print(f"\n🏆 Top 10 domains with their most visited titles:")
    for i, domain_data in enumerate(summary['top_domains_with_titles'][:10], 1):
        print(f"\n{i}. {domain_data['domain']} ({domain_data['visit_count']} visits)")
        for j, title in enumerate(domain_data['top_titles'][:3], 1):  # Show top 3 titles
            print(f"   {j}. {title[:80]}{'...' if len(title) > 80 else ''}")
