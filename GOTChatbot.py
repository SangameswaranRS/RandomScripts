import nltk
import numpy as np
import random
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print('--Libraries Imported--')
lm = WordNetLemmatizer()

# Function to handle greetings
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "Improve your knowledge talking to a GOT Master"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def lemmatizeTokens(tokens):
    return [lm.lemmatize(token) for token in tokens]
    
def LemNormalize(text):
    return    

# Use Cosine similarity - to find out similar sentences in the corpus and return it to the user.
# TFID Vectorizer - To vectorize words in the userip, corpus.
def response(user_response, sentencesInTheDataset):
    robo_response=''
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(sentencesInTheDataset)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response='Actually I am not a pro in GOT. I dont clearly understand what you are saying'
        return robo_response
    else:
        return sentencesInTheDataset[idx]

def startBot():
    file = open("ASOIAF.txt", "r")
    fileContents = file.read()
    # Transform everything into lowercase.
    fileContents = fileContents.lower()
    sentencesInTheDataset = sent_tokenize(fileContents)
    wordsInTheDataset = word_tokenize(fileContents)
    lemmatizedTokens = lemmatizeTokens(wordsInTheDataset)
    print('-------------------------------------------')
    repeatFlag = True
    print('I can answer Some of your questions to GOT')
    while(repeatFlag):
        user_response= input('You: ')
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                repeatFlag=False
                print("GOT: You are welcome..")
            else:
                if(greeting(user_response)!=None):
                    print("GOT: "+greeting(user_response))
                else:
                    sentencesInTheDataset.append(user_response)
                    wordsInTheDataset=wordsInTheDataset+word_tokenize(user_response)
                    final_words=list(set(wordsInTheDataset))
                    print("GOT: ",end="")
                    print(response(user_response,sentencesInTheDataset))
                    sentencesInTheDataset.remove(user_response)
        else:
            repeatFlag=False
            print("GOT: Bye! take care..")

# Start the bot:
startBot()