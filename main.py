import requests
import os
import json
from dotenv import load_dotenv
    
load_dotenv()

response = requests.get('https://api.spotify.com/v1/albums/id/1vCWHaC5f2uS3yhpwWbIA6')
json_response =  json.loads(response.text)
print(json_response)
print()