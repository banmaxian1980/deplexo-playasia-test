import requests
from flask import Flask, Response

app = Flask(__name__)

TARGET = "https://www.play-asia.com/zh-cn/search/newfinalfantasyXIVmerch?tagid=5636933"


@app.route("/")
def home():
    return "Deplexo test server is running."


@app.route("/test")
def test():
    try:
        r = requests.get(
            TARGET,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            allow_redirects=True,
        )

        return Response(
            "HTTP status: %s\n\n"
            "Final URL: %s\n\n"
            "Content-Type: %s\n\n"
            "First 2000 chars:\n\n%s"
            % (
                r.status_code,
                r.url,
                r.headers.get("content-type", ""),
                r.text[:2000],
            ),
            content_type="text/plain; charset=utf-8",
        )

    except Exception as e:
        return Response(
            "REQUEST ERROR:\n\n%s" % e,
            status=502,
            content_type="text/plain; charset=utf-8",
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
