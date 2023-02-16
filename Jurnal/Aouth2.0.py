import requests
from requests_oauth2client import *

token = "an_access_token"
resp = requests.get("https://my.protected.api/endpoint", auth=BearerAuth(token))
