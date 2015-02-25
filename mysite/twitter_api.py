from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import json

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "ruYHp14Tx4YNp1Y7039hc9797"
CONSUMER_SECRET = "dDVhVTT101hnzNQDu20vVTRdT8czdXnvm1Qt0pT1SsjekkABEp"

OAUTH_TOKEN = "16479615-v8QuDKjf8Cohb928cOn6OYAanKS5MYXutXk1VX0OA"
OAUTH_TOKEN_SECRET = "1LaaBvhVvJa73NjAXYAWmRuShtulu30MTAF0WVvzWQjvm"


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
   
    oauth = get_oauth()
    r = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=1", auth=oauth)
    print r.json()[0]['user']['followers_count']