import json
import urllib2
from song import song

api = "https://api.deezer.com/"
options = "?output=json&access_token="
access_token = "frLHKy5pwdlJOo6WOwIz71Qsg3l7zVCCl8FtMRMqKb3JzRYSoFl"


def construct_url(path, additional=""):
		return api + path + options + access_token + additional


def fetch(path, additional=""):
		response = urllib2.urlopen(construct_url(path, additional))
		data = response.read()
		return json.loads(data)


def find_loved_playlist(playlists):
		for playlist in playlists:
				if (playlist["is_loved_track"]):
						return playlist


def fetch_playlist_tracks_page(id, index):
		data = fetch('playlist/' + str(id), '&index=' + str(index))
		tracks = data["tracks"]["data"]
		return tracks


def fetch_playlist_tracks(playlist):
		playlist_id = playlist["id"]
		playlist_size = playlist["nb_tracks"]
		fetched_tracks = 0
		tracks = []

		while fetched_tracks < playlist_size:
				page = fetch_playlist_tracks_page(playlist_id, fetched_tracks)
				fetched_tracks += len(page)
				tracks += page

		return tracks


def list():
		playlists = fetch('user/me/playlists')["data"]
		loved = find_loved_playlist(playlists)
		tracks = fetch_playlist_tracks(loved)
		songs = []
		for track in tracks:
				songs.append(
						song(
								track["id"],
								track["title"],
								track["artist"]["name"],
								track["album"]["title"],
								# the method get is used to return None if there is no album cover
								track["album"].get("cover_big")
						)
				)
				pass

		return songs
