from GetToken import GettingToken
from SpotipyAUTH import GetSpotipyAUTH
import json
import os

#You can use the method below as an alternative way to login.
#token = GettingToken()

#Here is the recommended way to login.
sp = GetSpotipyAUTH()

#You can set the artist ID in your .env file.
#Here's more information about the Spotify artist ID:
#https://developer.spotify.com/documentation/web-api/
artistID = os.getenv("ARTIST_ID")
Spotify_URI = 'spotify:artist:' + artistID
results = sp.artist_top_tracks(Spotify_URI)
print(json.dumps(results, indent=4, sort_keys=True))

#Print the top tracks of the artist along withe the audio, popularity, and cover art.
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('popularity    : ' + str(track['popularity']))
    print('cover art: ' + track['album']['images'][0]['url'])
print("")

#Get the related artists.
Spotify_URI = 'spotify:artist:' + artistID
results = sp.artist_related_artists(Spotify_URI)
print(json.dumps(results, indent=4, sort_keys=True))