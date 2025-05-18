import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if not client_id or not client_secret:
    raise ValueError("Please set the SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables.")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_related_artists(artist_name):
    result = sp.search(q=artist_name, type='artist', limit=1)
    
    if result['artists']['items']:
        artist_id = result['artists']['items'][0]['id']
        try:
            related_artists = sp.artist_related_artists(artist_id)
            return [artist['name'] for artist in related_artists['artists']]
        except spotipy.exceptions.SpotifyException as e:
            print(f"Error fetching related artists: {e}")
            return []
    else:
        return "Artist not found."



artist_name = "The weeknd"
similar_artists = get_related_artists(artist_name)
print(similar_artists)
