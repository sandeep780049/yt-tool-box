from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

# HOME ROUTE
@app.route('/')
def index():
    return render_template('index.html')

# THUMBNAIL DOWNLOADER
@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = ''
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            thumbnail_url = yt.thumbnail_url
        except:
            thumbnail_url = 'Error: Invalid YouTube URL'
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

# TAG GENERATOR
@app.route('/tag', methods=['GET', 'POST'])
def tag():
    tags = ''
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            tags = ', '.join(yt.keywords)
        except:
            tags = 'Error: Unable to fetch tags'
    return render_template('tag.html', tags=tags)

# KEYWORD GENERATOR
@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = ''
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            keywords = ', '.join(YouTube(video_url).keywords)
        except:
            keywords = 'Error: Unable to fetch keywords'
    return render_template('keywords.html', keywords=keywords)

# AI TITLE & DESCRIPTION GENERATOR
@app.route('/ai', methods=['GET', 'POST'])
def ai():
    ai_title = ''
    ai_description = ''
    if request.method == 'POST':
        topic = request.form['topic']
        ai_title = f"Top 10 Secrets About {topic} You Didn't Know!"
        ai_description = f"Discover amazing facts and tips about {topic} that will help grow your channel. Don't miss out on this powerful knowledge."
    return render_template('ai.html', ai_title=ai_title, ai_description=ai_description)

# STATS VIEWER
@app.route('/stats', methods=['GET', 'POST'])
def stats():
    title = ''
    views = ''
    channel = ''
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            title = yt.title
            views = yt.views
            channel = yt.author
        except:
            title = 'Error: Invalid URL'
    return render_template('stats.html', title=title, views=views, channel=channel)

# VIDEO INFO VIEWER
@app.route('/videoinfo', methods=['GET', 'POST'])
def videoinfo():
    title = ''
    length = ''
    publish = ''
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            title = yt.title
            length = yt.length
            publish = yt.publish_date.strftime('%Y-%m-%d')
        except:
            title = 'Error fetching data'
    return render_template('videoinfo.html', title=title, length=length, publish=publish)

# STATIC PAGES
@app.route('/about_site')
def about():
    return render_template('about_site.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/what-is-tags')
def what_is_tags():
    return render_template('what-is-tags.html')

@app.route('/what-is-thumbnails')
def what_is_thumbnails():
    return render_template('what-is-thumbnails.html')

@app.route('/what-is-keyword')
def what_is_keywords():
    return render_template('what-is-keyword.html')

# RENDER DEPLOYMENT ENTRY POINT
# No need for if __name__ == '__main__':
