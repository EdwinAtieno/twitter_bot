import seen as seen
import tweepy
import time
import logging

from config import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

tweetNumber = 20
q = "MY SEARCH"
api= create_api()

def crashBot():
    for tweet in reversed(tweets):

        try:
            if tweet.id in seen:
                print("Skipping", tweet.id, "because we already replied to it")
                continue
            if q in tweet.full_text.lower():
                seen.add(tweet.id)

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
    tweets = list(tweepy.Cursor(api.search, q, tweet_mode='extended').items(tweetNumber))
    crashBot()
    time.sleep(30)

    import tweepy
    import logging
    from config import create_api
    import time
    import seen as seen

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()


    def check_mentions(api, keywords, since_id):
        logger.info("Retrieving mentions")
        new_since_id = since_id
        for tweet in tweepy.Cursor(api.mentions_timeline,
                                   since_id=since_id).items():
            new_since_id = max(tweet.id, new_since_id)

            if tweet.in_reply_to_status_id is not None:
                continue
            if any(keyword in tweet.text.lower() for keyword in keywords):
                logger.info(f"Answering to {tweet.user.name}")

                if not tweet.user.following:
                    tweet.user.follow()
                sn = tweet.user.screen_name
                m = "Please reach us via DM" % (sn)
                api.update_status(m, tweet.id)

        return new_since_id


    def main():
        api = create_api()
        since_id = 1
        while True:
            since_id = check_mentions(api, ["help", "support"], since_id)
            logger.info("Waiting...")
            time.sleep(60)


    if __name__ == "__main__":
        main()