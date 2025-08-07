from flask import Flask, render_template, request, redirect, url_for
import requests
from pytube import YouTube

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Thumbnail Downloader
@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            thumbnail_url = yt.thumbnail_url
        except Exception:
            thumbnail_url = "Invalid URL or video not found"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

# Tags Generator
@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags_list = []
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            yt = YouTube(video_url)
            tags_list = yt.keywords
        except Exception:
            tags_list = ["Invalid video URL."]
    return render_template('tags.html', tags=tags_list)

# Keywords Generator
@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords_list = []
    if request.method == 'POST':
        topic = request.form['topic']
        if topic:
            # Dummy example keywords
            keywords_list = [
                f"{topic} tutorial", f"{topic} for beginners",
                f"{topic} 2025", f"how to use {topic}", f"{topic} tips"
            ]
    return render_template('keywords.html', keywords=keywords_list)

# Channel Stats Viewer
@app.route('/stats', methods=['GET', 'POST'])
def stats():
    data = {}
    if request.method == 'POST':
        channel_url = request.form['url']
        # Dummy values for now
        data = {
            "name": "Demo Channel",
            "subscribers": "1M",
            "views": "100M",
            "videos": "250"
        }
    return render_template('stats.html', data=data)

# AI Title & Description Generator
@app.route('/ai', methods=['GET', 'POST'])
def ai():
    title = ""
    description = ""
    if request.method == 'POST':
        topic = request.form['topic']
        if topic:
            title = f"Top 5 Tips About {topic}"
            description = f"Learn how to improve your content with these top {topic} tips for 2025. Perfect for creators trying to grow!"
    return render_template('ai.html', title=title, description=description)

# Info Pages
@app.route('/what-is-tags')
def what_is_tags():
    return render_template('what-is-tags.html')

@app.route('/what-is-thumbnails')
def what_is_thumbnails():
    return render_template('what-is-thumbnails.html')

@app.route('/what-is-keywords')
def what_is_keywords():
    return render_template('what-is-keywords.html')

@app.route('/about-site')
def about_site():
    return render_template('about_site.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')
