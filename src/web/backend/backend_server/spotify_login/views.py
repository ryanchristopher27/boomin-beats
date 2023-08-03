from django.shortcuts import render

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

def index(request):

    scope = "user-library-read"

    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    # sp = Spotify(client_credentials_manager=SpotifyClientCredentials())

    # access_token = sp_oauth.get_access_token()  

    # sp = Spotify(auth_manager=sp_oauth)

    # https://open.spotify.com/track/6wsqVwoiVH2kde4k4KKAFU?si=d69de43ef5344e96

    # track = sp.search(q='track:I Know?')
    # print('Track', track)

    # results = sp.current_user_saved_tracks()

    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     print(idx, track['ar tists'][0]['name'], " - ", track['name'])

    return HttpResponse("Done")

