from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thumbnail')
def thumbnail():
    return render_template('thumbnail.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/what-is-tag')
def what_is_tag():
    return render_template('what_is_tag.html')

@app.route('/what-is-thumbnail')
def what_is_thumbnail():
    return render_template('what_is_thumbnail.html')

@app.route('/how-tags-help')
def how_tags_help():
    return render_template('how_tags_help.html')

@app.route('/what-is-keyword')
def what_is_keyword():
    return render_template('what_is_keyword.html')
