from __future__ import unicode_literals
from __future__ import print_function
import random
import string
import tweepy

# Twitter credentials
CONSUMER_KEY = 'vnhxBxEIQw3jjyBZxopDcGqLV'
CONSUMER_SECRET = 'aKzyrHML08eX9pz5pEc7pAUWGNlLXO8Fb4N6bTn3Jxrh0aIgjM'
ACCESS_TOKEN = '741350648164323328-Nu7pWdtFqEccRPiUDSiPmYGQoiYF78Z'
ACCESS_SECRET = 'KOeKaREqW1SZ37bvG7rdIY27KORkTDskdsAOO1aD2kp2e'


def send_tweet(text):
    # Add a random code at the end to prevent duplicate consecutive tweets.
    random_code_len = 10
    random_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random_code_len))
    text = text[:140 - random_code_len - 1] + ' ' + random_code

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # Tweet a line every hour
    api.update_status(text)


if __name__ == '__main__':
    send_tweet('Hello from python!')
