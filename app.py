from flask import Flask, render_template, request
from pytube import YouTube
import random

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required to fix 'Bad Request'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        url = request.form.get('video_url')
        if url:
            try:
                yt = YouTube(url)
                thumbnail_url = yt.thumbnail_url
            except:
                thumbnail_url = "Error retrieving thumbnail."
    return render_template("thumbnail.html", thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        url = request.form.get('video_url')
        if url:
            try:
                yt = YouTube(url)
                tags = yt.keywords
            except:
                tags = ["Error retrieving tags."]
    return render_template("tags.html", tags=tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        url = request.form.get('video_url')
        if url:
            try:
                yt = YouTube(url)
                keywords = yt.keywords
            except:
                keywords = ["No keywords found."]
    return render_template("keywords.html", keywords=keywords)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    titles = []
    if request.method == 'POST':
        topic = request.form.get('topic')
        if topic:
            titles = [f"{topic} - Top Secrets {i}" for i in range(1, 11)]
    return render_template("ai.html", titles=titles)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    stats = {}
    if request.method == 'POST':
        url = request.form.get('video_url')
        try:
            yt = YouTube(url)
            stats = {
                "title": yt.title,
                "views": yt.views,
                "length": yt.length,
                "author": yt.author
            }
        except:
            stats = {"error": "Failed to fetch video stats."}
    return render_template("stats.html", stats=stats)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    info = {}
    if request.method == 'POST':
        url = request.form.get('video_url')
        try:
            yt = YouTube(url)
            info = {
                "title": yt.title,
                "author": yt.author,
                "publish_date": yt.publish_date,
                "description": yt.description,
                "views": yt.views,
                "length": yt.length
            }
        except:
            info = {"error": "Could not retrieve video info."}
    return render_template("video_info.html", info=info)

@app.route('/whatis')
def whatis():
    return render_template("whatis.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

if __name__ == '__main__':
    app.run(debug=True)
