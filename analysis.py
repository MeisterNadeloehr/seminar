import tweepy
import csv
import pandas as pd

####input your credentials here
consumer_key = 'aRLGzK3P3MWSz368Hwrn9KIP3'
consumer_secret = 'D5gWYq06j6C6M3Z0uHC54gMK3Ox6jxTxw3RpW2JaUrxmf6CxpH'
access_token = '766383287996645376-KMvy3Nug57h2upYAfm6z8DHvI5ZUSr6'
access_token_secret = 'PoX9jeJmQkjvANW11wgySY6ad1GgFXBqBSn0XL2jJiBww'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
# hier der name des output files
search_keyword = 'fluechtlinge'
csvFile = open(search_keyword + '.csv', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile)
csvWriter = csv.writer(csvFile, delimiter=' ')

# hier keywort, startdatum und sprache eingeben
for tweet in tweepy.Cursor(api.search,q = search_keyword,
                           lang="de",
                           since="2018-12-04").items():
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
