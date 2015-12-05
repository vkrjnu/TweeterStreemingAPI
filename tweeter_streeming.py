from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json, time, math

access_token = "388139836-nottn5MwhKBlf6cERn5R7PcRjVFfrzezGJW7h79f"
access_token_secret = "7aPwrTvgHOyhuCxZy1HNR7LgiBjdBqtHsae1mms00eTBi"
api_key = "0ccUnXhzrEd6edFkpxOWwV5SA"
api_secret_key = "OvV2CzLDdJtsIeelMiEJBcA7uSna9yimyY2JVeNJR10QybJ2Pr"

class StdOutListner(StreamListener):
	def __init__(self, api = None, fprefix = ''):
	    self.count = 1
	    self.start_time = time.localtime(time.time())
	    self.last_five = 0
	    self.tweets_data = []
	    self.tweets_data_list = []
	def on_data(self, data):
	    tweet = json.loads(data)
	    self.tweets_data.append(tweet['text'])
	    print(tweet['user']['name'])
	    current_time = time.localtime(time.time())
	    time_diff = (time.mktime(current_time) - time.mktime(self.start_time)) / 60
	    if math.floor(time_diff) == 1:
	        self.tweets_data_list.append(self.tweets_data)
	        print(len(self.tweets_data))
	        print("\n\n")
	        if self.count == 5:
	            self.last_five = 1
	        if self.last_five == 1:
	        	print(self.tweets_data_list)
	        	del( self.tweets_data_list[0] )
	        else:
	        	print(self.tweets_data_list)
	        	self.count += 1
	        self.start_time = time.localtime(time.time())
	        del(self.tweets_data[:])
	    return True
	def on_error(self, status):
	    print("stoped")
if __name__ == "__main__":
	stdl = StdOutListner()
	auth = OAuthHandler(api_key, api_secret_key)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, stdl)
	stream.filter(track=['python'])

