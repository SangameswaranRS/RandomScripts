print('---Init---')
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

print('--Importing done--')

# Nltk expects word features to be like this. ['Hello', 'World'] should be structured as {'Helo':True,'wordl':true}
def create_features_from_words(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    print('--stopped unused words--')
    return dict([(word,True) for word in words])

# Get negative reviews from the corpus
def get_negative_reviews():
    totalNegativeReviews = []
    for files in movie_reviews.fileids('neg'):
        wordsInFile = movie_reviews.words(files) 
        # Dataset tuple(word features,labels)
        totalNegativeReviews.append((create_features_from_words(wordsInFile), "Negative"))
    return totalNegativeReviews

# Get positive reviews from the corpus
def get_positive_reviews():
    totalPositiveReviews= []
    for files in movie_reviews.fileids('pos'):
        wordsInFile = movie_reviews.words(files)
        totalPositiveReviews.append((create_features_from_words(wordsInFile),"Positive"))
        return totalPositiveReviews

# Train the Classifier.
def classifier_train_full():
    # Training the entire data. If score is needed, then split into training and testing datasets
    positiveReviews = get_positive_reviews()
    negativeReviews = get_negative_reviews()
    trainingData = positiveReviews[:800]+negativeReviews[:800]
    testingData = negativeReviews[800:]+ positiveReviews[800:]
    print('--Training Classifier--')
    classifier = NaiveBayesClassifier.train(trainingData)
    accuracy = nltk.classify.util.accuracy(classifier, testingData)
    print('---Model Accuracy='+str(accuracy)+'-------')
    return classifier

def entry_point():
    classifier = classifier_train_full()
    reviewInput= input('Enter your review : ')
    wordsInReviewInput = word_tokenize(reviewInput)
    reviewSentiment = classifier.classify(create_features_from_words(wordsInReviewInput))
    print('---Review Category----'+str(reviewSentiment))

entry_point()

