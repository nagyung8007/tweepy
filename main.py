import tweepy
from google.cloud import language_v1
import matplotlib.pyplot as plt
from pytwitter import Api

# OAuth 1.0A
# api = Api(bearer_token="1679322074089914369-tNyXw8A7nBTyxd7RRlneG2EvG4NBFv")

# OAuth2.0
api = Api(client_id="OWk1c2ZnbVFlR0ZUYWZJZ240YjU6MTpjaQ", oauth_flow=True)
# get the url and code verifier for user to authorize
url, code_verifier, _ = api.get_oauth2_authorize_url()
api.generate_oauth2_access_token("https://localhost/?state=state&code=code", code_verifier)
# copy the response url
