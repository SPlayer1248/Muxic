import datetime

from django.db import models


# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    album_date_release = models.DateField(max_length=100, default=datetime.date.today)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=500)
    song_logo = models.CharField(max_length=1000)
    song_date_release = models.DateField(max_length=100, default=datetime.date.today)

    def __str__(self):
        return self.artist + ' - ' + self.song_title
