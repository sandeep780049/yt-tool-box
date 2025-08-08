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
        url = request.form.get('video_url')
        try:
            yt = YouTube(url)
            thumbnail_url = yt.thumbnail_url
        except Exception as e:
            print("Error:", e)
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags_list = []
    if request.method == 'POST':
        url = request.form.get('video_url')
        try:
            yt = YouTube(url)
            tags_list = yt.keywords
        except Exception as e:
            print("Error:", e)
    return render_template('tags.html', tags=tags_list)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords_list = []
    if request.method == 'POST':
        url = request.form.get('video_url')
        try:
            yt = YouTube(url)
            keywords_list = yt.keywords
        except Exception as e:
            print("Error:", e)
    return render_template('keywords.html', keywords=keywords_list)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    generated_title = ""
    generated_description = ""
    if request.method == 'POST':
        topic = request.form.get('video_topic')
        if topic:
            generated_title = f"Top 10 Tips About {topic} You Must Know!"
            generated_description = f"Discover the most useful insights on {topic}. This video covers everything you need to grow your channel!"
    return render_template('ai.html', title=generated_title, description=generated_description)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    video_stats = {}
    if request.method == 'POST':
        url = request.form.get('video_url')
        try:
            yt = YouTube(url)
            video_stats = {
                'title': yt.title,
                'views': yt.views,
                'length': yt.length,
                'author': yt.author
            }
        except Exception as e:
            print("Error:", e)
    return render_template('stats.html', stats=video_stats)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    info = {}
    if request.method == 'POST':
        url = request.form.get('video_url')
        try:
            yt = YouTube(url)
            info = {
                'title': yt.title,
                'channel': yt.author,
                'publish_date': yt.publish_date,
                'length': yt.length,
                'views': yt.views,
                'description': yt.description[:300]  # First 300 chars
            }
        except Exception as e:
            print("Error:", e)
    return render_template('video_info.html', info=info)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about_site')
def about_site():
    return render_template('about_site.html')

@app.route('/what-is-tag')
def what_is_tag():
    return render_template('what-is-tag.html')

@app.route('/what-is-thumbnail')
def what_is_thumbnail():
    return render_template('what-is-thumbnail.html')

@app.route('/what-is-keyword')
def what_is_keyword():
    return render_template('what-is-keyword.html')
