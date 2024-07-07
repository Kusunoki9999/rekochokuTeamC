document.getElementById('add-song-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const playlist_id = document.getElementById('playlist_id').value;
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
        // 曲が追加された後にリストを更新するコードをここに追加できます。
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
