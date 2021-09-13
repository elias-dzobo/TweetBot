import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time

consumer_key = 'IjnmXY2vpjAJJek8dWM51YiHF'
consumer_secret = 'NP5985N98dy7AWqI0elUAnpHgRzKj9sGVki8qjnFnIqrlCUCx8'
access_token  = '948717579224473600-bRNh6cINiDp4sKIRX8Dip4LCJJF42di'
access_secret = 'P7JY1PIvEjYVB9fXSSYyP0HCkiWU37B7k91Ciz0f8nXZq'

start_time = time.time()
keyword_list = ['$btc', '$ada', '$matic', '$eth']


#create stream class
class MyListener(StreamListener):

    def __init__(self, start_time, time_limit = 60):
        self.time = start_time
        self.limit = time_limit

    def on_data(self, data):
        try:
            with open('ada.json', 'a') as f:
                while (time.time() - self.time) < self.limit:
                    f.write(data)
                    return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True




if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    twitter_stream = Stream(auth, MyListener(start_time, time_limit=60))
    twitter_stream.filter(track = keyword_list, languages=['en'])
