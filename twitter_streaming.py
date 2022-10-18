# https://github.com/skathirmani/data-scraping

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import os
import glob

consumer_key = "eVazopG0C6MPuJruABnb9Ojuo"
consumer_secret = "bRDPy1fV5ROPG5t5bCFtNxyAzbhMqUOz6aLsnhfLpmxUh3SJHs"

access_token = "873805520112459776-R8U5mUVRSs8hnXHYukrvtPe2crmSa7b"
access_token_secret = "7qq4TUEeimDlV3KfFPDp2gq030ECb7UnckpcLKuN3mD3j"


class StdOutListener(StreamListener):

    def on_data(self, data):
        print('----')
        tweet = json.loads(data)
        tweet_df = pd.DataFrame({
            'user_name': [tweet['user']['name']],
            'user_handler': [tweet['user']['screen_name']],
            'text':[tweet['text']],
            'created_at':[tweet['created_at']],
            'user_location':[tweet['user']['location']],
            'source':[tweet['source']]
            
        })
        file_name = 'tweets_datascience.csv'
        file_cwd = glob.glob('*.csv')
        print(os.getcwd())
        if file_name in file_cwd:
               with open(file_name, 'a') as f:
                    print('appending')
                    try:
                        tweet_df.to_csv(f, index=False, header=False)
                    except UnicodeEncodeError: 
                        pass
        
        else:
            print('creating a file')
            
            try:
                tweet_df.to_csv(file_name,index=False,encoding='utf-8')
            except UnicodeEncodeError:
                pass
        
        
        
        
        

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['#TuesdayThoughts'])