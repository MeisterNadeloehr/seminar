# -*- coding: utf-8 -*-
import os, sys
import tweepy
import csv
import pandas as pd
####input your credentials here

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
from wordcloud import WordCloud
import nltk


liste = [
'Hera22112013',
'IsidorMeyer1',
'Chasty_t',
'JaNuWatn',
'sandmango2005',
'mona_rumpel',
'LC180666',
'fop4651',
'chris_p79',
'uwebecher',
'Ayse_0815',
'MyCodeOfConduct',
'X9donernesto',
'blaupfeil',
'Renft1964',
'Grazywalking',
'FvdMosselaar',
'cornelia_cagol',
'Boelscheline',
'kchak79',
'KarlHalasz',
'DeutscherMiche5',
'NightRalph',
'safe_ID35',
'FalkRodig',
'HamburgerDeern4',
'StolzesVolk',
'Logiker01',
'NationalerBoy14',
'wakeupinfo',
'HeidiHofer06',
'BERLINER1404',
'dfoqF5yazTb1YI3',
'hdiesterweg',
'Mica4711',
'FiveFaker',
'morawnski',
'KimmyBertsch',
'SigfriedArthur',
'dgsportler',
'DKekser',
'MichaelSellne11',
'MadDocFoster',
'richito81',
'G0RI1982',
'Vergesslichr',
'Silgetown',
'tueringi24972',
'hh119933',
'AnchardAran',
'gruenebanane1',
'Urleere',
'AvalancheGerman',
'Chreuper',
'Deutscher_17',
'DeutscheFarben',
'Sachsen_17',
'g_oschi',
'JustAnotherReco',
'MicKurti',
'AbdulMansoor01',
'Der_Erzgebirger',
'homemimy',
'BjrnHansen18',
'77abraxas77',
'jesper_vangroot',
'PaulAbr89089961',
'PeterWitzbold',
'MalWieder_real',
'Deutschland_17'
]


#corp = nltk.corpus.ConllCorpusReader('.', 'tiger_release_aug07.corrected.16012013.conll09',
#                                     ['ignore', 'words', 'ignore', 'ignore', 'pos'],
#                                     encoding='utf-8')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
extractor = tweepy.API(auth,wait_on_rate_limit = True)
w = ""
w2 = ""
w3 = ""


#riesige for-schleife
for dudes in liste:

    tweets = extractor.user_timeline(screen_name = dudes, count="200", tweet_mode="extended")
    print("-----\n\n")
    print("USER: "+ dudes)

    print("-----\n\n")

    # We create a pandas dataframe as follows:
    data = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['Tweets'])

    # We add relevant data:
    data['len']  = np.array([len(tweet.full_text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])


    # We obtain all possible sources:
    sources = []
    for source in data['Source']:
        if source not in sources:
            sources.append(source)

    # We create a numpy vector mapped to labels:
    percent = np.zeros(len(sources))

    for source in data['Source']:
        for index in range(len(sources)):
            if source == sources[index]:
                percent[index] += 1
                pass

    percent /= 100

    #from textblob import TextBlob
    from textblob_de import TextBlobDE as TextBlob
    import re

    def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analize_sentiment(tweet):
        analysis = TextBlob(clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1


    # We create a column with the result of the analysis:
    data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])

    # We display the updated dataframe with the new column:
    #display(data.head(10))


    # We construct lists with classified tweets:
    pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]


    # We print percentages:
    #print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
    #print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
    #print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))


    data2 = pd.DataFrame()

    d = [[dudes, format(len(tweets)), format(len(pos_tweets)*100/len(data['Tweets'])), format(len(neu_tweets)*100/len(data['Tweets'])), format(len(neg_tweets)*100/len(data['Tweets'])) ]]
    df = pd.DataFrame(d)
    #data2.append(data)
    data.to_csv('tweets_reconquista.csv', header=False, encoding='utf-8', mode='a')
    df.to_csv('sentiment_reconquista.csv', header=False, encoding='utf-8', mode='a')


    #wenn der user mehr als 20 Prozent negative tweets hat, füge seine tweets in die analyse für wordcloud hinzu
    if(format(len(pos_tweets)*100/len(data['Tweets']))>20):
        w += data.to_string(columns = ['Tweets'])

    #wenn der user mehr als 20 Prozent positive tweets hat, füge seine tweets in die analyse für wordcloud hinzu
    if(format(len(neg_tweets)*100/len(data['Tweets']))>20):
        w2 += data.to_string(columns = ['Tweets'])

    #gesamt wordcloud
    w3 += data.to_string(columns = ['Tweets'])

    print("-------------")
    #print("USER: "+ dudes + " FINISHED")
    #print("-------------")

    print("\n\n")

print("---------------------------------")
print("Everything written successfully!")

from nltk.corpus import stopwords
stopset = stopwords.words('german')
stopset += stopwords.words('english')
stopset += ["account", "withheld", "temporarily", "Tweet", "unavailable", "Tweets", "people", "followed", "unfollowed", "unav"] #ohne 'leere' Tweets
stopset += ["Ja", "Nein", "ganz", "Guten"]

#retweets entfernen
cleaned_string = " ".join([word for word in w.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

cleaned_string2 = " ".join([word for word in w2.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])
cleaned_string3 = " ".join([word for word in w3.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])


w_1=""
w_2=""
w_3=""

for word,pos in (TextBlob(cleaned_string).pos_tags):
        if (pos[0] == 'N'):
             w_1+=word + " "

for word,pos in (TextBlob(cleaned_string2).pos_tags):
        if (pos[0] == 'N'):
             w_2+=word + " "


for word,pos in (TextBlob(cleaned_string3).pos_tags):
        if (pos[0] == 'N'):
             w_3+=word + " "


wordcloud = WordCloud(stopwords=stopset, background_color='white', width=1800, height=1400).generate(w_1)

wordcloud_2 = WordCloud(stopwords=stopset, background_color='white', width=1800, height=1400).generate(w_2)

wordcloud_3 = WordCloud(stopwords=stopset, background_color='white', width=1800, height=1400).generate(w_3)



plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('twitter_wordcloud_neg_nomen_reconquista.png', dpi=300)
plt.show()


plt.imshow(wordcloud_2)
plt.axis('off')
plt.savefig('twitter_wordcloud_pos_nomen_reconquista.png', dpi=300)
plt.show()


plt.imshow(wordcloud_3)
plt.axis('off')
plt.savefig('twitter_wordcloud_gesamt_nomen_reconquista.png', dpi=300)
plt.show()
