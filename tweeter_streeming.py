from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "388139836-nottn5MwhKBlf6cERn5R7PcRjVFfrzezGJW7h79f"
access_token_secret = "7aPwrTvgHOyhuCxZy1HNR7LgiBjdBqtHsae1mms00eTBi"
api_key = "0ccUnXhzrEd6edFkpxOWwV5SA"
api_secret_key = "OvV2CzLDdJtsIeelMiEJBcA7uSna9yimyY2JVeNJR10QybJ2Pr"

class StdOutListner(StreamListener):
	def on_data(self, data):
	    print(data)
	    return True
	def on_error(self, status):
	    print(status)
if __name__ == "__main__":
	stdl = StdOutListner()
	auth = OAuthHandler(api_key, api_secret_key)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, stdl)
	stream.filter(track=['python','ruby'])


