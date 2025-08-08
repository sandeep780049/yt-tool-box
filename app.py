from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = video_url.split("v=")[-1].split("&")[0]
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        return render_template('thumbnail.html', thumbnail_url=thumbnail_url)
    return render_template('thumbnail.html')

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        video_title = request.form['video_title']
        tags = [video_title.strip().replace(" ", "_") + suffix for suffix in ['_2025', '_yt', '_growth']]
    return render_template('tags.html', tags=tags)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        topic = request.form['topic']
        keywords = [topic + k for k in [' tips', ' 2025', ' hacks']]
    return render_template('keywords.html', keywords=keywords)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    channel_name = ''
    stats_data = {}
    if request.method == 'POST':
        channel_name = request.form['channel_name']
        stats_data = {
            'Subscribers': '1.2M',
            'Views': '34M',
            'Videos': '215'
        }
    return render_template('stats.html', channel_name=channel_name, stats=stats_data)

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    title = ''
    description = ''
    if request.method == 'POST':
        topic = request.form['topic']
        title = f"Top 5 Tips for {topic}"
        description = f"In this video, we explore the best tips for {topic} to boost your skills."
    return render_template('ai.html', title=title, description=description)

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    video_data = {}
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_data = {
            'Title': 'Sample Video Title',
            'Views': '1.5M',
            'Likes': '120K',
            'Comments': '4K'
        }
    return render_template('video_info.html', video_data=video_data)

# Content/SEO pages
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
