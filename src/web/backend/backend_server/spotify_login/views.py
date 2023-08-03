from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Spotipy imports
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'a6e889c6521040a797bdda3dbb27b451'
CLIENT_SECRET = '77e4125490d5481bb89b5891dbb4458c'
REDIRECT_URI = 'https://example.com/callback'
SCOPE = 'user-library-read'

def index(request):

    scope = "user-library-read"

    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)

    sp = spotipy.Spotify(auth_manager=sp_oauth)

    results = sp.current_user_saved_tracks()

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " - ", track['name'])

    return HttpResponse("Hello, world. You're at the polls index.")

