#!/usr/bin/env python3
"""quickurl – tiny CLI for TinyURL API.
Usage:
    python quickurl.py <long_url>
"""
import sys
import requests

def shorten(url: str) -> str:
    """Return a TinyURL short link for *url*.
    Raises ValueError if the service returns a non‑200 response.
    """
    api = "http://tinyurl.com/api-create.php"
    resp = requests.get(api, params={"url": url}, timeout=5)
    if resp.status_code != 200:
        raise ValueError(f"TinyURL API error: {resp.status_code}")
    return resp.text.strip()

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: quickurl.py <long_url>")
        sys.exit(1)
    long_url = sys.argv[1]
    try:
        short = shorten(long_url)
        print(short)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
