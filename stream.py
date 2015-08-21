import time
import ast
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'm6GUDEF3MODZDgOviUGR68DLM'
csecret = 'LjLt31OrfU17sgWNJWm4CFgujtm7NqQXJaOwlmVUuB0xTsH9Iu'
atoken = '3433267936-Jmp8YGeqrK2LFlpOVpY5Nzzrflej7P9RFYo7m5V'
asecret = 'uDCTiswlOyKXZ3XOywd11mEQ97T1MeHxih7TeiW6s4cF2'

class listener(StreamListener):

	def on_data(self,data):
		tweet = data.split(',"text":"')[1].split('","source')[0]
		saveFile = open('twitDB.csv', 'a')
		saveFile.write(tweet)
		saveFile.write('\n')
		saveFile.close()
		print tweet
		return True


	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["arduino"])
