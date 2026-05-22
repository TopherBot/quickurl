# quickurl

A **tiny** command‑line tool to create short URLs via the public TinyURL API.

```
$ pip install -r requirements.txt
$ python quickurl.py https://example.com/very/long/path
https://tinyurl.com/abc123
```

## Features
- Single‑file implementation (≈60 LOC)
- No external configuration required
- Unit tests with mocked HTTP calls
- GitHub Actions CI (lint + pytest)

## License
MIT © 2024
