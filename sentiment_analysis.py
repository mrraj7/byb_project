# ===================================================================================================
# Practical Task 26 - Python program that performs sentiment analysis on a dataset of product reviews
# ===================================================================================================

# Import all the required libraries
import spacy
from textblob import TextBlob
import pandas as pd
import re

# Load the en_core_web_sm spaCy model as per the given requirement
nlp = spacy.load('en_core_web_sm')

# Define a function to pre-process the given text data.
# This is to remove special characters, integers, stopwords, punctuations, currency and spaces
def normalise(msg):
    msg = re.sub('[^A-Za-z]+', ' ', str(msg)) 
    doc = nlp(msg)
    res=[]
    for token in doc:
        if(token.is_stop or token.is_digit or token.is_punct or not(token.is_oov) or token.is_currency 
           or token.is_space or len(token.text) <= 2):
            pass
        else:
            res.append(token.lemma_.lower())
    return res

# Define a function for sentiment analysis
def sentiment_analysis(text):
    # Process the text with SpaCy
    doc = nlp(text)
    
    # Use TextBlob for sentiment analysis
    blob = TextBlob(doc.text)
    
    # Get sentiment polarity (-1 to 1) 
    sentiment = blob.sentiment
    return sentiment.polarity

# This function is to label for the polarity score. A polarity score of 1 indicates a very positive sentiment, 
# while a polarity score of -1 indicates a very negative sentiment. A polarity score of close to 0 
# indicates a neutral sentiment

def get_sentiment_label(polarity_score):
    if polarity_score > 0.05:
        print(f"The sentiment polarity {polarity_score} reflects a positive review .")
        return
    elif polarity_score < -0.05:
        print(f"The sentiment polarity {polarity_score} reflects a negative review.")
        return
    else:
        print(f"The sentiment polarity {polarity_score} a neutral review.")
        return

# This function is to take the input statement and predict the sentiment 
def sentiment_predictor(input):
    clean_text = normalise(input)
    sentiment = sentiment_analysis(str(clean_text))
    label = get_sentiment_label(sentiment)
    return

# This function is to check similarity of the given text
# Use similarity() method to get the similarity score of two given review text
def similarity_score(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    similarity = doc1.similarity(doc2)
    print(f"Similarity score : {similarity}")
    return

# Test the model by taking a couple of sample review text and predicts its sentiment
input1 = ["Bought this product for my Dad. Its perfectly working as expected. I would recommend this to others"]
input2 = ["product broken in few weeks and  waste of money"]
sentiment_predictor(input1[0])
sentiment_predictor(input2[0])

# Now, test the model on sample Amazon product reviews

# First read the CSV file
df = pd.read_csv("/Users/tsmr_/Desktop/Session folder/Machine Learning/NLP/amazon_product_reviews.csv")

# Drop any null values in the dataframe, if any 
df.dropna(subset=['reviews.text'], inplace=True)

# Now test the model by passing few product reviews and predicts its sentiment
my_review_of_choice1 = df['reviews.text'][0]
my_review_of_choice2 = df['reviews.text'][17]
my_review_of_choice3 = df['reviews.text'][200]
my_review_of_choice4 = df['reviews.text'][254]

sentiment_predictor(my_review_of_choice1)
sentiment_predictor(my_review_of_choice2)
sentiment_predictor(my_review_of_choice3)
sentiment_predictor(my_review_of_choice4)

# Now let's check the similarity of the product reviews for couple of product reviews text
similarity_score(df['reviews.text'][0], df['reviews.text'][200])

