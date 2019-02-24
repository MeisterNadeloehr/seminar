






















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


#ALLE USER
liste = [
'EstoyLimpia',
'Hera22112013',
'IsidorMeyer1',
'Chasty_t',
'Dunkeldenk',
'JaNuWatn',
'sandmango2005',
'MadFWagner',
'mona_rumpel',
'ramses_der_lll',
'henrik_verwoerd',
'FFritzsche2',
'LC180666',
'fop4651',
'chris_p79',
'WilhelmTell77',
'NikoLaus1977',
'bo_hermaine',
'uwebecher',
'Ayse_0815',
'MyCodeOfConduct',
'Matthias_Kt',
'DatOlli64',
'6pack88',
'X9donernesto',
'blaupfeil',
'Renft1964',
'Grazywalking',
'FvdMosselaar',
'cornelia_cagol',
'Boelscheline',
'SchafDas',
'kchak79',
'schweizerguy',
'MaximilianHenr5',
'KarlHalasz',
'DeutscherMiche5',
'NightRalph',
'safe_ID35',
'FalkRodig',
'HamburgerDeern4',
'StolzesVolk',
'darktweep',
'Logiker01',
'NationalerBoy14',
'wakeupinfo',
'HeidiHofer06',
'Luisa_maletzki',
'lmaolililu',
'BERLINER1404',
'HuhnUschi',
'dfoqF5yazTb1YI3',
'nansen_harald',
'WalhallaWachter',
'hdiesterweg',
'PrinzPrint7',
'svensationismus',
'peterkah12',
'Mica4711',
'FiveFaker',
'morawnski',
'SalvatoreDiVito',
'KimmyBertsch',
'LudwigErhard2',
'SigfriedArthur',
'dgsportler',
'DKekser',
'MichaelSellne11',
'EarlyTurner444',
'MadDocFoster',
'richito81',
'G0RI1982',
'LuetzowsJagd',
'Vergesslichr',
'Miss_Morpheus',
'Silgetown',
'tueringi24972',
'hh119933',
'AnchardAran',
'SeppDahte',
'gruenebanane1',
'Urleere',
'AvalancheGerman',
'Chreuper',
'Deutscher_17',
'Adler184',
'DeutscheFarben',
'Sachsen_17',
'g_oschi',
'JustAnotherReco',
'MicKurti',
'Shimmy_rhymes',
'AbdulMansoor01',
'Der_Erzgebirger',
'homemimy',
'66Boreas',
'BjrnHansen18',
'77abraxas77',
'jesper_vangroot',
'CyberCrusader14',
'PaulAbr89089961',
'reimgration',
'PeterWitzbold',
'MalWieder_real',
'FatihTlatoaniXa',
'Deutschland_17',
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

#liste2 = ['user:']

# Open/create a file to append data to
csvFile = open('result_reconquista.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)


# pro_trump=['TruthSerum888','karlyherron', 'R41nB14ck', 'RedApplePol', 'MKhaoS_86']
for screen_name in liste:
    try:
        user_followers = extractor.friends_ids(id=screen_name)# this returns the interger value of the user id a sepcifc user is following

    except tweepy.TweepError as t:
        if t.api_code == 50: # The code corresponding to the user not found error
            print("screen_name that failed=",  screen_name)
            liste.remove(screen_name)
            #print(liste)
        elif t.api_code == 88: # The code for the rate limit error
            #time.sleep(15*60) # Sleep for 15 minutes
            print("rate limit")
    else:# if no error
         #print("No error ", screen_name)
         #liste2.append(screen_name)
        print(screen_name)
        csvWriter.writerow("'" + screen_name  + "',")

csvFile.close()

