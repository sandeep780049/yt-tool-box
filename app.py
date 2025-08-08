from flask import Flask, render_template, request
import re

app = Flask(__name__)

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = extract_video_id(video_url)
        if video_id:
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = extract_video_id(video_url)
        if video_id:
            tags = [f"tag{i}" for i in range(1, 11)]
    return render_template('tags.html', tags=tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        topic = request.form['topic']
        if topic:
            keywords = [f"{topic} tutorial", f"{topic} in 2025", f"{topic} tips", f"{topic} guide"]
    return render_template('keywords.html', keywords=keywords)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    title = ""
    description = ""
    if request.method == 'POST':
        topic = request.form['topic']
        if topic:
            title = f"Top 5 {topic} Tips You Must Know in 2025!"
            description = f"Discover the latest strategies on {topic}. Boost your YouTube success with these effective methods. Don’t miss out!"
    return render_template('ai.html', title=title, description=description)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    stats_data = {}
    if request.method == 'POST':
        channel_url = request.form['channel_url']
        if channel_url:
            stats_data = {
                'subscribers': '10.5K',
                'videos': '152',
                'views': '1.2M',
                'created': 'Jan 2020'
            }
    return render_template('stats.html', stats_data=stats_data)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    info = {}
    if request.method == 'POST':
        video_url = request.form['video_url']
        if video_url:
            info = {
                'title': 'Sample Video Title',
                'description': 'This is a sample video description.',
                'channel': 'Sample Channel',
                'publish_date': '2025-01-01'
            }
    return render_template('video_info.html', info=info)

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
