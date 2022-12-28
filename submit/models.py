from django.db import models
import datetime as dt


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=200)
    album_artist = models.CharField(max_length=200)
    num_tracks = models.IntegerField(default=0)
    
    def __str__(self):
        reply = "{artist} - {album}"
        return reply.format(artist = self.album_artist, album = self.album_name)

class Artist(models.Model):
    arist_name = models.CharField(max_length=200)

    def __str__(self):
        return self.artist_name

class Track(models.Model):
    track_name = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    track_length = models.IntegerField(default=0)

    def __str__(self):
        reply = "{track} - {artist} ({album})"
        return reply.format(track = self.track_name, artist = self.artist_name, album = self.album_name)

class Listen(models.Model):
    track_name = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    track_length = models.IntegerField(default=0)
    time_played = models.DateTimeField(default=dt.datetime.now, blank=True)
    def __str__(self):
        reply = "{time}: {track} - {artist} ({album})"
        return reply.format(time = self.time_played.strftime('%m/%d/%y %H:%M'), track = self.track_name, artist = self.artist_name, album = self.album_name)

