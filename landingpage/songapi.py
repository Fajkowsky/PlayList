from django.conf import settings

import json
import urllib2


def get_song_link(artist, title):
    link = 'http://tinysong.com/b/%s+%s?format=json&key=%s' % (
        artist, title, settings.TINYSONG_KEY)
    data = json.load(urllib2.urlopen(link))
    if data:
        return data['SongID']
    else:
        return "#"
