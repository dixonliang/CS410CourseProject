import tweepy # import tweepy aka Twitter API
from textblob import TextBlob # import textblob
import numpy as np # import numpy
from rank_bm25 import BM25Okapi # import BM25
import matplotlib.pyplot as plt # import plotting
plt.ion()


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

### initialization of team names and starting 11 from the game

team1 = "Chelsea"
team2 = "Newcastle"

#team1
team1_Player1 = "Mendy"
team1_Player2 = "Rudiger"
team1_Player3 = "Zouma"
team1_Player4 = "Chilwell"
team1_Player5 = "James"
team1_Player6 = "Kante"
team1_Player7 = "Mount"
team1_Player8 = "Kovacic"
team1_Player9 = "Abraham"
team1_Player10 = "Werner"
team1_Player11 = "Ziyech"

#team2
team2_Player1 = "Joelinton"
team2_Player2 = "Saint-Maximin"
team2_Player3 = "Hayden"
team2_Player4 = "Longstaff"
team2_Player5 = "Murphy"
team2_Player6 = "Lewis"
team2_Player7 = "Clark"
team2_Player8 = "Lascelles"
team2_Player9 = "Fernandez"
team2_Player10 = "Manquillo"
team2_Player11 = "Darlow"

team1_player_array = [team1_Player1, team1_Player2, team1_Player3, team1_Player4, team1_Player5, team1_Player6, team1_Player7,
team1_Player8, team1_Player9, team1_Player10, team1_Player11] # player array for Team 1

team2_player_array = [team2_Player1, team2_Player2, team2_Player3, team2_Player4, team2_Player5, team2_Player6, team2_Player7,
team2_Player8, team2_Player9, team2_Player10, team2_Player11] # player array for Team 2

team1_player_sentiment = [] # place holder array for players senitment scores
team1_player_tweets = [] # place holder for the tweets for each player that match threshold

team2_player_sentiment = [] # place holder array for players senitment scores
team2_player_tweets = [] # place holder for the tweets for each player that match threshold

### define the number of tweets we want to sort for and subjective threshold

number_of_tweets = 100 # how many tweets we want to search for
threshold = 0.10 # threshold for subjectivity [0,1]

### setting date range, ideally run day after the game

date_since = "2020-11-21"
date_until = "2020-11-22"

### implementiation for specific terms relating to the game, perhaps for ranking in BM25Okapi

terms = ["score","assist"] # want to weight the sentiment for these terms more than usual, specifically scoring a goal or assisting a goal should be weighted more

### code to sort by sentiment rating

def sentiment_element(element): # define sorting function
    return element[1]


### implementation of BM25Okapi to rank relevant of tweets in relation the game

def rank_scores(corpus, terms):
    bm25 = BM25Okapi(corpus)
    tweet_scores = bm25.get_scores(terms)
    top_10_tweets = bm25.get_top_n(terms, corpus, n=10)
    return tweet_scores

def rank_top(corpus, terms):
    bm25 = BM25Okapi(corpus)
    top_10_tweets = bm25.get_top_n(terms, corpus, n=10)
    return top_10_tweets


### loop for Team 1 to find sentiment


for i in team1_player_array: # loop through each player
    search_words = [i, team1] # search array for each player
    tweets = tweepy.Cursor(api.search,search_words,lang="en",since=date_since,until=date_until).items(number_of_tweets) # find tweets for each player
    tweet_array = []
    sentiment_array = []
    combined_array = []

    for tweet in tweets:
        tweet_array.append(tweet.text)
        sentiment_array.append(TextBlob(tweet.text).sentiment) # append the sentiment into array

    for j in range(0,len(tweet_array)): # create combined array to sort
        combined_array.append([tweet_array[j],sentiment_array[j][0]])

    combined_array.sort(key=sentiment_element)  # sort tweet array by sentiment (remember that lowest sentiment is first)

    team1_player_tweets.append(combined_array) # create array of all of the respective player tweets, which are now sorted by sentiment

    sentiment_count = 0 # want to only count sentiments that are subjective
    sentiment_total = 0 # keep track for average
    for sentiment in sentiment_array:
        if (sentiment[1] >= threshold): # set threshold for objectivity, 0 = objective, 1 = subjective
            sentiment_count = sentiment_count + 1
            sentiment_total = sentiment_total + sentiment[0]

    if (sentiment_total == 0):
        team1_player_sentiment.append([i,0,sentiment_count]) # handle 0 count
    else:
        team1_player_sentiment.append([i,sentiment_total/sentiment_count,sentiment_count])


### loop for Team 2 to find sentiment

for i in team2_player_array: # loop through each player
    search_words = [i, team2] # search array for each player
    tweets = tweepy.Cursor(api.search,search_words,lang="en",since=date_since,until=date_until).items(number_of_tweets) # find tweets for each player
    tweet_array = []
    sentiment_array = []
    combined_array = []

    for tweet in tweets:
        tweet_array.append(tweet.text)
        sentiment_array.append(TextBlob(tweet.text).sentiment) # append the sentiment into array

    for j in range(0,len(tweet_array)): # create combined array to sort
        combined_array.append([tweet_array[j],sentiment_array[j][0]])

    combined_array.sort(key=sentiment_element)  # sort tweet array by sentiment (remember that lowest sentiment is first)

    team2_player_tweets.append(combined_array) # create array of all of the respective player tweets, which are now sorted by sentiment

    sentiment_count = 0 # want to only count sentiments that are subjective
    sentiment_total = 0 # keep track for average
    for sentiment in sentiment_array:
        if (sentiment[1] >= threshold): # set threshold for objectivity
            sentiment_count = sentiment_count + 1
            sentiment_total = sentiment_total + sentiment[0]


    if (sentiment_total == 0):
        team2_player_sentiment.append([i,0,sentiment_count]) # handle 0 count
    else:
        team2_player_sentiment.append([i,sentiment_total/sentiment_count,sentiment_count])


### display the top 10 min and max sentiment tweets for a player based on team

def display_tweets(team, player_number):
    if (team == team1):
        print(team1_player_tweets[player_number-1][0:9]) # negative sentiment
        print(team1_player_tweets[player_number-1][number_of_tweets-11:number_of_tweets-1]) # positive sentiment
    else:
        print(team2_player_tweets[player_number-1][0:9]) # negative sentiment
        print(team2_player_tweets[player_number-1][number_of_tweets-11:number_of_tweets-1]) # positive sentiment


### sort each senitment array and organize for plotting

team1_player_sentiment.sort(key=sentiment_element)
team2_player_sentiment.sort(key=sentiment_element)

# create index for team 1
team1_Index = []
team1_Sentiment = []
for i in team1_player_sentiment:
    team1_Index.append(i[0])
    team1_Sentiment.append(round(i[1],3))

# create index for team 2
team2_Index = []
team2_Sentiment = []
for i in team2_player_sentiment:
    team2_Index.append(i[0])
    team2_Sentiment.append(round(i[1],3))


### create bar graphs displaying data and then save down

def plot_bar_team1():
    fig, ax = plt.subplots()
    ax.barh(team1_Index, team1_Sentiment, color = "lightblue")
    plt.title(team1 + ' Sentiment')
    plt.xlabel('Sentiment Score [-1,1]')
    for i, v in enumerate(team1_Sentiment):
        ax.text(v, i, " " + str(v), color='black', va = 'center', fontweight='bold')
    plt.savefig('team1.png')

plot_bar_team1()

def plot_bar_team2():
    fig, ax = plt.subplots()
    ax.barh(team2_Index, team2_Sentiment, color = "orange")
    plt.title(team2 + ' Sentiment')
    plt.xlabel('Sentiment Score [-1,1]')
    for i, v in enumerate(team2_Sentiment):
        ax.text(v, i, " " + str(v), color='black', va = 'center', fontweight='bold')
    plt.savefig('team2.png')

plot_bar_team2()






