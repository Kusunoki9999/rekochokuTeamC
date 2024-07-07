// YouTube IFrame Player APIの準備ができたら呼ばれる関数
function onYouTubeIframeAPIReady() {
    // JSONファイルを取得
    fetch('../bff/id_sheet.json')
        .then(response => response.json())
        .then(data => {
            // プレイリストからYouTube動画IDを取得
            const playlistId = "1"; // プレイリストID
            const songs = data.playlists[playlistId].songs; //

            // YouTube動画IDを取得する関数
            function getYouTubeVideoId(url) {
                //const regExp = /^.*(youtu.be\/|v\/|\/u\/\w\/|embed\/|watch\?v=|\&v=|v=)([^#\&\?]*).*/;
                const regExp = /^.*(youtu.be\/)([^#\&\?]*).*/;
                const match = url.match(regExp);
                return (match && match[2].length == 11) ? match[2] : null;
            }

            // プレイリスト用の動画IDを配列にする
            const videoIds = songs.map(url => getYouTubeVideoId(url)).filter(id => id !== null);

            // YouTubeプレーヤーを作成
            const player = new YT.Player('player', {
                height: 500, //縦サイズ
                width: 10, //横サイズ
                videoId: videoIds[0],
                playerVars: {
                    'autoplay': 1, // 自動再生
                    'loop': 1,     // ループ再生
                    //'controls': 0, //コントロールバー非表示
                    'playlist': videoIds.join(','), // ループ再生に必要
                    'rel': 0
                },
                events: {
                    'onReady': onPlayerReady,
                    'onStateChange': onPlayerStateChange
                }
            });

            // プレーヤーが準備できた時に呼ばれる関数
            function onPlayerReady(event) {
                event.target.playVideo();
            }

            // プレーヤーの状態が変わった時に呼ばれる関数
            function onPlayerStateChange(event) {
                if (event.data === YT.PlayerState.ENDED) {
                    event.target.playVideo(); // 終了したら次の動画を再生
                }
            }
        })
        .catch(error => console.error('Error loading JSON:', error));
}
