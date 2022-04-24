from GetToken import GettingToken
from SpotipyAUTH import GetSpotipyAUTH
import json
import os
#token = GettingToken()
sp = GetSpotipyAUTH()

artistID = os.getenv("ARTIST_ID")
Spotify_URI = 'spotify:artist:' + artistID
results = sp.artist_top_tracks(Spotify_URI)
print(json.dumps(results, indent=4, sort_keys=True))
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('popularity    : ' + str(track['popularity']))
    print('cover art: ' + track['album']['images'][0]['url'])
print("")