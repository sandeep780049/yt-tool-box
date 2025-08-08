from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/thumbnail", methods=["GET", "POST"])
def thumbnail():
    if request.method == "POST":
        url = request.form["video_url"]
        try:
            yt = YouTube(url)
            thumbnail_url = yt.thumbnail_url
            return render_template("thumbnail.html", thumbnail_url=thumbnail_url)
        except Exception as e:
            return render_template("thumbnail.html", error=str(e))
    return render_template("thumbnail.html")

@app.route("/tags", methods=["GET", "POST"])
def tags():
    if request.method == "POST":
        url = request.form["video_url"]
        try:
            yt = YouTube(url)
            tags = yt.keywords
            return render_template("tags.html", tags=tags)
        except Exception as e:
            return render_template("tags.html", error=str(e))
    return render_template("tags.html")

@app.route("/keywords", methods=["GET", "POST"])
def keywords():
    if request.method == "POST":
        url = request.form["video_url"]
        try:
            yt = YouTube(url)
            keywords = yt.keywords
            return render_template("keywords.html", keywords=keywords)
        except Exception as e:
            return render_template("keywords.html", error=str(e))
    return render_template("keywords.html")

@app.route("/ai", methods=["GET", "POST"])
def ai():
    if request.method == "POST":
        topic = request.form["video_topic"]
        title = f"Top 5 Tips About {topic}"
        description = f"In this video, we dive into {topic} and explore the most effective strategies. Don’t miss out!"
        return render_template("ai.html", title=title, description=description)
    return render_template("ai.html")

@app.route("/stats", methods=["GET", "POST"])
def stats():
    return render_template("stats.html")

@app.route("/video-info", methods=["GET", "POST"])
def video_info():
    return render_template("video_info.html")

@app.route("/what-is-tag")
def what_is_tag():
    return render_template("what-is-tag.html")

@app.route("/what-is-thumbnail")
def what_is_thumbnail():
    return render_template("what-is-thumbnail.html")

@app.route("/what-is-keyword")
def what_is_keyword():
    return render_template("what-is-keyword.html")

@app.route("/about-site")
def about_site():
    return render_template("about_site.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")
