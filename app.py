# app.py (Flask backend)

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Thumbnail Downloader
@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = extract_video_id(video_url)
        if video_id:
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

# Tag & Keyword Generator
@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        video_topic = request.form['video_topic']
        tags = generate_tags(video_topic)
    return render_template('tags.html', tags=tags)

# Channel Stats Viewer
@app.route('/stats')
def stats():
    return render_template('stats.html')

# AI Title & Description Generator
@app.route('/ai-generator', methods=['GET', 'POST'])
def ai_generator():
    title, description = '', ''
    if request.method == 'POST':
        topic = request.form['topic']
        title = f"🔥 {topic} - Must Watch!"
        description = f"This video is about {topic}. Watch till the end and don't forget to like & subscribe!"
    return render_template('ai_generator.html', title=title, description=description)

# Video Info Viewer
@app.route('/video-info')
def video_info():
    return render_template('video_info.html')

# Extra content pages
@app.route('/what-is-tag')
def what_is_tag():
    return render_template('what_is_tag.html')

@app.route('/what-is-keyword')
def what_is_keyword():
    return render_template('what_is_keyword.html')

@app.route('/grow-channel')
def grow_channel():
    return render_template('grow_channel.html')

@app.route('/about-site')
def about_site():
    return render_template('about_site.html')

# Helper functions
def extract_video_id(url):
    if 'v=' in url:
        return url.split('v=')[1].split('&')[0]
    elif 'youtu.be/' in url:
        return url.split('youtu.be/')[1].split('?')[0]
    return None

def generate_tags(topic):
    return [f"{topic} tips", f"{topic} 2025", f"best {topic}", f"{topic} in Hindi"]

# Note: No if __name__ block so it works on Render
