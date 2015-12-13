from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json, time, math, sys, os, re, operator
from nltk import pos_tag, word_tokenize
from urllib.request import urlopen

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
	    self.tag_type_list = ['DT','CC','CD','IN','JJ','JJR','JJS','PRP','PRP$','SYM','WP','WP$','WRB','WDT','UH','TO','PDT','POS','VBZ']
	    self.tag_words = {}
	def on_data(self, data):
	    tweet = json.loads(data)
	    self.tweets_data.append(tweet)
	    current_time = time.localtime(time.time())
	    time_diff = (time.mktime(current_time) - time.mktime(self.start_time)) / 60
	    if math.floor(time_diff) == 1:
	        tweets_data_list.append(tuple(self.tweets_data))
	        if self.count == 5:
	            self.last_five = 1
	        tweet_text = ""
	        if self.last_five == 1:
	        	for all_tweets in tweets_data_list :
	        		for tweets in all_tweets :
		        		screen_name = tweets['user']['screen_name']
		        		tweet_text += tweets['text']
		        		if screen_name in self.tweets_user : 
		        			self.tweets_user[screen_name] = int(self.tweets_user[screen_name]) + 1
		        		else:
		        			self.tweets_user[screen_name] = 1
	        	del( tweets_data_list[0])
	        else:
	        	for all_tweets in tweets_data_list:
	        		for tweets in all_tweets :
		        		screen_name = tweets['user']['screen_name']
		        		tweet_text += tweets['text']
		        		#print(tweet_text)
		        		if screen_name in self.tweets_user : 
		        			self.tweets_user[screen_name] = int(self.tweets_user[screen_name]) + 1
		        		else:
		        			self.tweets_user[screen_name] = 1
	        	self.count += 1
	        	#for sl in link_set:
	        		#slp = sl.encode("utf-8")
	        		#el = urlopen(sl)
	        		#print(el.url)
	        	#print(link_set)
	        self.start_time = time.localtime(time.time())
	        print("\n****Twitter's User with total number of tweets****")
	        for tu, tn in self.tweets_user.items():
	        	print(tu+" : "+ str(tn))
	        link_set = set(re.findall(r"https?://[^\s]+", tweet_text))
	        number_of_link = len(link_set)
	        tweet_text = re.sub(r"(https?://[^\s]+)|([^A-Za-z0-9]+)",' ',tweet_text)
	        #maximum noun and verb words included
	        print("\n****Total number of shared links in tweets***")
	        print(number_of_link)
	        text_token = word_tokenize(tweet_text)
	        pos_tag_list = pos_tag(text_token)
	        for tag_list in pos_tag_list:
	        	if tag_list[1] not in self.tag_type_list:
	        		if tag_list[0] in self.tag_words:
	        			self.tag_words[tag_list[0]] += 1
	        		else:
	        		 	self.tag_words[tag_list[0]] = 1
	        sorted_tag = sorted(self.tag_words.items(), key=operator.itemgetter(1),reverse = True)
	        c = 0
	        print('\n*****top ten used words in tweets*****')
	        for tag_list in sorted_tag:
	        	c += 1
	        	if len(tag_list[0]) > 1:
	        		print(tag_list[0]+" : "+ str(tag_list[1]))
	        	if c == 10:
	        		break;
	        self.tweets_user.clear()
	        self.tag_words.clear()
	        del(self.tweets_data[:])
	    return True

	def on_error(self, status):
	    print("Error occured" + str(status))

if __name__ == "__main__":
	try:
		stdl = StdOutListner()
		auth = OAuthHandler(api_key, api_secret_key)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, stdl)
		argstr = (sys.argv[1] if len(sys.argv) > 1 else "python")
		stream.filter(track=[argstr])
	except KeyboardInterrupt:
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)