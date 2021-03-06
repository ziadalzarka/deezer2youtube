import os
import eyed3
import urllib.request
import urllib.error
import urllib.parse
import re
from youtube_search import search
from youtube_download import download
from audio_convert import convert


class song:
    def __init__(self, trackid, title, artist, album, album_art_url):
        self.trackid = trackid
        self.title = str(title)
        self.artist = str(artist)
        self.album = str(album)
        self.album_art_url = album_art_url

    def fetch_album_art(self):
        response = urllib.request.urlopen(self.album_art_url)
        return response.read()

    def set_metadata(self, filename):
        file = eyed3.load(filename)
        file.tag.title = self.title
        file.tag.album = self.album
        file.tag.artist = self.artist

        if (self.album_art_url):
            album_art = self.fetch_album_art()
            file.tag.images.set(3, album_art, "image/jpeg",
                                "Downloaded by YouTube Converter")
        file.tag.save()

    def construct_payload(self):
        return "{0} {1} audio".format(self.title, self.artist)

    def format_file_name(self):
        filename = "{0} - {1}.mp3".format(self.title, self.artist)
        return re.sub('\\?|\\\\|<|>|:|\\||/|\\*|"', '', filename)

    def download(self, dir=""):
        try:
            filename = os.path.join(dir, self.format_file_name())

            if (os.path.isfile(filename)):
                return

            payload = self.construct_payload()


            key = search(str(payload))

            unknown_audio = download(key)
            audiopath = convert(unknown_audio)

            os.remove(unknown_audio)
            self.set_metadata(audiopath)
            os.rename(audiopath, filename)
        except Exception as e:
            print(e)
            print("Failed to download {0} - {1}".format(
                self.title, self.artist))
