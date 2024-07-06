from flask import Flask, request, jsonify
import json

app = Flask(__name__)
json_file_path = 'id_sheet.json'

def main():
    f = open('id_sheet.json','r')
    json_data = json.load(f)

# 読み込み
def load_json():
    with open(json_file_path, 'r') as file:
        return json.load(file)

# 書き込み
def save_json(data):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/add_song', methods=['POST'])
def add_song():
    data = request.json
    playlist_id = str(data['playlist_id'])
    song_url = data['song_url']

    playlists = load_json()

    # playlistのチェック
    if playlist_id not in playlists['playlists']:
        playlists['playlists'][playlist_id] = {
            "songs": []
        }

    playlists['playlists'][playlist_id]['songs'].append(song_url)

    save_json(playlists)

    return jsonify(playlists)

if __name__ == '__main__':
    app.run(debug=True)

    