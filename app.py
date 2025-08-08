from flask import Flask, render_template, request
from pytube import YouTube
import openai
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        url = request.form['video_url']
        yt = YouTube(url)
        thumbnail_url = yt.thumbnail_url
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        url = request.form['video_url']
        yt = YouTube(url)
        tags = yt.keywords
    return render_template('tags.html', tags=tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        url = request.form['video_url']
        yt = YouTube(url)
        keywords = yt.keywords
    return render_template('keywords.html', keywords=keywords)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    stats = {}
    if request.method == 'POST':
        url = request.form['video_url']
        yt = YouTube(url)
        stats = {
            'title': yt.title,
            'views': yt.views,
            'length': yt.length,
            'author': yt.author
        }
    return render_template('stats.html', stats=stats)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    ai_result = ''
    if request.method == 'POST':
        topic = request.form['video_topic']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Generate an engaging YouTube title and description for: {topic}",
            max_tokens=100
        )
        ai_result = response.choices[0].text.strip()
    return render_template('ai.html', ai_result=ai_result)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    info = {}
    if request.method == 'POST':
        url = request.form['video_url']
        yt = YouTube(url)
        info = {
            'title': yt.title,
            'description': yt.description,
            'length': yt.length,
            'views': yt.views,
            'author': yt.author,
            'publish_date': yt.publish_date
        }
    return render_template('video_info.html', info=info)

# Static pages
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
