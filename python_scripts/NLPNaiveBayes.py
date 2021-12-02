from os import read
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet
from nltk import NaiveBayesClassifier
import nltk
import string
import random
import pandas as pd
import numpy as np
all_words=[]
features=[]
lemmatizer=WordNetLemmatizer()
def getSimplePOS(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN
def clean_review(words):
    stop=stopwords.words('english')
    punctuation=string.punctuation
    output_words=[]
    words=word_tokenize(words)
    for w in words:
        if not w.lower() in stop and not w in punctuation:
            pos=pos_tag([w])
            output_words.append((lemmatizer.lemmatize(w, pos=getSimplePOS(pos[0][1]))).lower())
    return output_words
def get_feature_dict(words):
    words_set=set(words)
    current_features={}
    for w in features:
        current_features[w]=w in words_set
    return current_features
def mainf(inputf):
    global all_words
    all_words=[]
    global features
    features=[]
    data=[]
    for i in range(len(inputf)):
        data.append((inputf[i][0], inputf[i][1]))
#         print(i, (inputf[i][0], inputf[i][1]))
    random.shuffle(data)
    for i in range(len(data)):
        data[i]=(clean_review(data[i][0]), data[i][1])
    n=len(data)
    n=4*(n//5);
    training_doc=data[0:n]
    testing_doc=data[n:]
    testing_data2=[w[0] for w in testing_doc]
    for doc in training_doc:
        all_words+=doc[0]
    print(len(all_words))
    freq=nltk.FreqDist(all_words)
    common=freq.most_common(3000)
    features=[i[0] for i in common]
    training_doc=[(get_feature_dict(doc),category) for doc,category in training_doc]
    testing_doc=[(get_feature_dict(doc),category) for doc, category in testing_doc]
#     print(tr)
    return training_doc, testing_doc