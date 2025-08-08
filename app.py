from flask import Flask, render_template, request
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
        except:
            thumbnail_url = "Invalid or unsupported URL"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    video_tags = []
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        try:
            yt = YouTube(video_url)
            video_tags = yt.keywords
        except:
            video_tags = ["Could not fetch tags. Please check the URL."]
    return render_template('tags.html', tags=video_tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    video_keywords = []
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        try:
            yt = YouTube(video_url)
            video_keywords = yt.keywords
        except:
            video_keywords = ["Could not fetch keywords."]
    return render_template('keywords.html', keywords=video_keywords)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    info = {}
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        try:
            yt = YouTube(video_url)
            info = {
                'title': yt.title,
                'author': yt.author,
                'views': yt.views,
                'length': yt.length,
                'publish_date': yt.publish_date
            }
        except:
            info['error'] = "Unable to fetch video info."
    return render_template('video_info.html', info=info)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    title = ""
    description = ""
    if request.method == 'POST':
        topic = request.form.get('video_topic')
        if topic:
            title = f"🔥 {topic.title()} Explained in 2 Minutes!"
            description = f"Discover everything about {topic} in just 2 minutes. Stay tuned for quick tips, tricks, and valuable insights!"
    return render_template('ai.html', title=title, description=description)
