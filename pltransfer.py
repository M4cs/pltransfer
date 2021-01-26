import plistlib, json
import requests
import tqdm
import time

config = {
    "spotify_auth_token": "YOUR_AUTH_TOKEN",
}

def create_query(entry):
    keys = [ 'name', 'artist', 'album']
    query = "?type=track&q="
    for key in keys:
        query += (entry.get(key) if entry.get(key) else '') + "+"
    return query

def likesong(song_ids):
    song_lists = []
    songs = []
    song_ids.reverse()
    for song in song_ids:
        if len(songs) == 50:
            song_lists.append(songs)
            songs = []
        songs.append(song)
    if len(songs) > 0:
        song_lists.append(songs)
    sesh = requests.session()
    for sids in song_lists:
        res = sesh.put('https://api.spotify.com/v1/me/tracks',
        data=json.dumps({
            'ids': sids
        }),
        headers={
            'Authorization': 'Bearer ' + config['spotify_auth_token']
        })
        if res.status_code == 401:
            print('You need a new access_token!')
            return None
        if res.status_code == 200:
            print("Added 50 Songs to Liked Songs")
        else:
            print('Failed to add another 50 songs to Liked Songs')
        time.sleep(3)

def search_song(entry):
    sesh = requests.session()
    res = sesh.get('https://api.spotify.com/v1/search' + create_query(entry),
    headers = {
        'Authorization': 'Bearer ' + config['spotify_auth_token']
    })
    if res.status_code == 401:
        print('You need a new access_token!')
        return None
    if res.json():
        data = res.json()
        return data

with open('Library.xml', 'rb') as f:
    plist = plistlib.load(f)

song_list = []

index = 0
for k, v in plist['Tracks'].items():
    artist = v.get('Artist')
    name = v.get('Name')
    album = v.get('Album')
    song_list.append({'artist': artist, 'name': name, 'album': album})
    if not artist or not name or not album:
        index += 1

song_ids_to_like = []
for track in song_list:
    response = search_song(track)
    if response.get('tracks'):
        if response['tracks'].get('items'):
            if len(response['tracks']['items']) > 0:
                song_ids_to_like.append(response['tracks']['items'][0]['id'])                                                                                                                        

likesong(song_ids_to_like)