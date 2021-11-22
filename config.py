# tweepy-bots/bots/config.py
import tweepy
import logging
import secretskeys as sk


logger = logging.getLogger()


def create_api():
    auth = tweepy.OAuthHandler(sk.consumer_key, sk.consumer_secret)
    auth.set_access_token(sk.access_token, sk.access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    print("API created")

    return api
create_api()