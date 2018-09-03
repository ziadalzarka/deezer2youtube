import os
from youtube_search import search
from youtube_download import download
from audio_convert import convert
from deezer_fetcher import list

list = list()

print 'Got a playlist of ' + str(len(list)) + ' songs.'

for song in list:
	print song.title + ' - ' + song.artist
	song.download('songs')