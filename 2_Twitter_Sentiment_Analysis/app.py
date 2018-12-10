import tweepy #Para interactuar con TW
from textblob import TextBlob #Para analizar los tweets
#Numeros que identifican a nuestra API:
consumer_key = "RZEUAlCbUZjxA6rhHzydLMSm3"
consumer_secret = "8j04g2Vcw4Q4FRS8ebXjBFBh9Vcy9eQKObTmmAyqDFcsCJuCyZ"

access_token = "824818583356186626-8XbN7XhDAJGZkqFgQeNjRZroVOvbQz5"
access_token_secret = "ewaxpFvWoy426sGWPNN2tAh14WqFPxuGKM7LRnuhLA6gL"
#Para "iniciar sesion" en TW:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) #Variable que uso para interactuar con TW

public_tweets = api.search("Trump") #Busco tweets con la palabra "Trump"

for tweet in public_tweets: #Por cada tweet que encuentre...
    print(tweet.text) #Lo convierto a texto y lo muestro en la consola
    analysis = TextBlob(tweet.text) #Analizo los tweets
    print(analysis.sentiment)
