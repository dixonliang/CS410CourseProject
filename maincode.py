import tweepy
from textblob import TextBlob
import numpy as np

consumer_key = "HR3EtkGlGwOp1rIXnF6Ung1ru"
consumer_secret = "cf3xBpa3cnJ695B4jsfVaXyeQY5G0vkDaikYEOwPK5AkvkqPn1"
access_token = "1963798074-flPLyqr6TrTvisNbuBknHeutsz6CCNsrFL6jZ5g"
access_token_secret = "BYpEqUOKVbWGVIZvKN4Wt8GmyA70jTEPDCfXJ4Oto3KHA"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth,wait_on_rate_limit=True)

### initialization of team names and starting 11 + subs from the game

Team1 = "England"
Team2 = "Belgium"

#Team1
Team1_Player1 = "Grealish"
Team1_Player2 = "Sancho"
Team1_Player3 = "Dier"
Team1_Player4 = "Walker"
Team1_Player5 = "Mings"
Team1_Player6 = "Trippier"
Team1_Player7 = "Rice"
Team1_Player8 = "Henderson"
Team1_Player9 = "Chilwell"
Team1_Player10 = "Mount"
Team1_Player11 = "Kane"

#Team2
Team2_Player1 = ""
Team2_Player2 = ""
Team2_Player3 = ""
Team2_Player4 = ""
Team2_Player5 = ""
Team2_Player6 = ""
Team2_Player7 = ""
Team2_Player8 = ""
Team2_Player9 = ""
Team2_Player10 = ""
Team2_Player11 = ""

player_array = [Team1_Player1, Team1_Player2, Team1_Player3, Team1_Player4, Team1_Player5, Team1_Player6, Team1_Player7,
Team1_Player8, Team1_Player9, Team1_Player10, Team1_Player11] # player array

player_sentiment = [] # place holder array for players senitment scores

### setting date range, ideally run day after the game

date_since = "2020-11-12"
date_until = "2020-11-19"

### code to find sentiment

def sentiment_element(element): # define sorting function
    return element[1]

for i in player_array: # loop through each player
    search_words = [i, Team1, Team2] # search array for each player
    tweets = tweepy.Cursor(api.search,search_words,lang="en",since=date_since).items(50) # find tweets for each player
    tweet_array = []
    sentiment_array = []

    for tweet in tweets:
        tweet_array.append(tweet.text)
        sentiment_array.append(TextBlob(tweet.text).sentiment) # append the sentiment into array

    sentiment_count = 0 # want to only count sentiments that are subjective
    sentiment_total = 0 # keep track for average
    for sentiment in sentiment_array:
        if (sentiment[1] >= 0.25):
            sentiment_count = sentiment_count + 1
            sentiment_total = sentiment_total + sentiment[0]

    player_sentiment.append([i,sentiment_total/sentiment_count,sentiment_count])
    player_sentiment.sort(key=sentiment_element)







