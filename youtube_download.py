import os
import sys
from pytube import YouTube


def download(key):
    vid = YouTube('https://www.youtube.com/watch?v=' + key)

    stream = vid.streams \
        .filter(type='audio') \
        .order_by('abr') \
        .asc() \
        .first()

    stream.download(filename=key, output_path='temp')

    return os.path.join('temp', key + '.' + stream.subtype)
