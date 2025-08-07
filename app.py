from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/thumbnail')
def thumbnail():
  return render_template('thumbnail.html')

@app.route('/stats')
def stats():
  return render_template('stats.html')

@app.route('/ai-title-description')
def ai_title():
  return render_template('ai_title.html')

@app.route('/faq')
def faq():
  return render_template('faq.html')

@app.route('/what-is-tag') 
def what_is_tag(): 
  return render_template('what_is_tag.html')

@app.route('/what-is-thumbnail') 
def what_is_thumbnail():
  return render_template('what_is_thumbnail.html')

@app.route('/about-site')
def about_site():
  return render_template('about_site.html')



