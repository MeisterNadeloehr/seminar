import tweepy
import csv
import pandas as pd
####input your credentials here
import xlsxwriter
import datetime

consumer_key = 'aRLGzK3P3MWSz368Hwrn9KIP3'
consumer_secret = 'D5gWYq06j6C6M3Z0uHC54gMK3Ox6jxTxw3RpW2JaUrxmf6CxpH'
access_token = '766383287996645376-KMvy3Nug57h2upYAfm6z8DHvI5ZUSr6'
access_token_secret = 'PoX9jeJmQkjvANW11wgySY6ad1GgFXBqBSn0XL2jJiBww'

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#%matplotlib inline


# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Return API with authentication:
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


# We create an extractor object:
extractor = twitter_setup()

# We create a tweet list as follows:
#tweets = extractor.user_timeline(screen_name="realDonaldTrump", count=200)


#for tweets in tweepy.Cursor(extractor.search, q = "nazis",
#                           lang="de",
#                           since="2018-12-04").items():
#    print(tweets.text)


#tweets = extractor.search(q = "nazis", count = 100)

#query = 'nazis'
#max_tweets = 1000
#tweets = [status for status in tweepy.Cursor(extractor.search, q=query).items(max_tweets)]

tweets = tweepy.Cursor(extractor.search, q = "reconquista germanica",
                           lang="de",
                           since="2017-12-12").items(100000)

data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# We add relevant data:
#data['len']  = np.array([len(tweet.text) for tweet in tweets])
#data['ID']   = np.array([tweet.id for tweet in tweets])
#data['Date'] = np.array([tweet.created_at for tweet in tweets])
#data['Source'] = np.array([tweet.source for tweet in tweets])
#data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
#data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])


#print("Number of tweets extracted: {}.\n".format(len(tweets)))

# Display of first 10 elements from dataframe:
display(data.head(10))


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('reconquista.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
data.to_excel(writer, sheet_name="sheet1")

# Close the Pandas Excel writer and output the Excel file.
writer.save()
