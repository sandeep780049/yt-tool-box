from flask import Flask, render_template, request
from pytube import YouTube
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            thumbnail_url = yt.thumbnail_url
        except:
            thumbnail_url = None
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    video_tags = []
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            video_tags = yt.keywords
        except:
            video_tags = []
    return render_template('tags.html', video_tags=video_tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    video_keywords = []
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            video_keywords = yt.keywords
        except:
            video_keywords = []
    return render_template('keywords.html', video_keywords=video_keywords)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    generated_title = ""
    generated_description = ""
    if request.method == 'POST':
        topic = request.form['topic']
        generated_title = f"🔥 Must Watch: {topic} Explained in 5 Minutes!"
        generated_description = f"This video dives deep into the topic: {topic}. Learn interesting insights and useful tips. Don’t forget to like and subscribe!"
    return render_template('ai.html', generated_title=generated_title, generated_description=generated_description)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    video_stats = {}
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            video_stats = {
                "title": yt.title,
                "author": yt.author,
                "views": yt.views,
                "length": yt.length,
                "publish_date": yt.publish_date.strftime("%Y-%m-%d"),
                "description": yt.description[:300] + "..." if yt.description else ""
            }
        except:
            video_stats = {}
    return render_template('stats.html', video_stats=video_stats)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    info = {}
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            info = {
                "title": yt.title,
                "channel": yt.author,
                "length": yt.length,
                "views": yt.views,
                "description": yt.description[:300] + "..."
            }
        except:
            info = {}
    return render_template('video_info.html', info=info)

@app.route('/what-is-tag')
def what_is_tag():
    return render_template('what-is-tag.html')

@app.route('/what-is-thumbnail')
def what_is_thumbnail():
    return render_template('what-is-thumbnail.html')

@app.route('/what-is-keyword')
def what_is_keyword():
    return render_template('what-is-keyword.html')

@app.route('/about_site')
def about_site():
    return render_template('about_site.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ != "__main__":
    # Render-compatible: no app.run()
    pass
