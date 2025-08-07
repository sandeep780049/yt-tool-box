from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/thumbnail", methods=["GET", "POST"])
def thumbnail():
    thumbnail_url = None
    if request.method == "POST":
        url = request.form["video_url"]
        if "v=" in url:
            video_id = url.split("v=")[-1].split("&")[0]
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[-1]
        else:
            video_id = url
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return render_template("thumbnail.html", thumbnail_url=thumbnail_url)

@app.route("/tags", methods=["GET", "POST"])
def tags():
    tags_list = []
    if request.method == "POST":
        video_url = request.form["video_url"]
        # Simulated tags for now
        tags_list = ["youtube", "video", "trending", "viral", "yt tools"]
    return render_template("tags.html", tags=tags_list)

@app.route("/stats", methods=["GET", "POST"])
def stats():
    data = {}
    if request.method == "POST":
        channel_id = request.form["channel_id"]
        data = {
            "channel_name": "Demo Channel",
            "subscribers": "1.2M",
            "views": "95M",
            "videos": "210"
        }
    return render_template("stats.html", data=data)

@app.route("/ai", methods=["GET", "POST"])
def ai():
    title = ""
    description = ""
    if request.method == "POST":
        topic = request.form["topic"]
        title = f"How to {topic} in 2025"
        description = f"Learn how to {topic} easily with our step-by-step tutorial."
    return render_template("ai.html", title=title, description=description)

@app.route("/video_info", methods=["GET", "POST"])
def video_info():
    info = {}
    if request.method == "POST":
        url = request.form["video_url"]
        info = {
            "title": "Sample Video",
            "duration": "10:15",
            "upload_date": "2024-12-01"
        }
    return render_template("video_info.html", info=info)
