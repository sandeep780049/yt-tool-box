from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/thumbnail", methods=["GET", "POST"])
def thumbnail():
    if request.method == "POST":
        video_url = request.form["video_url"]
        return render_template("thumbnail.html", thumbnail_url=video_url)
    return render_template("thumbnail.html")

@app.route("/tags", methods=["GET", "POST"])
def tags():
    if request.method == "POST":
        video_title = request.form["video_title"]
        tags = [f"{video_title} Tag 1", f"{video_title} Tag 2", f"{video_title} Tag 3"]
        return render_template("tags.html", tags=tags)
    return render_template("tags.html")

@app.route("/keywords", methods=["GET", "POST"])
def keywords():
    if request.method == "POST":
        topic = request.form["topic"]
        keywords = [f"{topic} Keyword 1", f"{topic} Keyword 2", f"{topic} Keyword 3"]
        return render_template("keywords.html", keywords=keywords)
    return render_template("keywords.html")

@app.route("/stats", methods=["GET", "POST"])
def stats():
    if request.method == "POST":
        channel_name = request.form["channel_name"]
        stats = {"Subscribers": "1.2M", "Views": "100M", "Videos": "150"}
        return render_template("stats.html", stats=stats)
    return render_template("stats.html")

@app.route("/ai", methods=["GET", "POST"])
def ai():
    if request.method == "POST":
        topic = request.form["topic"]
        title = f"Best Title for {topic}"
        description = f"This is an SEO friendly description for {topic}."
        return render_template("ai.html", title=title, description=description)
    return render_template("ai.html")

@app.route("/video_info", methods=["GET", "POST"])
def video_info():
    if request.method == "POST":
        video_url = request.form["video_url"]
        info = {"Title": "Sample Video", "Views": "1M", "Likes": "50K"}
        return render_template("video_info.html", info=info)
    return render_template("video_info.html")

@app.route("/about_site")
def about_site():
    return render_template("about_site.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/what-is-keyword")
def what_is_keyword():
    return render_template("what-is-keyword.html")

@app.route("/what-is-tag")
def what_is_tag():
    return render_template("what-is-tag.html")

@app.route("/what-is-thumbnail")
def what_is_thumbnail():
    return render_template("what-is-thumbnail.html")
