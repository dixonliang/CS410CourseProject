# CS 410 Course Project

This is the repo for my course project for CS 410 Text Information Systems for my Masters in Computer Science at University of Illinois Urbana-Champaign. The main idea of this repo is to provide the code, documentaion, and demo for a basic sentiment analysis for soccer games using Python. The easiest way to use this code is to use the Jupyter Notebook in this repo. A video tutorial on Youtube is also provided. The source code is available as well. 

YouTube Demo Link: 

Files: 
Project Proposal.pdf - The initial project proposal. 
Progress Report.pdf - Progress Report as of 11/30/20.
maincode.py - The main source code
demo.ipynb - Empty demo code in Jupyter Notebook

We will be using Tweepy to source tweets from the Twitter API and TextBlob to provide a framework for natural language processing to provide sentiment analysis. In addition, we will use PyPi's implementation of BM25Okapi to provide context of the sentiment analysis.

Ideally, the result of this code will show the relative sentiment of a player's performance during a recent game. By using wisdom of the crowds, we hope to gain an idea of how the player performed. Using BM25Okapi, we will also be able to use relevant terms to see what might have caused sentiment to go way or another (ex. player scored a goal or provided an assist, etc.) Using PyPlot, we will also be able to visualize the results.

Technically, this code can be used for any soccer game, but given the popularity and language barrier, EPL games are likely to provide the most meaningful results. Adjustments could be made for La Liga or Serie A using Spanish or Italian NLP. Please feel free to reach out as I welcome any collaboration as the code can be improved and applied to different sports or different applications all together :) .
