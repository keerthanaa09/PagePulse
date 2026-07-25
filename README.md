# Page Pulse

Page Pulse is a Flask-based web application that analyzes any website URL and provides useful webpage metrics such as HTTP status, response time, SEO-related information, and content statistics.

## Features

- HTTP Status
- Response Time
- Page Title
- Meta Description
- H1 Count
- Images without Alt Text
- Total Images
- Total Links
- Word Count
- HTTPS Detection
- SEO Score
- Error Handling for Invalid URLs and Timeouts

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- BeautifulSoup
- Requests
- Pytest

## Installation

```bash
git clone <repository_url>

cd PagePulse

pip install -r requirements.txt

python app.py
```

Visit:

```
http://127.0.0.1:5000
```

## API

### POST /analyze

Input

```json
{
  "url":"https://example.com"
}
```

Output

```json
{
  "status":200,
  "response_time":0.8,
  "title":"Example",
  "description":"Example description",
  "h1_count":1,
  "images_without_alt":2,
  "word_count":1500,
  "seo_score":90
}
```

## Design Decisions

- Flask was selected because it is lightweight and well suited for REST APIs.
- BeautifulSoup was used for reliable HTML parsing.
- Proper exception handling ensures the application never crashes due to invalid URLs or timeouts.

## Testing

Run:

```bash
pytest
```

## Author
Keerthana B Y

Built for Digital Heroes Training Task