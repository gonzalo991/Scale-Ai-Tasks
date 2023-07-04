# 1. explain this piece of code use for a brand reputation management:  

import pandas as pd  
from textblob import TextBlob

# Load the customer reviews dataset

reviews_df = pd.read_csv('customer_reviews.csv')

# Perform sentiment analysis on each review

sentiments = []  
for review in reviews_df['review_text']:  
    blob = TextBlob(review)  
    sentiment_score = blob.sentiment.polarity  
    if sentiment_score > 0:  
        sentiment = 'Positive'  
    elif sentiment_score < 0:  
        sentiment = 'Negative' 
    else:  
        sentiment = 'Neutral' 
sentiments.append(sentiment)

# Add sentiment column to the dataframe

reviews_df['sentiment'] = sentiments

# Calculate overall sentiment distribution

sentiment_counts = reviews_df['sentiment'].value_counts()

# Calculate average sentiment score

average_sentiment_score = reviews_df['sentiment_score'].mean()

# Identify most common positive and negative words

positive_reviews = reviews_df[reviews_df['sentiment'] == 'Positive']  
positive_words = ’ '.join(positive_reviews['review_text']).split()

negative_reviews = reviews_df[reviews_df['sentiment'] == 'Negative']  
negative_words = ’ '.join(negative_reviews['review_text']).split()

common_positive_words = pd.Series(positive_words).value_counts().head(10)  
common_negative_words = pd.Series(negative_words).value_counts().head(10)

# Generate insights and reports

print('Sentiment Distribution:')  
print(sentiment_counts)

print('\nAverage Sentiment Score:')  
print(average_sentiment_score)

print('\nMost Common Positive Words:')  
print(common_positive_words)

print('\nMost Common Negative Words:')  
print(common_negative_words)

# Export the updated dataset with sentiment analysis results

reviews_df.to_csv('customer_reviews_with_sentiment.csv', index=False)

'''
The code above performs sentiment analysis on customer reviews and generates insights and reports.

The code imports the libraries pandas and TextBlob. It then reads the customer reviews dataset and performs 
sentiment analysis on each review. The sentiments are added to the dataframe, and the overall sentiment distribution, 
average sentiment score, and the most common positive and negative words are calculated. Finally, the updated dataset 
is exported with the sentiment analysis results.

In this example, we assume that you have a CSV file called ‘customer_reviews.csv’. This file contains customer reviews 
in a column called ‘review_text’. This code uses TextBlob’s sentiment-analysis library, where sentiments are scored from 
-1 to 1. Sentiments are classified as positive, negative or neutral based on these scores.

The code iterates over each review, performs sentiment analysis using TextBlob and assigns a sentiment label (‘positive’,
 ‘negative’ or ‘neutral’). The code adds the sentiment-column to the dataframe.

By counting the occurrences of each sentiment label, the code calculates the overall sentiment distribution. 
The code also calculates the average sentiment score across all of the reviews.

In addition, by combining all positive and negative reviews and extracting the most common words, the code 
identifies the most common positive and negative words.

Lastly, the code generates insights and reporting, printing the sentiment distribution, average sentiment 
scores and the most common positive and negative words.

When finished, the code exports the updated dataset containing the sentiment analysis results to a new CSV 
file named ‘customer_reviews_with_sentiment.csv’.

Note that this is a simplified example and in a real situation it might be necessary to pre-process the 
text data, handle more complex sentiment analysis models and consider additional features such as review 
metadata, entity extraction and trend analysis to enhance brand reputation management.

 2. How does the code handle preprocessing of the customer reviews ?

The pre-processing of customer reviews is not explicitly shown in the code example provided. However, for 
NLP tasks such as sentiment analysis, preprocessing is an important step. Before performing sentiment analysis, 
here are some common preprocessing techniques that can be used:

-   **Text cleaning**  — This is the removal of unnecessary characters, such as punctuation marks, special 
symbols or emoticons, which may not contribute significantly to the sentiment analysis task.
-   **Lowercase**  — Ensures that the sentiment analysis model treats words in a case-insensitive manner by 
converting all text to lower case. This is not the case with the words ‘good’ and ‘good’.
-   **Tokenisation**  — In this step, the text is broken down into individual words, or tokens. Tokenisation 
helps to analyse text at a more granular level. It also helps to capture word-level features.
-   **Stopword removal**  — Stopwords are common words such as ‘and’, ‘the’ or ‘is’ that often carry little 
sentiment or meaning. The removal of stop words can reduce noise in the data and improve the efficiency of 
sentiment analysis.
-   **Lemmatisation or stemming**  — Lemmatising or stemming reduces words to their stem or root. Lemmatisation 
takes into account the context of the word. Stemming applies simpler rules to remove prefixes or suffixes. The 
aim is to reduce inflectional variation and treat related words as the same, which is an aid to sentiment analysis accuracy.
-   **Negation handling**  — Negation words can reverse the sentiment of subsequent words, such as “not”, “no” 
or “never”. As part of the pre-processing, the identification and handling of such negation patterns may be 
necessary to ensure accurate sentiment analysis.

Libraries such as NLTK (Natural Language Toolkit) or spaCy in Python are typically used to perform these 
preprocessing steps. Improving the quality of input data, reducing noise and improving the performance of
sentiment analysis models can be achieved by implementing these techniques prior to sentiment analysis.
'''

# 3. can you refactor this code and add this step ?


#Here is a refactored version of the code that includes some pre-processing of the text using the NLTK library:

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the customer reviews dataset
reviews_df = pd.read_csv('customer_reviews.csv')

# Text preprocessing
lemmatizer = WordNetLemmatizer()
stopwords = set(stopwords.words('english'))

preprocessed_reviews = []
for review in reviews_df['review_text']:
    # Text cleaning - remove punctuation and special characters
    cleaned_text = ''.join([c for c in review if c.isalnum() or c.isspace()])
    
    # Tokenization
    tokens = nltk.word_tokenize(cleaned_text.lower())
    
    # Stopword removal
    filtered_tokens = [token for token in tokens if token not in stopwords]
    
    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    preprocessed_review = ' '.join(lemmatized_tokens)
    preprocessed_reviews.append(preprocessed_review)

# Add preprocessed reviews to the dataframe
reviews_df['preprocessed_review'] = preprocessed_reviews

# Perform sentiment analysis on each preprocessed review
sentiments = []
for preprocessed_review in reviews_df['preprocessed_review']:
    blob = TextBlob(preprocessed_review)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        sentiment = 'Positive'
    elif sentiment_score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    sentiments.append(sentiment)

# Add sentiment column to the dataframe
reviews_df['sentiment'] = sentiments

# Rest of the code remains the same...



# 4. can you explain the new functionality of this code ?
'''
The new functionality of the code is the addition of text preprocessing using the NLTK library. For text 
pre-processing, the following steps have been added:

1.  Import necessary NLTK modules (stopwords, punkt, wordnet) and download resources.
'''
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')



# 2.  Using the stopwords corpus from NLTK, initialise a WordNet lemmatiser for lemmatisation and create a 
# set of English stopwords.

lemmatizer = WordNetLemmatizer()
stopwords = set(nltk.corpus.stopwords.words('english'))


'''
3.  The following pre-processing steps are performed within the loop iterating over customer reviews:

-   Text cleaning, which removes unnecessary characters such as punctuation marks and special symbols.
-   Tokenization, which breaks down the text into individual words, or tokens.
-   Stopword removal, which removes common words such as ‘and’, ‘the’, or ‘is’ that often carry little sentiment or meaning.
-   Lemmatization, which reduces words to their stem or root.
-   The pre-processed tokens are then reassembled to form a pre-processed token string.

'''
preprocessed_reviews = []
for review in reviews_df['review_text']:
    # Text cleaning - remove punctuation and special characters
    cleaned_text = ''.join([c for c in review if c.isalnum() or c.isspace()])
    
    # Tokenization
    tokens = nltk.word_tokenize(cleaned_text.lower())
    
    # Stopword removal
    filtered_tokens = [token for token in tokens if token not in stopwords]
    
    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    preprocessed_review = ' '.join(lemmatized_tokens)
    preprocessed_reviews.append(preprocessed_review)

# 4.  The pre-processed reviews are added to the data frame as a new column (pre-processed_review).


reviews_df['preprocessed_review'] = preprocessed_reviews


'''
5.  As shown in the previous code, sentiment analysis is performed on each preprocessed review.

By incorporating these preprocessing steps, the code can now perform sentiment analysis on the preprocessed reviews, rather than on the raw customer reviews. The sentiment analysis is performed using the TextBlob library, which scores the sentiment of each review based on a polarity score. The sentiment score is then classified as positive, negative, or neutral.

'''


# 5. How does the code handle special characters, punctuation, and whitespace during the text cleaning step?

'''
The text cleaning step removes unnecessary characters such as special symbols and punctuation marks. It 
also standardizes whitespace. Here is an overview of how the code handles special characters, punctuation, 
and whitespace:

1.  Special characters — The code removes any special characters that are not alphanumeric or whitespace. 
This is done by iterating over each character in the review text and checking if the current character is a
special character.
2.  Punctuation — The code removes any punctuation marks except for the period (.). This is done by converting
the review text to lowercase and then iterating over each character in the review text and checking if the current 
character is a punctuation mark.
3.  Whitespace — The code collapses multiple whitespace characters into a single space. This is done by iterating 
over each character in the review text and checking if the current character is a whitespace character.
4.  Blank lines — The code removes any blank lines at the beginning and end of the review text.
5.  Extra whitespace — The code removes any extra whitespace between words. This is done by trimming the review
text to remove any leading or trailing whitespace.

In the provided code, the text cleaning step focuses on removing special characters and punctuation marks from
the review text. It does not specifically handle multiple whitespaces, blank lines, or extra whitespace between words.
Here’s the corrected explanation for the text cleaning step:
'''
cleaned_text = ''.join([c for c in review if c.isalnum() or c.isspace()])
'''
In this line of code, each character c in the verification string is iterated over. The isalnum() 
method checks to see if the character is alphanumeric (a letter or a digit), and the isspace() method 
checks to see if it is a space.

It is included in the list parsing if the character is alphanumeric or a space. The review text is 
effectively stripped of all other special characters and punctuation.

For example, if the text of the review is “Hello, world! This is an example of an evaluation”, 
the cleaned text would be Hello world This is an example of an evaluation" (with special characters and 
punctuation stripped).

It’s important to note, however, that this particular step of cleaning up the text doesn’t deal with multiple 
spaces, blank lines, or extra spaces between words. Additional steps or code changes would be required to deal 
with these issues.
'''