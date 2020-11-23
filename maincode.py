import tweepy
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
plt.ion()


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

### initialization of team names and starting 11 from the game

Team1 = "Chelsea"
Team2 = "Newcastle"

#Team1
Team1_Player1 = "Mendy"
Team1_Player2 = "Rudiger"
Team1_Player3 = "Zouma"
Team1_Player4 = "Chilwell"
Team1_Player5 = "James"
Team1_Player6 = "Kante"
Team1_Player7 = "Mount"
Team1_Player8 = "Kovacic"
Team1_Player9 = "Abraham"
Team1_Player10 = "Werner"
Team1_Player11 = "Ziyech"

#Team2
Team2_Player1 = "Joelinton"
Team2_Player2 = "Saint-Maximin"
Team2_Player3 = "Hayden"
Team2_Player4 = "Longstaff"
Team2_Player5 = "Murphy"
Team2_Player6 = "Lewis"
Team2_Player7 = "Clark"
Team2_Player8 = "Lascelles"
Team2_Player9 = "Fernandez"
Team2_Player10 = "Manquillo"
Team2_Player11 = "Darlow"

Team1_player_array = [Team1_Player1, Team1_Player2, Team1_Player3, Team1_Player4, Team1_Player5, Team1_Player6, Team1_Player7,
Team1_Player8, Team1_Player9, Team1_Player10, Team1_Player11] # player array for Team 1

Team2_player_array = [Team2_Player1, Team2_Player2, Team2_Player3, Team2_Player4, Team2_Player5, Team2_Player6, Team2_Player7,
Team2_Player8, Team2_Player9, Team2_Player10, Team2_Player11] # player array for Team 2

Team1_player_sentiment = [] # place holder array for players senitment scores
Team1_player_tweets = [] # place holder for the tweets for each player that match threshold

Team2_player_sentiment = [] # place holder array for players senitment scores
Team2_player_tweets = [] # place holder for the tweets for each player that match threshold

### setting date range, ideally run day after the game

date_since = "2020-11-21"
date_until = "2020-11-22"

### implementiation for specific terms relating to the game, perhaps for ranking

game_terms = ['pass','goal','defend','dribble']

### code to sort by sentiment rating

def sentiment_element(element): # define sorting function
    return element[1]


### implementation ranking function to weight?















### implementation to find highest or lowest sentiment tweets














### loop for Team 1


# note for self, maybe want to specify POS and relationship to avoid bad classification


for i in Team1_player_array: # loop through each player
    search_words = [i, Team1, Team2] # search array for each player
    tweets = tweepy.Cursor(api.search,search_words,lang="en",since=date_since).items(100) # find tweets for each player
    tweet_array = []
    sentiment_array = []

    for tweet in tweets:
        tweet_array.append(tweet.text)
        sentiment_array.append(TextBlob(tweet.text).sentiment) # append the sentiment into array

    Team1_player_tweets.append(tweet_array) # create array of all of the respective player tweets

    sentiment_count = 0 # want to only count sentiments that are subjective
    sentiment_total = 0 # keep track for average
    for sentiment in sentiment_array:
        if (sentiment[1] >= 0.10): # set threshold for objectivity, 0 = objective, 1 = subjective
            sentiment_count = sentiment_count + 1
            sentiment_total = sentiment_total + sentiment[0]

    if (sentiment_total == 0):
        Team1_player_sentiment.append([i,0,sentiment_count]) # handle 0 count
    else:
        Team1_player_sentiment.append([i,sentiment_total/sentiment_count,sentiment_count])


### loop for Team 2

for i in Team2_player_array: # loop through each player
    search_words = [i, Team1, Team2] # search array for each player
    tweets = tweepy.Cursor(api.search,search_words,lang="en",since=date_since).items(100) # find tweets for each player
    tweet_array = []
    sentiment_array = []

    for tweet in tweets:
        tweet_array.append(tweet.text)
        sentiment_array.append(TextBlob(tweet.text).sentiment) # append the sentiment into array

    Team2_player_tweets.append(tweet_array) # create array of all of the respective player tweets

    sentiment_count = 0 # want to only count sentiments that are subjective
    sentiment_total = 0 # keep track for average
    for sentiment in sentiment_array:
        if (sentiment[1] >= 0.10): # set threshold for objectivity
            sentiment_count = sentiment_count + 1
            sentiment_total = sentiment_total + sentiment[0]


    if (sentiment_total == 0):
        Team2_player_sentiment.append([i,0,sentiment_count]) # handle 0 count
    else:
        Team2_player_sentiment.append([i,sentiment_total/sentiment_count,sentiment_count])


### sort each senitment array and organize for plotting

Team1_player_sentiment.sort(key=sentiment_element)
Team2_player_sentiment.sort(key=sentiment_element)

# create index for team 1
Team1_Index = []
Team1_Sentiment = []
for i in Team1_player_sentiment:
    Team1_Index.append(i[0])
    Team1_Sentiment.append(round(i[1],3))

# create index for team 2
Team2_Index = []
Team2_Sentiment = []
for i in Team2_player_sentiment:
    Team2_Index.append(i[0])
    Team2_Sentiment.append(round(i[1],3))


### create bar graphs displaying data and then save down

def plot_bar_team1():
    fig, ax = plt.subplots()
    ax.barh(Team1_Index, Team1_Sentiment, color = "lightblue")
    plt.title(Team1 + ' Sentiment')
    plt.xlabel('Sentiment Score [-1,1]')
    for i, v in enumerate(Team1_Sentiment):
        ax.text(v, i, " " + str(v), color='black', va = 'center', fontweight='bold')
    plt.savefig('team1.png')

plot_bar_team1()

def plot_bar_team2():
    fig, ax = plt.subplots()
    ax.barh(Team2_Index, Team2_Sentiment, color = "orange")
    plt.title(Team2 + ' Sentiment')
    plt.xlabel('Sentiment Score [-1,1]')
    for i, v in enumerate(Team2_Sentiment):
        ax.text(v, i, " " + str(v), color='black', va = 'center', fontweight='bold')
    plt.savefig('team2.png')

plot_bar_team2()






