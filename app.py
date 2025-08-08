from flask import Flask, render_template, request
from pytube import YouTube
import random

app = Flask(__name__)

def generate_ai_title_description(topic):
    return {
        "title": f"🔥 Best Tips for {topic} YouTube Video!",
        "description": f"Learn how to grow your channel using this amazing {topic}-based content. Don't miss these key insights for creators!"
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/thumbnail", methods=["GET", "POST"])
def thumbnail():
    if request.method == "POST":
        url = request.form.get("url")
        try:
            yt = YouTube(url)
            return render_template("thumbnail.html", thumbnail_url=yt.thumbnail_url)
        except:
            return render_template("thumbnail.html", error="Invalid URL or video not found.")
    return render_template("thumbnail.html")

@app.route("/tags", methods=["GET", "POST"])
def tags():
    if request.method == "POST":
        url = request.form.get("url")
        try:
            yt = YouTube(url)
            tags = yt.keywords
            return render_template("tags.html", tags=tags)
        except:
            return render_template("tags.html", error="Video not found or tags not available.")
    return render_template("tags.html")

@app.route("/keywords", methods=["GET", "POST"])
def keywords():
    if request.method == "POST":
        url = request.form.get("url")
        try:
            yt = YouTube(url)
            keywords = yt.keywords
            return render_template("keywords.html", keywords=keywords)
        except:
            return render_template("keywords.html", error="Unable to fetch keywords.")
    return render_template("keywords.html")

@app.route("/video_info", methods=["GET", "POST"])
def video_info():
    if request.method == "POST":
        url = request.form.get("url")
        try:
            yt = YouTube(url)
            info = {
                "title": yt.title,
                "description": yt.description,
                "views": yt.views,
                "length": yt.length,
                "author": yt.author
            }
            return render_template("video_info.html", info=info)
        except:
            return render_template("video_info.html", error="Failed to fetch video info.")
    return render_template("video_info.html")

@app.route("/ai", methods=["GET", "POST"])
def ai():
    if request.method == "POST":
        topic = request.form.get("topic")
        if topic:
            result = generate_ai_title_description(topic)
            return render_template("ai.html", result=result)
    return render_template("ai.html")

@app.route("/about_site")
def about_site():
    return render_template("about_site.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/what-is-tags")
def what_is_tags():
    return render_template("what-is-tag.html")

@app.route("/what-is-thumbnails")
def what_is_thumbnails():
    return render_template("what-is-thumbnail.html")

@app.route("/what-is-keywords")
def what_is_keywords():
    return render_template("what-is-keyword.html")

# No if __name__ part needed for Render
