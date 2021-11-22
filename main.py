from config import create_api
import tweepy
import secretskeys as sk
class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)

api = create_api()
printer = IDPrinter(
    sk.consumer_key, sk.consumer_secret,
    sk.access_token, sk.access_token_secret
)
printer.sample()