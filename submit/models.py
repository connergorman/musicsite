from django.db import models
import datetime as dt


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Track(models.Model):
    track_name = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    track_length = models.IntegerField(default=0)

    def __str__(self):
        reply = "{track} - {artist} ({album})"
        return reply.format(track=self.track_name, artist=self.artist.name, album=self.album_name)

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track)
    def __str__(self):
        reply = "{artist} - {album}"
        return reply.format(artist=self.artist.name, album=self.album_name)



class Listen(models.Model):
    track_name = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    track_length = models.IntegerField(default=0)
    time_played = models.DateTimeField(default=dt.datetime.now, blank=True)

    def __str__(self):
        reply = "{time}: {track} - {artist} ({album})"
        return reply.format(time=self.time_played.strftime('%m/%d/%y %H:%M'), track=self.track_name, artist=self.artist_name, album=self.album_name)
