from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Play-Asia redirect server is working!"

@app.route("/ff14")
def ff14():
    return redirect(
        "https://www.play-asia.com/zh-cn/search/newfinalfantasyXIVmerch?tagid=5636933",
        code=302
    )

@app.route("/jacket")
def jacket():
    return redirect(
        "https://www.play-asia.com/zh-cn/final-fantasy-xiv-bomber-jacket-alpha-squadron-size-m/13/70khqf?tagid=5636933",
        code=302
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
