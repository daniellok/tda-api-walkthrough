import requests
from urllib.parse import quote, unquote
import pickle

params = {
    "client_id" :  "CHEOK@AMER.OAUTHAP", 
    "redirect_uri" : "http://localhost", 
    "access_type"  : "offline", 
    "grant_type"   : "authorization_code", 
    "code"         :  read `auth_code.txt` and URL-decode it.
    }

response = requests.post(url, data=params, headers=headers)

