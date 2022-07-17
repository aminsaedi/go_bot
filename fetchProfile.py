from twitter import Twitter, OAuth
from io import BytesIO
import os
from pprint import pprint
import requests

token = os.environ['TOKEN']
token_secret = os.environ['TOKEN_SECRET']
consumer_key = os.environ['CONSUMER']
consumer_secret = os.environ['CONSUMER_SECRET']

t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))


def get_image_by_username(username):
    user = t.users.lookup(screen_name=username)
    url = user[0]['profile_image_url'].replace("_normal", "_400x400")
    response = requests.get(url)
    if (response.status_code == 200):
        return response.content
    return None
