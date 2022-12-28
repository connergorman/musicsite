from .models import Listen


def add_listen(cleaned_data: dict):
    """Takes the input from a track submission and stores it into the listening DB"""

    # artist, album, track, duration, date
    artist = cleaned_data['artist']
    album = cleaned_data['album']
    track = cleaned_data['track']
    dur_delta = cleaned_data['duration']
    dur_secs = dur_delta.total_seconds()
    date = cleaned_data['date'] 
    t = Listen(track_name=track, album_name=album, artist_name=artist, track_length=dur_secs, time_played=date)
    t.save()
    
