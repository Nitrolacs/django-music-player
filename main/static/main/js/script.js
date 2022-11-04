const player = document.querySelector('.audio-player')
const play = document.querySelector('.play-track')
const prev = document.querySelector('.prev-track')
const next = document.querySelector('.next-track')
const duration = document.querySelector('.total_duration')
const currentTime = document.querySelector('.current-time')
const progress = document.querySelector('.slider')
const progress_container = document.querySelector('.bar')
const play_button = document.querySelector('.play_btn')
const progress_line = document.querySelector('.fill')
const audio_tracks = document.querySelector('.songs')
const song_title = document.querySelector('.songname')
const artist = document.querySelector('.songauthor')
const playlist_name = document.querySelector('.playlistname')
const music_img = document.querySelector('.music_cover')
const plst_cover = document.querySelector('.music_cover_plst')

// init music indexing
let compositionIndex = 0

// functions
const setSRC = () => {
    player.src = MEDIA_URL + '/' + musics[compositionIndex].audio_file
    song_title.textContent = musics[compositionIndex].title
    artist.textContent = musics[compositionIndex].artist
    music_img.setAttribute('src', MEDIA_URL + '/' + musics[compositionIndex].cover_image)
    playlist_name.textContent = musics[compositionIndex].playlist__name
    plst_cover.setAttribute('src', MEDIA_URL + '/' + musics[compositionIndex].playlist__cover_image)
}

const playOrPause = () => {
    if (player.paused) {
        play_button.src = pause_route
        player.play()
    } else {
        play_button.src = play_route
        player.pause()
    }
}

const formatTime = (secs) => {
    let min = Math.floor((secs % 3600) / 60)
    let sec = Math.floor(secs % 60)
    if (sec < 10) {
        sec = `0${sec}`
    }
    return `${min}:${sec}`
}

// load music on refresh
setSRC()
player.pause()

// when play is clicked
play.addEventListener('click', () => {
    playOrPause()
})

// load duration of music for UI
player.addEventListener('loadedmetadata', () => {
    duration.textContent = formatTime(player.duration)
})

// update progress bar
player.addEventListener('timeupdate', () => {
    let sec = player.currentTime
    let total = player.duration
    let audio_played = Math.round((sec / total) * 100)
    currentTime.textContent = formatTime(player.currentTime)
    progress_line.style.width = `${audio_played}%`
    progress.value = audio_played

    if (sec === total) {
        compositionIndex = compositionIndex + 1

        if (compositionIndex > musics.length - 1) {
            compositionIndex = 0
        }
        setSRC()
        playOrPause()
    }
})

// when prev btn is clicked
prev.addEventListener('click', () => {
    compositionIndex = compositionIndex - 1
    if (compositionIndex < 0) {
        compositionIndex = musics.length - 1
    }
    setSRC()
    playOrPause()
})

// when next btn is clicked
next.addEventListener('click', () => {
    compositionIndex = compositionIndex + 1
    if (compositionIndex > musics.length - 1) {
        compositionIndex = 0
    }
    setSRC()
    playOrPause()
})

// update progress bar on click
progress.addEventListener('click', e => {
    const clicked_percentage = (e.offsetX / progress_container.offsetWidth) * 100
    const audio_played = (clicked_percentage / 100) * player.duration
    let playing
    if (player.paused) {
        playing = false
    } else {
        playing = true
    }

    player.currentTime = audio_played
    if (playing === false) {
        play_button.src = pause_route
        player.play()
    }
})

audio_tracks.addEventListener('click', e => {
    if (e.target.className === 'play_img') {
        let parent_cont

        if (e.target.nodeName === 'div') {
            parent_cont = e.target.parentNode
        } else {
            parent_cont = e.target.parentNode.parentNode
        }

        const newIndex = Array.from(audio_tracks.querySelectorAll('li')).indexOf(parent_cont)

        if (newIndex === compositionIndex) {
            playOrPause()
        } else {
            compositionIndex = newIndex
            setSRC()
            play_button.src = pause_route
            player.play()
        }
    }
})