from flask import app, Flask, render_template, redirect, request, url_for
from googleapiclient.discovery import build

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/playlist")
def playlist():
    video_title = get_title(video_id)
    return render_template('playlist.html', video_title=video_title)

@app.route("/play")
def play():
    return render_template('play.html')

#YouTubeAPI
#video_idはURLから取得できるように修正
api_key = ""
video_id = "-NFhRWhkp7I"

def get_title(video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    video_title = response['items'][0]['snippet']['title']
    return video_title

if __name__ == "__main__":
    app.run()