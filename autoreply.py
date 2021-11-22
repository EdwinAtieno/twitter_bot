import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

tweetNumber = 20
q = "MY SEARCH"
api = create_api()
tweets = list(tweepy.Cursor(api.search_tweets, q, tweet_mode='extended').items(tweetNumber))


def crashBot():
    for tweet in reversed(tweets):

        try:

            if q in tweet.full_text.lower():
                print(str(tweet.id) + '-' + tweet.full_text)
                api.update_status("@" + tweet.user.screen_name + " MY MESSAGE", tweet.id)
                api.retweet(tweet.id)
                print("done!")
                time.sleep(30)
        except tweepy.tweepyError as e:
            print(e.reason)
            time.sleep(30)


while True:
    crashBot()
    time.sleep(30)