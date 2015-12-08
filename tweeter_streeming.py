from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json, time, math

access_token = "388139836-nottn5MwhKBlf6cERn5R7PcRjVFfrzezGJW7h79f"
access_token_secret = "7aPwrTvgHOyhuCxZy1HNR7LgiBjdBqtHsae1mms00eTBi"
api_key = "0ccUnXhzrEd6edFkpxOWwV5SA"
api_secret_key = "OvV2CzLDdJtsIeelMiEJBcA7uSna9yimyY2JVeNJR10QybJ2Pr"
tweets_data_list = []
class StdOutListner(StreamListener):
	def __init__(self):
	    self.count = 1
	    self.start_time = time.localtime(time.time())
	    self.last_five = 0
	    self.tweets_data = []
	    self.tweets_user = {}
	def on_data(self, data):
	    tweet = json.loads(data)
	    self.tweets_data.append(tweet)
	    current_time = time.localtime(time.time())
	    time_diff = (time.mktime(current_time) - time.mktime(self.start_time)) / 60
	    if time_diff > 0:
	        tweets_data_list.append(tuple(self.tweets_data))
	        #print(tweets_data_list)
	        if self.count == 5:
	            self.last_five = 1
	        if self.last_five == 1:
	        	for all_tweets in tweets_data_list :
	        		for tweets in all_tweets :
		        		screen_name = tweets['user']['screen_name']
		        		if screen_name in self.tweets_user : 
		        			self.tweets_user[screen_name] = int(self.tweets_user[screen_name]) + 1
		        		else:
		        			self.tweets_user[screen_name] = 1
	        	del( tweets_data_list[0])
	        else:
	        	for all_tweets in tweets_data_list:
	        		for tweets in all_tweets :
		        		screen_name = tweets['user']['screen_name']
		        		if screen_name in self.tweets_user : 
		        			self.tweets_user[screen_name] = int(self.tweets_user[screen_name]) + 1
		        		else:
		        			self.tweets_user[screen_name] = 1
	        	self.count += 1
	        self.start_time = time.localtime(time.time())
	        print(self.tweets_user)
	        self.tweets_user.clear()
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