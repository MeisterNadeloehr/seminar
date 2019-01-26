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


liste = [
'gergrubi',
'klausmeier0104',
'rantanplan1412',
#'kekistani1',
'evelix26',
'hessenbursche',
'JuttaMBrandt',
'geli9001',
'C_Sidorow',
'godefroy99',
'Gekko125',
'WeLoveHaram',
'fragichmich',
'Oedoen1523AD',
'leaks_nsu',
'Segeltexter',
'Gabelzaehler',
'this_one_world',
'Luicifer6',
'verusoss1',
'herr_helmut',
'nunu_balloon',
'WalkofLife66',
'Dieter_Stein',
'derKongoMueller',
'lossorg',
'winston_groovy',
'neander777',
'ThomasVerheugen',
'Koppschuettla',
'hohlraumsausen',
'Cimbasi',
'Steuerzahler01',
'anrefi',
'Sk4nd41',
'hetzpetz',
'Udai23517958',
'OKnauer',
'M_T_Franz',
'DieBajuwaren',
'demokratiedoc',
'freddynasevoll',
'Newsboy1899',
'Leopoldinjo',
'LSteinwandter',
'vzuschauer',
'lawracks',
'Yorck_',
'knaagi',
'Andy_Sch16',
'FreiesNetz88',
'AndrewRoussak',
'2018_AfDwaehlen',
'Dieaak',
'ainyrockstar',
'fernetpunker',
'krainde',
'Rockopornero',
'Kybeline',
'HermannMaier23',
'mywordsrmessage',
'schottenhaml',
'leopoldnikon',
'heutesnow',
'laurin15320',
'OppressedFart',
'DirkHafermann',
'katorin_jou',
'Msteinlin',
'waszumelden',
'wendt_joachim',
'gegenUmvolkung',
'peppermind',
'Zaretten',
'VPfafenrot',
'euroztar',
'twittschler',
'_deus_lo_vult',
'tschrammen',
'Epithelgewebe',
'DerLiuhvan',
'SoBitte',
'BarbaraKube',
'rwschmidt1',
'Twente_Chris',
'SarraKowsky',
'Ralf41996825',
'FreavonWegen',
'RiRotb',
'dima973',
'WolfHansen',
'ossi1232',
'Mo190311',
'FriedrichsErbe',
'KoppReport',
'Schwaebli1',
'Folienschnitzer',
'gellis18',
'nveritatis',
'JuliaMertensJM',
'Ich2ES',
'mic_eff',
'Franz_Ohse',
'krokotasche',
'DeplorableJp',
'HagenSon_71',
'DMittelhesse',
'MattFK',
'bruchhof66',
'Anne_Zielisch',
'dadeldi',
'fepBWm',
'FreeWorldOne',
'jato122',
'eckicgn',
'kuechenbulle72',
'schlusselszene',
'PaulSchneider72',
'LucaHuerlimann',
'Regenbeobachter',
'White_Haven',
'xEasyx',
'maxfcbayern1996',
'eurogegner',
'BestBidderGi',
'DrThomasBruns',
'Thueringen_',
'UweSchulz4',
'Boeses_Schaf',
'merdeux_',
'IllyrioM',
'Jacobus_Liftus',
'Der_Berzel',
'KarlSchneider1',
'Kaffee_Racer',
'MagenheimE',
'peterroger17',
'AB_National',
'gordon_deitrich',
'kommentator1234',
'Identitaere_B',
'OneStepBayond',
'dtpmaker',
'Ey_Jackson',
'Jack_Ewiehose',
'timonisch',
'tantegerd1',
'AlteElster',
'Torti_N',
'Junta2Puschkin',
'Berapaula1960',
'KlausSchaper',
'dimetrodon109',
'mortalhope1',
'myFavoriteKraut'
]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
extractor = tweepy.API(auth,wait_on_rate_limit = True)


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
    display(data.head(10))


    # We construct lists with classified tweets:
    pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]


    # We print percentages:
    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))


    data2 = pd.DataFrame()

    d = [[dudes, format(len(tweets)), format(len(pos_tweets)*100/len(data['Tweets'])), format(len(neu_tweets)*100/len(data['Tweets'])), format(len(neg_tweets)*100/len(data['Tweets'])) ]]
    df = pd.DataFrame(d)
    #data2.append(data)
    data.to_csv('erste_150_8.csv', header=False, encoding='utf-8', mode='a')
    df.to_csv('erste_150_8_sentiment.csv', header=False, encoding='utf-8', mode='a')

    print("-------------")
    print("USER: "+ dudes + " FINISHED")
    print("-------------")

    print("\n\n")


print("---------------------------------")
print("Everything written successfully!")
