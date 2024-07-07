from flask import app, Flask, render_template, redirect, request, url_for, jsonify
from bff import json_manager
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/playlist")
def playlist():
    return render_template('playlist.html')

@app.route("/search")
def search():
    return render_template('search.html')

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

if __name__ == "__main__":
    app.run(debug=True)