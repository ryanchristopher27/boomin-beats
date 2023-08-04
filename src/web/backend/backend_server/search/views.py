from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse

# Spotipy imports
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = 'a6e889c6521040a797bdda3dbb27b451'
CLIENT_SECRET = '77e4125490d5481bb89b5891dbb4458c'
REDIRECT_URI = 'https://example.com/callback'
SCOPE = 'user-library-read'

# $env:"credentials" SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

# import os
# client_secret = os.environ['SPOTIPY_CLIENT_SECRET']

def index(request):

    # scope = "user-library-read"

    searchValue = request.GET['searchValue']
    # print(searchValue)

    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPE)
    # sp = Spotify(client_credentials_manager=SpotifyClientCredentials())

    access_token_dict = sp_oauth.get_access_token()  
    access_token = access_token_dict['access_token']

    spotify_obj = Spotify(auth=access_token)

    # https://open.spotify.com/track/6wsqVwoiVH2kde4k4KKAFU?si=d69de43ef5344e96

    tracks = spotify_obj.search(q='track:'+searchValue)
    # print('Track', json.dumps(tracks, sort_keys=False, indent=4))

    searchSuggestionObjects = []
    for track in tracks['tracks']['items']:
        searchSuggestionObjects.append({
            'title': track['name'],
            'artists': [artist['name'] for artist in track['artists']],
            'id': track['id']
        })

    print(json.dumps(searchSuggestionObjects, sort_keys=False, indent=4))

    response = {
        'type': 'searchSongs',
        'tracks': searchSuggestionObjects,
    }

    # return HttpResponse(json.dumps(searchSuggestionObjects, sort_keys=False, indent=4))

    # Create a JsonResponse with the response data
    json_response = JsonResponse(response)

    # Set the CORS headers in the response
    json_response["Access-Control-Allow-Origin"] = "http://localhost:5173"  # Replace with your frontend URL
    json_response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    json_response["Access-Control-Allow-Headers"] = "Content-Type"
    json_response["Access-Control-Allow-Credentials"] = "true"

    return json_response

