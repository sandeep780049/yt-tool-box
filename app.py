from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = extract_video_id(video_url)
        if video_id:
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags_list = []
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = extract_video_id(video_url)
        if video_id:
            tags_list = [
                "YouTube", "Viral", "Subscribe", "Tutorial", "2025", 
                "Tips", "Channel Growth", "Shorts", "Content", 
                "YouTuber", "Trending", "Boost Views", "SEO", "Guide",
                "Likes", "Engagement", "Watch Time", "Niche", "Editing", "Monetize"
            ]
    return render_template('tags.html', tags=tags_list)
