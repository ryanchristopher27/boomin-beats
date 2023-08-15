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
REDIRECT_URI = 'http://localhost:5173/profile'
SCOPE = 'user-library-read'

# $env:"credentials" SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

# import os
# client_secret = os.environ['SPOTIPY_CLIENT_SECRET']

def index(request):

    # scope = "user-library-read"


    access_token = request.GET['access_token']

    # sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
    #                         client_secret=CLIENT_SECRET,
    #                         redirect_uri=REDIRECT_URI,
    #                         scope=SCOPE)

    # access_token_dict = sp_oauth.get_access_token()  
    # access_token = access_token_dict['access_token']

    spotify_obj = Spotify(auth=access_token)

    current_user = spotify_obj.current_user()


    print(json.dumps(current_user, sort_keys=False, indent=4))

    response = {
        'type': 'get_profile',
        'profile': current_user,
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

