from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tools = [
        {"name": "Thumbnail Downloader", "link": "/thumbnail", "description": "Download YouTube video thumbnails in high quality for your SEO and branding needs."},
        {"name": "Tag & Keyword Generator", "link": "/tags", "description": "Generate SEO-friendly tags and keywords to boost video discoverability and reach."},
        {"name": "Channel Stats Viewer", "link": "/stats", "description": "Check your channel metrics and track your growth over time."},
        {"name": "AI Title & Description Generator", "link": "/ai-title-description", "description": "Automatically generate attention-grabbing titles and optimized video descriptions."},
        {"name": "Video Info Viewer", "link": "/video_info", "description": "Get detailed metadata and info of any public YouTube video instantly."}
    ]
    return render_template('index.html', tools=tools)

# Add proper routes for all tools (you already have this part)
