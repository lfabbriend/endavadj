import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials.client_id, client_secret= credentials.client_secret, redirect_uri=credentials.redirect_uri, scope=credentials.scope))
results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])