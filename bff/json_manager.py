import json
import os

# JSONファイルのパス
json_file_path = '/id_sheet.json'

def add_song_to_playlist(playlist_id, song_url):
    # JSONファイルを読み込む
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            playlists = json.load(f)
    else:
        playlists = {"playlists": {}}

    # プレイリストが存在する場合は曲を追加し、存在しない場合は新規作成
    if playlist_id in playlists['playlists']:
        playlists['playlists'][playlist_id]['songs'].append(song_url)
    else:
        playlists['playlists'][playlist_id] = {'songs': [song_url]}

    # JSONファイルに書き戻す
    with open(json_file_path, 'w') as f:
        json.dump(playlists, f, indent=4)

    return {'status': 'success', 'playlist_id': playlist_id, 'url': song_url}
