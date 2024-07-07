import json
import os


JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), 'id_sheet.json')

# 読み込み
def load_json():
    with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)

# 書き込み
def save_json(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def add_song(playlist_id, song_url):

    playlists = load_json()

    # プレイリストのチェック
    if playlist_id not in playlists['playlists']:
        playlists['playlists'][playlist_id] = {
            "songs": []
        }

    # 曲の追加
    playlists['playlists'][playlist_id]['songs'].append(song_url)
    save_json(playlists)

    return playlists
