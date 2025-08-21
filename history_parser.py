# takeout_history_parser.py
import json
from urllib.parse import urlparse
import re

def parse_takeout_json(path):
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)

    entries = []
    # Try common shapes: list of records or dict containing lists
    if isinstance(obj, list):
        src = obj
    elif isinstance(obj, dict):
        # gather lists/dicts that look like history records
        src = []
        for v in obj.values():
            if isinstance(v, list):
                src.extend(v)
    else:
        src = []

    for item in src:
        if not isinstance(item, dict):
            continue
        url = item.get("url") or item.get("link") or None
        title = item.get("title") or item.get("header") or item.get("activity") or ""
        ts = item.get("time") or item.get("timestampMillis") or item.get("time_usec") or None

        if isinstance(title, str) and title != "":
            entries.append({"url": url or "", "title": title or "", "timestamp": ts})
    return entries

if __name__ == "__main__":
    INPATH = "history.json"  # edit to your Takeout file path
    parsed = parse_takeout_json(INPATH)
    print(f"Found {len(parsed)} records")
    import json
    with open("takeout_history_parsed.json","w",encoding="utf-8") as f:
        json.dump(parsed, f, ensure_ascii=False, indent=2)
    print("Saved takeout_history_parsed.json")