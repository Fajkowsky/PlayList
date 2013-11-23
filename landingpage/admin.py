from django.contrib import admin
from models import Song, SongVoted


class SongAdmin(admin.ModelAdmin):
    list_display = ('user', 'artist', 'song_name', 'score_plus', 'score_minus')


class SongVotedAdmin(admin.ModelAdmin):
    list_display = ('user', 'song')

admin.site.register(SongVoted, SongVotedAdmin)
admin.site.register(Song, SongAdmin)
