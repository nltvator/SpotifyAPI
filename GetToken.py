import requests
import os
from dotenv import load_dotenv
def GettingToken():

    load_dotenv()

    #You can login to Spotify using the alternative method below. 
    #However, I would recommend using the SpotipyAUTH package instead.

    clientID = os.environ.get('ClientID')
    clientSecret=os.environ.get('ClientSecret')

    auth_url = 'https://accounts.spotify.com/api/token'

    data = {
        'grant_type': 'client_credentials',
        'client_id': clientID,
        'client_secret': clientSecret,
    }
        
    auth_response = requests.post(auth_url, data=data)    
    access_token = auth_response.json().get('access_token')
    return access_token