
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "4f889d3712204ce6be8552ef6c5615d6"
client_secret = "90d4d256e0ea4a83a3ff604f3350c701"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

for artist_id in [
    "4gzpq5DPGxSnKTe4SA8HAU",  # Coldplay
    "06HL4z0CvFAxyc27GXpf02",  # Taylor Swift
    "6eUKZXaKkcviH0Ku9w2n3V"   # Ed Sheeran
]:
    print(f"\nTrying artist ID: {artist_id}")
    try:
        related = sp.artist_related_artists(artist_id)
        print(f"Related artists for {artist_id}: {[a['name'] for a in related['artists']]}")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API error for {artist_id}: {e}")

