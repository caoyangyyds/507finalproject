from bs4 import BeautifulSoup
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

cid="fa2d0dca91814ec8b8f14bf49d02bc56"
secret="f580bdbfb7f04d35b0b6faccf55c5231"
auth_manager=SpotifyClientCredentials(client_id=cid,client_secret=secret)
sp=spotipy.Spotify(auth_manager=auth_manager)




name = "The weekend"
results = sp.search(q='artist:' + name, type='artist')
id = results['artists']['items'][0]['id']
the_week_url = f'spotify:artist:{id}'
the_week_results = sp.artist_top_tracks(the_week_url, country='US')
data_id = the_week_results['tracks'][0]['id']

the_week_analyst = sp.audio_features(data_id)
print(the_week_analyst)



#with open("test.json", "w") as write_file:
#    json.dump(the_week_results, write_file, indent=2)
#print(data_id)