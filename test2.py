import re
import io
import csv
import tweepy
from tweepy import OAuthHandler
#TextBlob perform simple natural language processing tasks.
#from textblob import TextBlob


consumer_key = 'aRLGzK3P3MWSz368Hwrn9KIP3'
consumer_secret = 'D5gWYq06j6C6M3Z0uHC54gMK3Ox6jxTxw3RpW2JaUrxmf6CxpH'
access_token = '766383287996645376-KMvy3Nug57h2upYAfm6z8DHvI5ZUSr6'
access_token_secret = 'PoX9jeJmQkjvANW11wgySY6ad1GgFXBqBSn0XL2jJiBww'

# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)




def get_tweets(query, count = 300):

    # empty list to store parsed tweets
    tweets = []
    target = io.open("mytweets.txt", 'w', encoding='utf-8')
    # call twitter api to fetch tweets
    q=str(query)
    a=str(q+" sarcasm")
    b=str(q+" sarcastic")
    c=str(q+" irony")
    fetched_tweets = api.search(a, count = count)+ api.search(b, count = count)+ api.search(c, count = count)
    # parsing tweets one by one
    print(len(fetched_tweets))

    for tweet in fetched_tweets:

        # empty dictionary to store required params of a tweet
        parsed_tweet = {}
        # saving text of tweet
        parsed_tweet['text'] = tweet.text
        if "http" not in tweet.text:
            line = re.sub("[^A-Za-z]", " ", tweet.text)
            target.write(line+"\n")
    return tweets

    # creating object of TwitterClient Class
    # calling function to get tweets
tweets = get_tweets(query ="", count = 20000)
