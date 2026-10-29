#!/usr/bin/env python3
"""Pixel Smith — smиттинг данных из API в JSON-отчёт."""

import json
import urllib.request

API_URL = "https://jsonplaceholder.typicode.com/posts"


def gather():
    with urllib.request.urlopen(API_URL, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))


def forge_report(posts):
    return {
        "total_posts": len(posts),
        "sample_titles": [p.get("title", "") for p in posts[:5]],
    }


def main():
    print(json.dumps(forge_report(gather()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
