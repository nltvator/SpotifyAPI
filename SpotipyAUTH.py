import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def GetSpotipyAUTH():
    
    #The following function allows you to login using your client ID and secret.
    #If you don't have your Client ID and Secret you can get them here:
    #https://developer.spotify.com/dashboard/applications

    clientID = os.environ.get('CLIENT_ID')
    clientSecret=os.environ.get('CLIENT_SECRET')
    client_credentials_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    return sp