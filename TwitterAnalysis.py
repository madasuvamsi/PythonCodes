from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Twitter credentials to access Twitter API
access_token = "**********************************"
access_token_secret = "**********************"
consumer_key = "dfsdfsrvdsf"
consumer_secret = "dfsdfrsdfsrdv"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):#override the streaming.py on_data method
        print(data)
        return True

    def on_error(self, status):#override the streaming.py on_error method
        print(status)

if __name__ == '__main__':
    #Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'NewYork'
    stream.filter(track=['FinTech'])
