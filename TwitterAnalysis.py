from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Twitter credentials to access Twitter API
access_token = "389306455-ET1qXls7J3WupRbgB5NgiiUbhT0v3zFYVzEorBIj"
access_token_secret = "vq1jhdrYOVESGz6WbtGEYtvjwv0l3rhx0f50eG7ZSQTWd"
consumer_key = "HvMWSOaHYKuo2zbpYPZQSYvDW"
consumer_secret = "au52kuDnnIkVeItSk0qMyTyzOrkRKU8nnskgCNFDgBrSyfKG7E"

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
