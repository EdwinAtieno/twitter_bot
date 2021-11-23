import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

tweetNumber = 20
q = "can we meet"
api = create_api()
since_id=1
tweets = list(tweepy.Cursor(api.search_tweets, q, tweet_mode='extended').items(tweetNumber)) and list(tweepy.Cursor(api.mentions_timeline, since_id=since_id).items())



def crashBot():
    for tweet in reversed(tweets):

        try:

            if q in tweet.text.lower():
                print(str(tweet.id) + '-' + tweet.text)
                api.update_status("@" + tweet.user.screen_name + "   Please DM me")
                api.retweet(tweet.id)
                tweet.favorite()
                print("done!")
                time.sleep(30)
        except tweepy.TweepyException as e:
            print(e)
            time.sleep(30)


while True:
    crashBot()
    time.sleep(30)