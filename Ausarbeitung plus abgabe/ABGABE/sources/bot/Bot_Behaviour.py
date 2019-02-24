import tweepy
import random
import datetime
import time

#standard authentification stuff
consumer_key = 'aRLGzK3P3MWSz368Hwrn9KIP3'
consumer_secret = 'D5gWYq06j6C6M3Z0uHC54gMK3Ox6jxTxw3RpW2JaUrxmf6CxpH'
access_token = '766383287996645376-KMvy3Nug57h2upYAfm6z8DHvI5ZUSr6'
access_token_secret = 'PoX9jeJmQkjvANW11wgySY6ad1GgFXBqBSn0XL2jJiBww'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#stores last seen tweet, so that no tweet is responded to multiple times
last_seen_ids = ["1"]


def retrieve_last_seen_id():
	return last_seen_ids[-1]

def store_last_seen_id(last_seen_id):
	last_seen_ids.append(last_seen_id)
	return

def switch_message(random_int):
	switcher = {
		0: "Das klingt sehr unglaubwürdig.",
		1: "Oh wirklich?",
		2: "Gibt es dazu auch richtige Quellen?",
		3: "Haben Sie dazu auch schon wo anders nachgelesen?",
		4: "Das klingt sehr nach Propaganda...",
		5: "Liest sich, als hätte das jemand extra für rechtes Publikum geschrieben",
		6: "Forschen Sie dazu mal genauer nach.",
		7: "Merken Sie eigentlich, was Sie hier verbreiten?",
		8: "Das stimmt nicht.",
		9: "Ich glaube nicht.",
		10: "Echt?",
		11: "Sicher?",
		12: "Finden Sie wirklich?",
		13: "Wo haben Sie das her?",
		14: "Was meinen Sie damit?",
		15: "Das kann doch nicht sein!",
		16: "Das kann so doch nicht stimmen",
		17: "Klingt falsch",
		18: "Meinen Sie das ernst?",
		19: "Glauben Sie das auch selbst?",
		20: "Tatsächlich?",
		21: "Finden Sie?",
		22: "Das denken Sie?",
		23: "Klingt das nicht wie Propaganda?",
		24: "Das glaube ich nicht...",
		25: "Sowas kann nicht wahr sein",
		26: "Da reproduzieren Sie aber selbst Lügenpresse...",
		27: "Wäre gut, wenn sich jemand wirklich informieren würde, bevor man so etwas schreibt...",
		28: "Schon mal selbst nachgeforscht?",
		29: "So langsam wird es lächerlich...",
		30: "Das klingt wie ausgedacht!",
		31: "Finde ich nicht.",
		32: "Das kann nicht der Wahrheit entsprechen.",
		33: "Wer denkt sich so etwas aus?",
		34: "Haben Sie so etwas überhaupt selber erlebt bevor Sie nur Propaganda reproduzieren?",
		35: "Das klingt nach rechtem Geschwätz!",
		36: "Das kann doch keiner ernstnehmen",
		37: "Denken Sie da doch mal rational drüber nach!",
		38: "Naja...",
		39: "Hören Sie doch auf damit.",
		40: "Passiert so etwas wirklich?",
		41: "Haben Sie dazu schon mal Fakten gecheckt?",
		42: "Checken Sie doch erst einmal die Fakten, bevor Sie so etwas schreiben"
	}
	return switcher.get(random_int, "")

def pull_tweets():
	last_seen_id = retrieve_last_seen_id()
	timeline = api.home_timeline(last_seen_id, tweet_mode='extended')

	for tweet in reversed(timeline):
		with open('Wordcloud_all_nouns.txt') as wordcloud:
			for keyword in wordcloud:
				keyword_stripped = keyword.strip()
				if tweet.id not in last_seen_ids and keyword_stripped.lower() in tweet.full_text.lower():
					last_seen_id = tweet.id
					store_last_seen_id(last_seen_id)
					print(str(tweet.id) + ", Schlüsselwort: " + keyword)
					random_int = random.randint(0,42)
					message = switch_message(random_int)

					if tweet.full_text.startswith("RT @") == True:
					    print("this tweet is a Retweet")
					    print(str(tweet.id) + " - " + tweet.full_text)
					    print(tweet.retweeted_status.id)
					    retweet = api.get_status(tweet.retweeted_status.id)
					    print(str(retweet.id) + " - " + retweet.text)
					    api.update_status("@"+retweet.user.screen_name + " "+ message, retweet.id)
					    print("@"+retweet.user.screen_name + " "+ message)
					else:
					    print("this tweet is original")
					    api.update_status("@"+tweet.user.screen_name + " "+message, tweet.id)
					    print(str(tweet.id) + " - " + tweet.full_text)
					    print("@"+tweet.user.screen_name + " "+ message)

					random_int = random.randint(-60,60)
					time.sleep(120+random_int)


while True:
	if datetime.datetime.now().hour < 23 and datetime.datetime.now().hour > 7:
	    pull_tweets()
	    random_int = random.randint(-10,10)
	    random_int = random_int * 60
	    time.sleep(900+random_int)