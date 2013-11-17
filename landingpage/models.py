# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    SONG_SPEED = (
        (u'Wolna', u'Wolna '),
        (u'Średnia', u'Średnia '),
        (u'Szybka', u'Szybka '),
    )

    user = models.ForeignKey(User)
    artist = models.CharField(max_length=50)
    song_name = models.CharField(max_length=50)
    score_plus = models.IntegerField(default=0)
    score_minus = models.IntegerField(default=0)
    song_type = models.CharField(max_length=10, choices=SONG_SPEED)

    def score(self):
        return self.score_plus - self.score_minus


class SongVoted(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
