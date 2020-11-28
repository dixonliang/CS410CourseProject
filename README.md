# Sentiment Analysis for Soccer Games (CS 410 Course Project) and Documentation

### Introduction

This is the repo for my course project for CS 410 Text Information Systems for my Masters in Computer Science at University of Illinois Urbana-Champaign. The main idea of this repo is to provide the code, documentaion, and demo for a basic sentiment analysis for soccer games using Python, Tweepy, TextBlob, and BM25Okapi. The easiest way to use this code is to use the Jupyter Notebook demo in this repo. A video tutorial on Youtube is also provided. The source code is available as well. Please feel free to reach out to me if you would like to collaborate :) .

#### Files 

YouTube Demo Link: 

Project Proposal.pdf - The initial project proposal. 

Progress Report.pdf - Progress Report as of 11/30/20.

maincode.py - The main source code

demo.ipynb - Empty demo code in Jupyter Notebook

team1_sentiment.png - Example sentiment bar chart for Team 1 (new file will be saved down if main code is run)
team1_BM25positive.png - Example positive BM25 average ranking for Team 1 (new file will be saved down if main code is run)
team1_BM25negative.png - Example negative BM25 average ranking for Team 1 (new file will be saved down if main code is run)

team2_sentiment.png - Example sentiment bar chart for Team 2 (new file will be saved down if main code is run)
team2_BM25positive.png - Example positive BM25 average ranking for Team 2 (new file will be saved down if main code is run)
team2_BM25negative.png - Example negative BM25 average ranking for Team 2 (new file will be saved down if main code is run)

### Background

We will be using Tweepy to source tweets from the Twitter API and TextBlob to provide a framework for natural language processing to provide sentiment analysis. In addition, we will use PyPi's implementation of BM25Okapi to provide context of the sentiment analysis.

Ideally, the result of this code will show the relative sentiment of a player's performance during a recent game. By using wisdom of the crowds, we hope to gain an idea of how the player performed. Using BM25Okapi, we will also be able to use relevant terms to see what might have caused sentiment to go way or another (ex. player scored a goal or provided an assist, etc.) Using PyPlot, we will also be able to visualize the results.

Technically, this code can be used for any soccer game, but given the popularity and language barrier, EPL games are likely to provide the most meaningful results. Adjustments could be made for La Liga or Serie A using Spanish or Italian NLP. Please feel free to reach out as I welcome any collaboration as the code can be improved and applied to different sports or different applications all together :) .

The easiest way to run through this code is by using the provided Jupyter Notebooks. A run through of the source code is provided below. 

### Code Documentation

#### Introduction 

Packages Needed: To begin, we need several packages installed and imported. These are: Tweepy, TextBlob, Numpy, Rank_BM25, and Matplotlib.pyplot. Documentation and links are found here: http://docs.tweepy.org/en/latest/api.html https://textblob.readthedocs.io/en/dev/api_reference.html https://numpy.org/doc/ https://pypi.org/project/rank-bm25/ https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.html

Most importantly, we will need access to the Twitter API, which can be gained by having a Twitter profile. You will be provided four keys of strings of letters and numbers which you will need to enter in the box below: consumer key, consumer secret, access token, access token secret. These will be used in the below code area. 

```shell
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)
``` 

#### Game Parameters

We will need to set the parameters for the game we are interested in; this includes the two teams names and the starting 11 for each team. 

```shell
team1 = ""
team2 = ""

#team1
team1_Player1 = ""
team1_Player2 = ""
team1_Player3 = ""
team1_Player4 = ""
team1_Player5 = ""
team1_Player6 = ""
team1_Player7 = ""
team1_Player8 = ""
team1_Player9 = ""
team1_Player10 = ""
team1_Player11 = ""

#team2
team2_Player1 = ""
team2_Player2 = ""
team2_Player3 = ""
team2_Player4 = ""
team2_Player5 = ""
team2_Player6 = ""
team2_Player7 = ""
team2_Player8 = ""
team2_Player9 = ""
team2_Player10 = ""
team2_Player11 = ""
```
After setting the game parameters, there are a few algorithm paramters we will need to set. 

```shell
### define the number of tweets we want to sort for and subjective threshold

number_of_tweets = 100 # how many tweets we want to search for
threshold = 0.10 # threshold for subjectivity [0,1]

### setting date range, ideally run day after the game

date_since = "2020-11-21"
date_until = "2020-11-22"
```


```shell
positive_terms = "assist good excellent great" # search queries, positive terms
negative_terms = "poor bad miss own awful" # negative terms
```

#### Running the Code

After setting the above parameters, the entire "maincode.py" can be run which will then output the relevant visualizations for this task. 



#### Helper Functions 




#### Output




