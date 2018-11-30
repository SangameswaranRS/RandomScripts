import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


inp = input('Enter text to be tokenized!')
ps = PorterStemmer()
lm = WordNetLemmatizer()

# Tokenize into words
print('------------word tokenization-------------')
words = word_tokenize(inp)
print(word_tokenize(inp))

# Sentences
print('-----------sentence tokenization-------------')
print(sent_tokenize(inp))


#Stemming the input
print('--------word stemming----------')
for w in words:
    print(ps.stem(w))


#Part of Speech Tagging.
print('---------------POS tagging---------------')
tagged_words = nltk.pos_tag(words)
print(tagged_words)


# Named Entity Recognition
print('-------named entity recognition------------')
ner = nltk.ne_chunk(tagged_words, binary=True)
print(ner)

#Lemmatizing all words
print('-----------word lemmatization------------------')
for w in words:
    print(lm.lemmatize(w))
print(lm.lemmatize('better',pos="a"))
print(lm.lemmatize('best', pos="a"))

#using wordnet - playing with synonyms and antonyms
print('----------wordnet-----------')
synonyms = wordnet.synsets("good")
synList = []
antList = []
for iterator in synonyms:
    for sys in iterator.lemmas():
        synList.append(sys.name())
        if sys.antonyms():
            antList.append(sys.antonyms()[0].name())
print(synList)
print(antList)

#wordnet - Word similarity
print('--- Word Similarity-----')
word1 = input('Enter word 1 :')
word2 = input('Enter word 2 :')
word1Synonyms  = wordnet.synsets(word1)
word2Synonyms = wordnet.synsets(word2)
print(word1Synonyms[0].wup_similarity(word2Synonyms[0]))
