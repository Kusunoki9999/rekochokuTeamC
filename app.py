from flask import app, Flask, render_template, redirect, request, url_for, jsonify
from bff import json_manager
import json
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

#json_managerの動作確認用
@app.route("/jsontest")
def jsontest():
    return render_template('jsontest.html')

@app.route('/add_song', methods=['POST'])
def add_song():
    data = request.json
    playlist_id = str(data['playlist_id'])
    song_url = data['song_url']

    playlists = json_manager.add_song(playlist_id, song_url)
    return jsonify(playlists)

@app.route("/play")
def play():
    return render_template('play.html')

#YouTubeAPI
#video_idはURLから取得できるように修正
api_key = "AIzaSyBlE6mCVybHe-DhIf2hmPUxhoKK8zqk0QY"
video_id = "-NFhRWhkp7I"

def get_title(video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    video_title = response['items'][0]['snippet']['title']
    return video_title

if __name__ == "__main__":
    app.run(debug=True)