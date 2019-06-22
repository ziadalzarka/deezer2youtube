import os
from youtube_search import search
from youtube_download import download
from audio_convert import convert
from deezer_fetcher import list
import json

list = list()
list.reverse()

print('Got a playlist of ', len(list), ' songs.')

for song in list:
	print(song.title + ' - ' + song.artist)
	song.download('songs')