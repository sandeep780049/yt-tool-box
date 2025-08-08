from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

# Home
@app.route('/')
def index():
    return render_template('index.html')

# Thumbnail Downloader
@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            yt = YouTube(video_url)
            thumb_url = yt.thumbnail_url
            return render_template('thumbnail.html', thumbnail_url=thumb_url)
        except Exception as e:
            return render_template('thumbnail.html', error=str(e))
    return render_template('thumbnail.html')

# Tags & Keyword Generator
@app.route('/tags', methods=['GET', 'POST'])
def tags():
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            yt = YouTube(video_url)
            tags = yt.keywords
            return render_template('tags.html', tags=tags)
        except Exception as e:
            return render_template('tags.html', error=str(e))
    return render_template('tags.html')

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            yt = YouTube(video_url)
            keywords = yt.keywords
            return render_template('keywords.html', keywords=keywords)
        except Exception as e:
            return render_template('keywords.html', error=str(e))
    return render_template('keywords.html')

# AI Title & Description Generator (simple logic)
@app.route('/ai', methods=['GET', 'POST'])
def ai():
    if request.method == 'POST':
        topic = request.form['topic']
        if topic.strip() == '':
            return render_template('ai.html', error='Please enter a topic.')
        title = f"Top 5 Tips About {topic.title()}"
        description = f"Learn everything you need to know about {topic} in this video. Don't forget to like and subscribe!"
        return render_template('ai.html', title=title, description=description)
    return render_template('ai.html')

# Channel Stats (simplified using Pytube)
@app.route('/stats', methods=['GET', 'POST'])
def stats():
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            yt = YouTube(video_url)
            views = yt.views
            length = yt.length
            author = yt.author
            publish_date = yt.publish_date.strftime("%Y-%m-%d")
            return render_template('stats.html', views=views, length=length, author=author, publish_date=publish_date)
        except Exception as e:
            return render_template('stats.html', error=str(e))
    return render_template('stats.html')

# Video Info Viewer
@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            yt = YouTube(video_url)
            title = yt.title
            desc = yt.description
            length = yt.length
            author = yt.author
            return render_template('video_info.html', title=title, description=desc, length=length, author=author)
        except Exception as e:
            return render_template('video_info.html', error=str(e))
    return render_template('video_info.html')

# Informational Pages
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
