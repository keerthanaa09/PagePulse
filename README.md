# Page Pulse

Page Pulse is a Flask-based web application that analyzes any website URL and provides useful webpage metrics such as HTTP status, response time, SEO-related information, and content statistics.

## Features

- Analyse any website URL
- HTTP Status Code
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
git clone <https://github.com/keerthanaa09/PagePulse.git>

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
  "response_time":0.51,
  "title":"Example Website",
  "description":"This is an example webpage description.",
  "h1_count":1,
  "images_without_alt":2,
  "total_images":24,
  "total_links":144,
  "https":true,
  "word_count":935,
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