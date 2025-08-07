from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        if "v=" in video_url:
            video_id = video_url.split("v=")[-1][:11]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("/")[-1][:11]
        else:
            video_id = video_url[:11]
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags_list = []
    if request.method == 'POST':
        topic = request.form['topic']
        tags_list = [f"{topic} tutorial", f"{topic} review", f"{topic} tips", f"{topic} for beginners", f"{topic} in 2025"]
    return render_template('tags.html', tags=tags_list)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords_list = []
    if request.method == 'POST':
        topic = request.form['topic']
        keywords_list = [f"best {topic}", f"{topic} explained", f"{topic} uses", f"{topic} benefits", f"why {topic} is important"]
    return render_template('keywords.html', keywords=keywords_list)

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    title, description = '', ''
    if request.method == 'POST':
        topic = request.form['topic']
        title = f"Top 5 Secrets About {topic} You Should Know"
        description = f"Learn everything about {topic}, its benefits, and tips to grow your channel using smart strategies."
    return render_template('ai.html', title=title, description=description)

# Informational pages
@app.route('/what-is-tags')
def what_is_tags():
    return render_template('what-is-tags.html')

@app.route('/what-is-thumbnails')
def what_is_thumbnails():
    return render_template('what-is-thumbnails.html')

@app.route('/what-is-keywords')
def what_is_keywords():
    return render_template('what-is-keywords.html')

@app.route('/about_site')
def about_site():
    return render_template('about_site.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')
