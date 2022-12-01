import tweepy
import configparser
import pandas as pd
import urllib.request
#import fyp

config = configparser.ConfigParser()
config.read('config.ini')

#get api keys and api secret key and access token and access token secret
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
authentication = tweepy.OAuth1UserHandler(api_key, api_key_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication)


queryTerm = "Dell Technologies"
public_tweets = api.search_tweets(q=queryTerm, lang = 'en', result_type = "mixed", count = "100")
columns = ['User' ,'Time', 'Tweet']
data = []

for tweet in public_tweets:
    data.append([tweet.user.screen_name, tweet.created_at, tweet.text, ])


dataframe = pd.DataFrame(data, columns=columns)
dataframe.to_json('tweets.json', orient='index')
print(dataframe)







