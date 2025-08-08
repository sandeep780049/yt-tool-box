from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dummy AI generation for Titles, Descriptions, Tags, Keywords
def generate_titles(topic):
    return [f"Catchy Title {i+1} for {topic}" for i in range(10)]

def generate_description(topic):
    return f"This is a detailed and SEO-optimized description about {topic}. It will help your video rank higher and reach a wider audience. Always include the main topic, related terms, and a clear summary of what the video is about. Hashtags and timestamps also improve engagement."

def generate_tags(topic):
    return [f"{topic} Tag {i+1}" for i in range(10)]

def generate_keywords(topic):
    return [f"{topic} Keyword {i+1}" for i in range(25)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        if 'v=' in video_url:
            video_id = video_url.split('v=')[-1][:11]
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        topic = request.form['video_topic']
        tags = generate_tags(topic)
    return render_template('tags.html', tags=tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        topic = request.form['video_topic']
        keywords = generate_keywords(topic)
    return render_template('keywords.html', keywords=keywords)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    titles = []
    description = ""
    if request.method == 'POST':
        topic = request.form['video_topic']
        titles = generate_titles(topic)
        description = generate_description(topic)
    return render_template('ai.html', titles=titles, description=description)

@app.route('/what-is-tag')
def what_is_tag():
    return render_template('what-is-tag.html')

@app.route('/what-is-thumbnail')
def what_is_thumbnail():
    return render_template('what-is-thumbnail.html')

@app.route('/what-is-keyword')
def what_is_keyword():
    return render_template('what-is-keyword.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about-site')
def about_site():
    return render_template('about_site.html')
