import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def GetSpotipyAUTH():

    clientID = os.environ.get('CLIENT_ID')
    clientSecret=os.environ.get('CLIENT_SECRET')
    client_credentials_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    return sp