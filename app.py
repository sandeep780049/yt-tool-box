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
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            thumbnail_url = yt.thumbnail_url
        except Exception as e:
            thumbnail_url = f"Error: {str(e)}"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            tags = yt.keywords
        except Exception as e:
            tags = [f"Error: {str(e)}"]
    return render_template('tags.html', tags=tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        topic = request.form['topic']
        # Simple mock keyword generator
        keywords = [f"{topic} tutorial", f"{topic} in 2025", f"{topic} for beginners", f"{topic} tricks", f"{topic} explained"]
    return render_template('keywords.html', keywords=keywords)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    title = ''
    description = ''
    if request.method == 'POST':
        topic = request.form['topic']
        title = f"Top 5 Tips About {topic} You Need To Know!"
        description = f"In this video, we dive deep into {topic}, revealing tips and strategies to help you grow your YouTube channel."
    return render_template('ai.html', title=title, description=description)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    channel_name = ''
    stats_data = {}
    if request.method == 'POST':
        channel_name = request.form['channel_name']
        # Mock data
        stats_data = {
            'Subscribers': '1.2M',
            'Total Views': '55M',
            'Videos': '240',
            'Country': 'India'
        }
    return render_template('stats.html', stats_data=stats_data, channel_name=channel_name)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    video_data = {}
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            video_data = {
                'title': yt.title,
                'author': yt.author,
                'length': yt.length,
                'views': yt.views,
                'publish_date': yt.publish_date,
                'description': yt.description[:500] + '...'
            }
        except Exception as e:
            video_data = {'error': str(e)}
    return render_template('video_info.html', video_data=video_data)

# Static pages
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


# No __main__ block as per Render requirement
