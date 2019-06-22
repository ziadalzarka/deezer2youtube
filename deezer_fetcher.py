import json
import urllib.request
import urllib.error
import urllib.parse
from song import song

api = "https://api.deezer.com/"
options = "?output=json&access_token="
access_token = "frUCqaVZ4ZiWHyu82MCGALNUojKeOu3d9NsOdUqwj9pl0RgHTv8"


def construct_url(path, additional=""):
    return api + path + options + access_token + additional


def fetch(path, additional=""):
    response = urllib.request.urlopen(construct_url(path, additional))
    data = response.read().decode('utf-8')
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


def dump_json(tracks):
    with open('songs_backup.json', 'w') as outfile:
        json.dump(tracks, outfile)


def offline_tracks():
    with open('songs.json', 'r') as infile:
        return json.load(infile)


def list():
    # tracks = offline_tracks()

    playlists = fetch('user/me/playlists')["data"]
    loved = find_loved_playlist(playlists)
    tracks = fetch_playlist_tracks(loved)

    songs = []

    dump_json(tracks)


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
