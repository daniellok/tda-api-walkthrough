import requests
from urllib.parse import quote, unquote
import pickle

with open("auth_code.txt") as file:
    auth_code = unquote(file.read())

params = {
    "client_id" :  "CHEOK@AMER.OAUTHAP", 
    "redirect_uri" : "http://localhost", 
    "access_type"  : "offline", 
    "grant_type"   : "authorization_code", 
    "code"         : auth_code
    }

url = "https://api.tdameritrade.com/v1/oauth2/token"

response = requests.post(url, data=params)


with open("token.pickle", "wb") as pickle_test:
    pickle.dump(response.json(), pickle_test)