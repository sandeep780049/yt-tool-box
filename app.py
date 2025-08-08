from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = ""
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = video_url.split("v=")[-1].split("&")[0]
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        video_title = request.form['video_title']
        keywords = video_title.lower().split()
        tags = list(set(keywords))
    return render_template('tags.html', tags=tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        topic = request.form['topic']
        keywords = [f"{topic} tutorial", f"{topic} 2025", f"learn {topic} fast", f"best {topic} tricks"]
    return render_template('keywords.html', keywords=keywords)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    title = ""
    description = ""
    if request.method == 'POST':
        topic = request.form['topic']
        title = f"Top 10 Tips About {topic} You Should Know!"
        description = f"This video dives deep into {topic}, revealing essential tips, hacks, and insights to help you master it like a pro!"
    return render_template('ai.html', title=title, description=description)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    stats_data = {}
    if request.method == 'POST':
        channel_name = request.form['channel_name']
        stats_data = {
            "Channel Name": channel_name,
            "Subscribers": "1.2M",
            "Videos": "340",
            "Total Views": "78M"
        }
    return render_template('stats.html', stats_data=stats_data)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    video_info = {}
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_info = {
            "Title": "Sample Video Title",
            "Views": "123K",
            "Likes": "10K",
            "Comments": "500"
        }
    return render_template('video_info.html', video_info=video_info)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about_site')
def about_site():
    return render_template('about_site.html')
