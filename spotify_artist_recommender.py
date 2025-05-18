import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables
load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")


# Spotify authentication
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_related_artists(artist_name):
    """Fetch related artists for a given artist."""
    result = sp.search(q=artist_name, type='artist', limit=1)
    
    if result['artists']['items']:
        artist_id = result['artists']['items'][0]['id']
        try:
            related_artists = sp.artist_related_artists(artist_id)
            return [artist['name'] for artist in related_artists['artists']]
        except spotipy.exceptions.SpotifyException:
            return "Related artists not found or not available for this artist."
    else:
        return "Artist not found."

if __name__ == "__main__":
    artist_name = input("Enter artist name: ")
    similar_artists = get_related_artists(artist_name)
    print(f"Related artists for '{artist_name}': {similar_artists}")
