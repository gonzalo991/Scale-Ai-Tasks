'''
Concept to cover (this is what your task must be about):
**High Level*: ML/AI

Category:
Natural Language Processing

Topic:
Future Directions

Operation for 1st prompt (you only need to follow this for your 1st prompt):

Rewrite: Ask the assistant to edit or modify an existing piece of code following various instructions.

Subsequent Prompt Guidance (how you must continue your conversation past the first response):

Same concept but not specific to the previous responses: For all subsequent prompts, discuss the same concept but do not directly follow-up on the previous responses.
'''

import tweepy
from textblob import TextBlob
import spacy
import matplotlib.pyplot as plt

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Load the spaCy model for entity recognition
nlp = spacy.load('en_core_web_sm')

# Function to perform sentiment analysis and entity recognition
def perform_sentiment_analysis(tweet):
    analysis = TextBlob(tweet)
    sentiment = analysis.sentiment.polarity
    entities = []
    doc = nlp(tweet)
    for entity in doc.ents:
        entities.append(entity.text)
    return sentiment, entities

# Perform social media analysis
def social_media_analysis(topic, count=100):
    tweets = api.search(q=topic, count=count)
    positive_sentiments = 0
    negative_sentiments = 0
    neutral_sentiments = 0
    entity_count = {}

    for tweet in tweets:
        sentiment, entities = perform_sentiment_analysis(tweet.text)
        if sentiment > 0:
            positive_sentiments += 1
        elif sentiment < 0:
            negative_sentiments += 1
        else:
            neutral_sentiments += 1

        for entity in entities:
            if entity in entity_count:
                entity_count[entity] += 1
            else:
                entity_count[entity] = 1

    # Plotting the sentiment distribution
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive_sentiments, negative_sentiments, neutral_sentiments]
    colors = ['green', 'red', 'blue']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Sentiment Analysis for ' + topic)
    plt.show()

    # Displaying the entity count
    sorted_entities = sorted(entity_count.items(), key=lambda x: x[1], reverse=True)
    print("Entity Count:")
    for entity, count in sorted_entities:
        print(entity + ": " + str(count))

# Perform social media analysis for a topic
topic = 'AI'
social_media_analysis(topic)
