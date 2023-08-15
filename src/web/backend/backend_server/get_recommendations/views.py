from django.shortcuts import render
import json
from django.http import JsonResponse
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

    track_id = request.GET['trackId']
    number_of_songs = request.GET['numberOfSongs']

    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPE)
    # sp = Spotify(client_credentials_manager=SpotifyClientCredentials())

    access_token_dict = sp_oauth.get_access_token()  
    access_token = access_token_dict['access_token']

    spotify_obj = Spotify(auth=access_token)

    # https://open.spotify.com/track/6wsqVwoiVH2kde4k4KKAFU?si=d69de43ef5344e96

    # recommendatios_genres = spotify_obj.recommendation_genre_seeds()

    recommendations = spotify_obj.recommendations(seed_tracks=[track_id], limit=number_of_songs)
    # print('Track', json.dumps(tracks, sort_keys=False, indent=4))

    print(json.dumps(recommendations, sort_keys=False, indent=4))
    recommendationsObjects = []
    for track in recommendations['tracks']:
        recommendationsObjects.append({
            'title': track['name'],
            'artists': [artist['name'] for artist in track['artists']],
            'id': track['id'],
            'image': track['album']['images'][2]['url'],
            'image_size': track['album']['images'][2]['height'],
            'duration_ms': track['duration_ms'],
            'explicit': track['explicit'],
            'track_url': track['external_urls']['spotify'],
            'album': track['album']['name'],
        })

    # return HttpResponse(json.dumps(recommendations, sort_keys=False, indent=4))

    # print(json.dumps(recommendationsObjects, sort_keys=False, indent=4))
    response = {
        'type': 'recommendations',
        'tracks': recommendationsObjects,
    }

    # Create a JsonResponse with the response data
    json_response = JsonResponse(response)

    # Set the CORS headers in the response
    json_response["Access-Control-Allow-Origin"] = "http://localhost:5173"  # Replace with your frontend URL
    json_response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    json_response["Access-Control-Allow-Headers"] = "Content-Type"
    json_response["Access-Control-Allow-Credentials"] = "true"

    return json_response

