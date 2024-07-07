document.getElementById('add-song-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const playlist_id = '1'; // プレイリストIDをここに設定
    const song_url = document.getElementById('song_url').value;

    fetch('/add_song', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ playlist_id, url: song_url })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Song added:', data);
        if (data.status === 'success') {
            addSongToList(song_url);
        } else {
            console.error('Error:', data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function addSongToList(song_url) {
    const songList = document.getElementById('song-list');

    const li = document.createElement('li');
    li.classList.add('song-item');

    const songInfo = document.createElement('div');
    songInfo.classList.add('song-info');
    songInfo.textContent = song_url;

    li.appendChild(songInfo);
    songList.appendChild(li);
}

