from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "Please enter a URL"}), 400

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:

        start = time.time()

        response = requests.get(url, timeout=10)

        end = time.time()

        response_time = round(end - start, 2)

        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type:
            return jsonify({"error": "URL does not contain HTML."}), 400

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No title"

        meta = soup.find("meta", attrs={"name": "description"})

        description = (
            meta["content"] if meta and meta.get("content") else "No description"
        )

        h1_count = len(soup.find_all("h1"))

        images = soup.find_all("img")

        total_images = len(images)

        missing_alt = sum(1 for img in images if not img.get("alt"))

        words = len(soup.get_text().split())

        links = len(soup.find_all("a"))

        https_used = url.startswith("https://")

        seo_score = 100

        if not https_used:
            seo_score -= 20

        if h1_count == 0:
            seo_score -= 20

        if missing_alt > 5:
            seo_score -= 10

        if words < 300:
            seo_score -= 20

        if seo_score < 0:
            seo_score = 0
        
        return jsonify({
            "status": response.status_code,
            "response_time": response_time,
            "title": title,
            "description": description,
            "h1_count": h1_count,
            "images_without_alt": missing_alt,
            "total_images": total_images,
            "total_links": links,
            "word_count": words,
            "https": https_used,
            "seo_score": seo_score
        })

    except requests.exceptions.Timeout:
        return jsonify({"error": "Website timed out"}), 408

    except requests.exceptions.RequestException:
        return jsonify({"error": "Invalid URL or connection failed"}), 400


if __name__ == "__main__":
    app.run(debug=True)