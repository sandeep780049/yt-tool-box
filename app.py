from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    return render_template('thumbnail.html')

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    return render_template('tags.html')

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    return render_template('keywords.html')

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    return render_template('ai.html')

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    return render_template('stats.html')

@app.route('/video_info', methods=['GET', 'POST'])
def video_info():
    return render_template('video_info.html')

@app.route('/what-is-tag')
def what_is_tag():
    return render_template('what-is-tag.html')

@app.route('/what-is-thumbnail')
def what_is_thumbnail():
    return render_template('what-is-thumbnail.html')

@app.route('/what-is-keyword')
def what_is_keyword():
    return render_template('what-is-keyword.html')

@app.route('/about-site')
def about_site():
    return render_template('about_site.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')
