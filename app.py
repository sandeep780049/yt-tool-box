from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Load your OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    tags = []
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if video_url:
            # Extract video title (simulate basic topic extraction)
            topic = extract_topic_from_url(video_url)
            prompt = f"Generate 25 relevant YouTube tags for a video about: {topic}"
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=200
                )
                ai_tags = response.choices[0].message.content
                tags = ai_tags.strip().split(",")  # AI response is comma-separated
                tags = [t.strip() for t in tags if t.strip()]
            except Exception as e:
                tags = [f"Error generating tags: {str(e)}"]
    return render_template('tags.html', tags=tags)

def extract_topic_from_url(url):
    # Basic fallback if no real metadata API is used
    return "the topic of the YouTube video pasted here"

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    titles = []
    description = ""
    if request.method == 'POST':
        topic = request.form.get('video_topic')
        if topic:
            try:
                title_prompt = f"Generate 10 catchy YouTube titles for: {topic}"
                description_prompt = f"Write a large and SEO-friendly YouTube video description for: {topic}"

                title_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": title_prompt}],
                    max_tokens=300
                )
                desc_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": description_prompt}],
                    max_tokens=400
                )

                titles = title_response.choices[0].message.content.strip().split("\n")
                titles = [t.strip("-•123. ") for t in titles if t.strip()]
                description = desc_response.choices[0].message.content.strip()

            except Exception as e:
                titles = [f"Error: {str(e)}"]
                description = "Something went wrong."
    return render_template('ai.html', titles=titles, description=description)

