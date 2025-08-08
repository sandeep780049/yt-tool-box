from flask import Flask, render_template, request
from pytube import YouTube
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            thumbnail_url = yt.thumbnail_url
            return render_template('thumbnail.html', thumbnail=thumbnail_url, url=url)
        except:
            return render_template('thumbnail.html', error="Invalid URL or video")
    return render_template('thumbnail.html')

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            tags = yt.keywords
            return render_template('tags.html', tags=tags, url=url)
        except:
            return render_template('tags.html', error="Invalid video URL")
    return render_template('tags.html')

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    if request.method == 'POST':
        topic = request.form['topic']
        generated_keywords = topic.lower().split() + ["viral", "trending", "2025"]
        return render_template('keywords.html', keywords=generated_keywords, topic=topic)
    return render_template('keywords.html')

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    if request.method == 'POST':
        topic = request.form['topic']
        title = f"🔥 {topic.title()} - Must Watch in 2025!"
        description = f"This video on {topic} covers everything you need to know. Stay tuned and subscribe for more updates!"
        return render_template('ai.html', title=title, description=description, topic=topic)
    return render_template('ai.html')

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            title = yt.title
            views = yt.views
            author = yt.author
            length = yt.length
            return render_template('stats.html', title=title, views=views, author=author, length=length, url=url)
        except:
            return render_template('stats.html', error="Invalid URL or video")
    return render_template('stats.html')

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            info = {
                'Title': yt.title,
                'Author': yt.author,
                'Publish Date': yt.publish_date,
                'Views': yt.views,
                'Length (s)': yt.length,
                'Description': yt.description
            }
            return render_template('video_info.html', info=info, url=url)
        except:
            return render_template('video_info.html', error="Invalid video URL")
    return render_template('video_info.html')

@app.route('/about_site')
def about_site():
    return render_template('about_site.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/what-is-tag')
def what_is_tag():
    return render_template('what-is-tag.html')

@app.route('/what-is-thumbnail')
def what_is_thumbnail():
    return render_template('what-is-thumbnail.html')

@app.route('/what-is-keyword')
def what_is_keyword():
    return render_template('what-is-keyword.html')
