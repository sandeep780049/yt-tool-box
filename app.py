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
@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        topic = request.form['topic'].strip()
        if topic:
            base_keywords = [
                f"{topic} tips", f"{topic} tutorial", f"{topic} guide", f"{topic} SEO",
                f"{topic} 2025", f"best {topic}", f"{topic} strategy", f"{topic} explained",
                f"{topic} ideas", f"grow with {topic}", f"{topic} content", f"{topic} hacks",
                f"{topic} marketing", f"{topic} tools", f"{topic} for beginners"
            ]
            keywords = base_keywords[:15]
    return render_template('keywords.html', keywords=keywords)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    class DummyStats:
        def __init__(self, channel, subscribers, views):
            self.channel = channel
            self.subscribers = subscribers
            self.views = views

    stats = None
    if request.method == 'POST':
        channel_url = request.form['channel_url']
        # Dummy logic for now – you can later connect to YouTube API
        if channel_url:
            channel_name = channel_url.split("/")[-1] if "/" in channel_url else "Your Channel"
            stats = DummyStats(channel_name, "12.3K", "1.5M")
    return render_template('stats.html', stats=stats)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    title = None
    description = None
    if request.method == 'POST':
        topic = request.form['video_topic']
        if topic:
            title = f"{topic} - Must Watch in 2025!"
            description = (
                f"Discover everything about {topic}. This video covers tips, tricks, and the best ways to explore or understand {topic}. "
                f"Don’t forget to like, share, and subscribe for more amazing content!"
            )
    return render_template('ai.html', title=title, description=description)
