import os
import eyed3
import urllib2
from youtube_search import search
from youtube_download import download
from audio_convert import convert


class song:

    def __init__(self, trackid, title, artist, album, album_art_url):
        self.trackid = trackid
        self.title = title
        self.artist = artist
        self.album = album
        self.album_art_url = album_art_url

    def fetch_album_art(self):
        response = urllib2.urlopen(self.album_art_url)
        return response.read()

    def set_metadata(self, filename):
        file = eyed3.load(filename)
        file.tag.title = unicode(self.title)
        file.tag.album = unicode(self.album)
        file.tag.artist = unicode(self.artist)
        if (self.album_art_url):
            album_art = self.fetch_album_art()
            file.tag.images.set(3, album_art, "image/jpeg", u"Downloaded by YouTube Converter")
        file.tag.save()

    def construct_payload(self):
        return "{0} {1} audio".format(self.title, self.artist)

    def format_file_name(self):
        return "{0} - {1}.mp3".format(self.title, self.artist)

    def download(self, dir=""):
        payload = self.construct_payload()

        key = search(payload)

        unknown_audio = download(key)
        audiopath = convert(unknown_audio)

        os.remove(unknown_audio)
        self.set_metadata(audiopath)
        os.rename(audiopath, os.path.join(
            dir, self.format_file_name()))