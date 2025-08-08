from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

# Home
@app.route("/")
def home():
    return render_template("index.html")

# Thumbnail Downloader
@app.route("/thumbnail", methods=["GET", "POST"])
def thumbnail():
    thumbnail_url = None
    if request.method == "POST":
        video_url = request.form["video_url"]
        yt = YouTube(video_url)
        thumbnail_url = yt.thumbnail_url
    return render_template("thumbnail.html", thumbnail_url=thumbnail_url)

# Tag Generator
@app.route("/tags", methods=["GET", "POST"])
def tags():
    tags = []
    if request.method == "POST":
        video_url = request.form["video_url"]
        yt = YouTube(video_url)
        tags = yt.keywords
    return render_template("tags.html", tags=tags)

# Keyword Generator
@app.route("/keywords", methods=["GET", "POST"])
def keywords():
    keywords = []
    if request.method == "POST":
        topic = request.form["topic"]
        keywords = [f"{topic} tutorial", f"{topic} explained", f"learn {topic} fast"]
    return render_template("keywords.html", keywords=keywords)

# Stats Viewer
@app.route("/stats", methods=["GET", "POST"])
def stats():
    stats = {}
    if request.method == "POST":
        channel_url = request.form["channel_url"]
        stats = {
            "name": "Test Channel",
            "subs": "1M",
            "views": "100M",
            "videos": "250"
        }
    return render_template("stats.html", stats=stats)

# AI Title & Description Generator
@app.route("/ai", methods=["GET", "POST"])
def ai():
    title = ""
    description = ""
    if request.method == "POST":
        topic = request.form["topic"]
        title = f"🔥 Must Watch: {topic} Explained in 5 Minutes!"
        description = f"This video covers everything you need to know about {topic}. Boost your YouTube SEO and grow your channel with powerful content!"
    return render_template("ai.html", title=title, description=description)

# Video Info Viewer
@app.route("/video-info", methods=["GET", "POST"])
def video_info():
    if request.method == "POST":
        video_url = request.form["video_url"]
        yt = YouTube(video_url)
        video_info = {
            "title": yt.title,
            "views": yt.views,
            "duration": f"{yt.length // 60}:{yt.length % 60:02d}",
            "publish_date": yt.publish_date.strftime("%Y-%m-%d"),
            "description": yt.description
        }
        return render_template("video_info.html", video_info=video_info)
    return render_template("video_info.html", video_info=None)

# Informational Pages
@app.route("/what-is-tag")
def what_is_tag():
    return render_template("what-is-tag.html")

@app.route("/what-is-keyword")
def what_is_keyword():
    return render_template("what-is-keyword.html")

@app.route("/what-is-thumbnail")
def what_is_thumbnail():
    return render_template("what-is-thumbnail.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/about-site")
def about_site():
    return render_template("about_site.html")
