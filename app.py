from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hostless is working!"

@app.route("/test")
def test():
    url = "https://www.play-asia.com/zh-cn/search/newfinalfantasyXIVmerch?tagid=5636933"

    try:
        r = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        return (
            f"UPSTREAM STATUS: {r.status_code}\n\n"
            f"FINAL URL: {r.url}\n\n"
            f"CONTENT TYPE: {r.headers.get('content-type')}\n\n"
            f"FIRST 3000 CHARACTERS:\n\n"
            f"{r.text[:3000]}"
        )

    except Exception as e:
        return f"ERROR: {e}", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
