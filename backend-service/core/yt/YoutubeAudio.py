from pytube import YouTube
import vlc
import time

LENGTH = 120


def play_youtube_video(video_url : str) -> None:
    """
    Accepts a youtube video url, gets the link for its audio stream and then uses vlc to play the audio upto the allowed length

    :Params
        video_url : str -> link for the youtube video
    """

    # Create a Youtube Object
    yt = YouTube(video_url)
    audio_stream = yt.streams.get_audio_only()
    play_video_from_link(audio_stream.url)


def play_video_from_link(video_link):
    try:
        # Create a VLC instance
        vlc_instance = vlc.Instance()

        # Create a media player
        media_player = vlc_instance.media_player_new()

        # Create a media from the video link
        media = vlc_instance.media_new(video_link)

        # Set the media for the media player
        media_player.set_media(media)
        start_time = time.time()
        media_player.play()

        # Wait for the player to finish playing
        while True:
            state = media_player.get_state()
            if (
                state == vlc.State.Ended
                or state == vlc.State.Error
                or time.time() >= start_time + LENGTH
            ):
                break

        # Release the media player and vlc instance
        media_player.release()
        vlc_instance.release()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    play_youtube_video("https://www.youtube.com/watch?v=UJeSWbR6W04")
