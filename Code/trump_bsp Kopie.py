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


# API's setup:

#def twitter_setup():
    # Authentication and access using keys:
#    auth.set_access_token(access_token, access_token_secret)
 #   api = tweepy.API(auth,wait_on_rate_limit=True)
    # Return API with authentication:
  #  api = tweepy.API(auth)
   # return api


#nicht mehr aktiv: 'darksideofkek', 'ValdoreJavorsky', 'hetzegegenhetze',
liste = ['Deutscher_17', 'Itschi1', 'Lepanto_', 'Luisa_Maletzki', 'kevin_hevin_21', 'gerlex', 'EldonNick', 'Wilhelm_Koerner', 'aka_Ganymed', 'phalanx_europa',
         'ruhr_area51',  'Rosskar1',  '_enochwasright',  'Theodoretiker', 'realNEWZBLOG',  'McTabbish', 'supermampf',
         'RMichael2000', 'kekdich', 'JustAnotherReco', 'AbdelMusuf', 'NicolasCarnot', 'enythen', 'BerlinerBaerRG', 'politoreality', 'Gefr_Molinarius', 'Chreuper',
         'Jeb_Ident', 'asorent', 'trueY4K', 'michranspatz', 'MerkelFan666', 'TeutemanTuts', 'SeppDahte', 'LordZentrum', 'TheDefi4nt', 'HeiligeRevolte',
         'Der_Schweizer2', 'Paganaer', 'vonosterhal', 'LangeRII', 'MilaSuperstar33', 'franziskam108', 'PepeBismarck', 'LudwigErhard2', 'Urleere', 'NorikNordlicht',
         'koeterrasse', 'analogsubground', 'Morpheus_1984','Silgetown','mick_denis','LuetzowsJagd','Robert30521605','Metadiskurs1','DerNervenarzt','Rheinpfeil67',
         'ChocolaRei', 'ald3rs0n', 'Fatima_Najar', 'VisithorQ', 'BerundoKun', 'Stefan_RW84', 'E_Fall_Planer', 'algo1988', 'daAlt30', 'Tiuri1983',
         'dgsportler', 'Widerstand3', 'realPeterV', 'de_ewake', 'IdentitarianL', 'EdlervonBert', 'QubitusQ', 'ChrissoJacobsen', '1407jule', 'martinh84804324',
         'johannburkard', 'RGLarp12', 'Johann_Weiler', 'AnonymforFredom', 'alphablut', 'MartinNeubaue10', 'er1k_w', 'Aufklrer1', 'Potentialwirbel', 'einsmannimmond',
         'Kek_von_D', 'grimm_grimm1', 'Svenja012', 'KimmyBertsch', 'MalWieder_real', 'MaxPan21064515', 'DonElvetos', 'PaulAbr89089961', 'AlbertDenilzer', 'Muhamed_al_afre'    #100
         ]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
extractor = tweepy.API(auth,wait_on_rate_limit = True)


#for dudes in liste:
#    print(dudes)
#    test = extractor.lookup_users(screen_names=liste)
#    print(test)

#print("LENGTH:")
#print(len(test))

#data2 = pd.DataFrame(columns=['Tweets', 'len', 'ID', 'Date', 'Source', 'Likes', 'RT'])
#df = pd.DataFrame({'A' : [np.nan]})

zweiteliste=[]

for x in liste:
    try:
        u=api.get_user(x)
        print (u.screen_name)
        zweiteliste.append(x)
    except Exception:
            pass




#riesige for-schleife
for dudes in zweiteliste:
    #We create a tweet list as follows:
    #tweets = extractor.user_timeline(screen_name="realDonaldTrump", count="10000")
    tweets = extractor.user_timeline(screen_name =dudes, count="200")
    print("-----\n\n")
    print("USER: "+ dudes)
    print("-----\n\n")
    print("Number of tweets extracted: {}.\n".format(len(tweets)))

    # We print the most recent 5 tweets:
    print("5 recent tweets:\n")
    for tweet in tweets[:5]:
        print(tweet.text)
        print()

    # We create a pandas dataframe as follows:
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

    # We display the first 10 elements of the dataframe:
    # display(data.head(10))

    # We add relevant data:
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])

    # Display of first 10 elements from dataframe:
    # display(data.head(10))


    # We extract the mean of lenghts:
    mean = np.mean(data['len'])

    # print("The lenght's average in tweets: {}".format(mean))


    # We extract the tweet with more FAVs and more RTs:
    fav_max = np.max(data['Likes'])
    rt_max  = np.max(data['RTs'])

    fav = data[data.Likes == fav_max].index[0]
    rt  = data[data.RTs == rt_max].index[0]

    # Max FAVs:
    #print("The tweet with more likes is: \n{}".format(data['Tweets'][fav]))
    # print("Number of likes: {}".format(fav_max))
    # print("{} characters.\n".format(data['len'][fav]))

    # Max RTs:
    #print("The tweet with more retweets is: \n{}".format(data['Tweets'][rt]))
    #print("Number of retweets: {}".format(rt_max))
    #print("{} characters.\n".format(data['len'][rt]))

    # We create time series for data:

    tlen = pd.Series(data=data['len'].values, index=data['Date'])
    tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])

    # Lenghts along time:
    tlen.plot(figsize=(16,4), color='r');

    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True);

    # We obtain all possible sources:
    sources = []
    for source in data['Source']:
        if source not in sources:
            sources.append(source)

    # We print sources list:
    #print("Creation of content sources:")
    #for source in sources:
    #    print("* {}".format(source))


    # We create a numpy vector mapped to labels:
    percent = np.zeros(len(sources))

    for source in data['Source']:
        for index in range(len(sources)):
            if source == sources[index]:
                percent[index] += 1
                pass

    percent /= 100

    # Pie chart:
    pie_chart = pd.Series(percent, index=sources, name='Sources')
    pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6));


    from textblob import TextBlob
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

    #data.to_csv('boehermann.csv', encoding='utf-8')

    # We construct lists with classified tweets:
    pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]


    # We print percentages:
    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))

    #data2.append(data)
    data.to_csv('boehermann.csv', header=False, encoding='utf-8', mode='a')
    print("-------------")
    print("USER: "+ dudes + " FINISHED")
    print("-------------")

    print("\n\n")


#data2.to_csv('boehermann.csv', encoding='utf-8')
print("---------------------------------")
print("Everything written successfully!")
