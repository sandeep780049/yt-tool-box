from flask import Flask, render_template, request
import requests
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        try:
            yt = YouTube(video_url)
            thumbnail_url = yt.thumbnail_url
        except Exception as e:
            thumbnail_url = None
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        try:
            yt = YouTube(video_url)
            tags = yt.keywords
        except:
            tags = []
    return render_template('tags.html', tags=tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        title = request.form.get('video_title')
        if title:
            words = title.lower().split()
            keywords = list(set(words))
    return render_template('keywords.html', keywords=keywords)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    generated_title = ""
    generated_description = ""
    if request.method == 'POST':
        topic = request.form.get('video_topic')
        if topic:
            generated_title = f"Top 5 Secrets About {topic.title()} You Must Know!"
            generated_description = f"Discover everything about {topic}. This video dives deep into {topic.lower()} tips, tricks, and hacks to boost your channel growth!"
    return render_template('ai.html', title=generated_title, description=generated_description)

@app.route('/about')
def about():
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

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    video_data = {}
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        try:
            yt = YouTube(video_url)
            video_data = {
                'title': yt.title,
                'author': yt.author,
                'views': yt.views,
                'publish_date': yt.publish_date,
                'length': yt.length,
                'description': yt.description
            }
        except:
            video_data = {}
    return render_template('video_info.html', video_data=video_data)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    stats_data = {}
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        try:
            yt = YouTube(video_url)
            stats_data = {
                'title': yt.title,
                'views': yt.views,
                'likes': "Unavailable via PyTube",
                'comments': "Unavailable via PyTube",
                'length': yt.length
            }
        except:
            stats_data = {}
    return render_template('stats.html', stats_data=stats_data)
