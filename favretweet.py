import tweepy
from config import create_api
import json
import logging

logging.basicConfig(level=logging.info("test"))
logger= logging.getLogger()

class FavRetweetListener(tweepy.Stream):
    def __init__(self, api):
        self.api = api
        self.me = "eddymzae1"

    def on_status(self, tweet):
        logger.info("Processing tweet id {}".format("tweet.id"))
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.api.get_user(self.me):
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)
def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    main(["python developer"])